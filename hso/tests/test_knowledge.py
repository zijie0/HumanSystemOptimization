from pathlib import Path

from humansystemoptimization.knowledge import load_knowledge_base


def test_lists_core_modules_in_readme_order():
    kb = load_knowledge_base(Path(__file__).resolve().parents[2])

    module_ids = [module["id"] for module in kb.list_modules()]

    assert module_ids[:7] == [
        "sleep",
        "diet",
        "mindset_dopamine",
        "learning_focus",
        "brain_health",
        "longevity",
        "personal_practice",
    ]


def test_search_finds_practices_across_modules():
    kb = load_knowledge_base(Path(__file__).resolve().parents[2])

    results = kb.search("早晨 阳光 睡眠")

    assert results[0]["module_id"] == "sleep"
    assert any("起床后" in hit for hit in results[0]["matches"])


def test_get_module_preserves_cautions_and_references():
    kb = load_knowledge_base(Path(__file__).resolve().parents[2])

    module = kb.get_module("longevity")

    assert "Sinclair" in module["summary"]
    assert any("争议" in caution for caution in module["cautions"])
    assert any(ref["title"] == "程序员延寿指南" for ref in module["references"])


def test_plan_template_returns_actionable_sections_for_focus():
    kb = load_knowledge_base(Path(__file__).resolve().parents[2])

    plan = kb.plan_template("sleep")

    assert plan["focus"] == "sleep"
    assert plan["medical_boundary"]
    assert any(item["module_id"] == "sleep" for item in plan["daily_actions"])
    assert any("睡眠" in metric for metric in plan["tracking_metrics"])
