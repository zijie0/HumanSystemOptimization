from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


def _default_root() -> Path:
    return Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class KnowledgeBase:
    root: Path
    data: dict[str, Any]

    def list_modules(self) -> list[dict[str, Any]]:
        return [
            {
                "id": module["id"],
                "title": module["title"],
                "summary": module["summary"],
                "priority": module["priority"],
                "chapter_path": module["chapter_path"],
            }
            for module in self.data["modules"]
        ]

    def get_module(self, module_id: str) -> dict[str, Any]:
        for module in self.data["modules"]:
            if module["id"] == module_id:
                return module
        raise KeyError(f"Unknown module_id: {module_id}")

    def search(self, query: str, limit: int = 5) -> list[dict[str, Any]]:
        tokens = [token.lower() for token in query.split() if token.strip()]
        if not tokens:
            return []

        scored: list[tuple[int, dict[str, Any]]] = []
        for module in self.data["modules"]:
            haystacks = self._search_fields(module)
            score = 0
            matches: list[str] = []
            for field in haystacks:
                lowered = field.lower()
                hits = sum(1 for token in tokens if token in lowered)
                if hits:
                    score += hits
                    matches.append(field)
            if score:
                scored.append(
                    (
                        score,
                        {
                            "module_id": module["id"],
                            "title": module["title"],
                            "summary": module["summary"],
                            "matches": matches[:6],
                        },
                    )
                )

        scored.sort(key=lambda item: (-item[0], self._module_rank(item[1]["module_id"])))
        return [item for _, item in scored[:limit]]

    def plan_template(self, focus: str = "general") -> dict[str, Any]:
        focus_id = focus if focus in {module["id"] for module in self.data["modules"]} else "general"
        selected = [
            module
            for module in self.data["modules"]
            if focus_id == "general" or module["id"] == focus_id
        ]
        if focus_id == "general":
            selected = self.data["modules"][:4]

        return {
            "focus": focus_id,
            "medical_boundary": self.data["medical_boundary"],
            "daily_actions": [
                {
                    "module_id": module["id"],
                    "title": module["title"],
                    "actions": module["practices"][:3],
                    "cautions": module["cautions"][:2],
                }
                for module in selected
            ],
            "tracking_metrics": self.data["tracking_metrics"],
            "review_cadence": "每 7 天回顾执行难度、睡眠/精力/运动/饮食记录，每 30 天结合身体指标或专业建议调整。",
        }

    def graph(self) -> dict[str, Any]:
        return self.data["graph"]

    def references(self) -> list[dict[str, Any]]:
        return self.data["references"]

    def _module_rank(self, module_id: str) -> int:
        for index, module in enumerate(self.data["modules"]):
            if module["id"] == module_id:
                return index
        return 10_000

    @staticmethod
    def _search_fields(module: dict[str, Any]) -> list[str]:
        fields = [module["title"], module["summary"]]
        for key in ("mechanisms", "practices", "cautions", "keywords"):
            fields.extend(module.get(key, []))
        fields.extend(ref["title"] for ref in module.get("references", []))
        return fields


def load_knowledge_base(root: Path | None = None) -> KnowledgeBase:
    repo_root = root or _default_root()
    index_path = repo_root / "skill" / "references" / "index.json"
    with index_path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return KnowledgeBase(root=repo_root, data=data)
