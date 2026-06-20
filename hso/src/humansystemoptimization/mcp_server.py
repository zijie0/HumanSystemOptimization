from __future__ import annotations

import argparse
import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from humansystemoptimization.knowledge import load_knowledge_base


SERVER_NAME = "human-system-optimization"


def list_modules_payload() -> dict[str, Any]:
    kb = load_knowledge_base()
    modules = kb.list_modules()
    return {
        "count": len(modules),
        "modules": modules,
        "medical_boundary": kb.data["medical_boundary"],
    }


def search_knowledge_payload(query: str, limit: int = 5) -> dict[str, Any]:
    kb = load_knowledge_base()
    return {
        "query": query,
        "limit": limit,
        "results": kb.search(query, limit=limit),
        "medical_boundary": kb.data["medical_boundary"],
    }


def get_module_payload(module_id: str) -> dict[str, Any]:
    kb = load_knowledge_base()
    return {
        "module": kb.get_module(module_id),
        "medical_boundary": kb.data["medical_boundary"],
    }


def build_life_plan_payload(focus: str = "general") -> dict[str, Any]:
    kb = load_knowledge_base()
    return {
        "plan": kb.plan_template(focus),
        "source": kb.data["source"],
    }


def get_graph_payload() -> dict[str, Any]:
    kb = load_knowledge_base()
    return {
        "graph": kb.graph(),
        "medical_boundary": kb.data["medical_boundary"],
    }


def create_server() -> FastMCP:
    mcp = FastMCP(SERVER_NAME)

    @mcp.tool()
    def list_modules() -> dict[str, Any]:
        """List the structured health habit knowledge modules."""
        return list_modules_payload()

    @mcp.tool()
    def search_knowledge(query: str, limit: int = 5) -> dict[str, Any]:
        """Search the local health habit knowledge base by keyword."""
        return search_knowledge_payload(query=query, limit=limit)

    @mcp.tool()
    def get_module(module_id: str) -> dict[str, Any]:
        """Return one full knowledge module by id."""
        return get_module_payload(module_id=module_id)

    @mcp.tool()
    def build_life_plan(focus: str = "general") -> dict[str, Any]:
        """Build a conservative habit-plan template for a module or general health."""
        return build_life_plan_payload(focus=focus)

    @mcp.tool()
    def get_graph() -> dict[str, Any]:
        """Return knowledge graph nodes and edges."""
        return get_graph_payload()

    return mcp


def _self_test() -> dict[str, Any]:
    modules = list_modules_payload()
    graph = get_graph_payload()
    return {
        "server": SERVER_NAME,
        "module_count": modules["count"],
        "graph_nodes": len(graph["graph"]["nodes"]),
        "graph_edges": len(graph["graph"]["edges"]),
        "tools": [
            "list_modules",
            "search_knowledge",
            "get_module",
            "build_life_plan",
            "get_graph",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="HumanSystemOptimization MCP server")
    parser.add_argument("--self-test", action="store_true", help="Load local knowledge and print a JSON health check.")
    args = parser.parse_args()

    if args.self_test:
        print(json.dumps(_self_test(), ensure_ascii=False, indent=2))
        return

    create_server().run()


if __name__ == "__main__":
    main()
