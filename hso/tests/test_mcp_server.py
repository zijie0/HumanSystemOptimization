from humansystemoptimization.mcp_server import (
    build_life_plan_payload,
    get_graph_payload,
    get_module_payload,
    list_modules_payload,
    search_knowledge_payload,
)


def test_list_modules_payload_contains_reader_paths():
    payload = list_modules_payload()

    assert payload["count"] >= 7
    assert payload["modules"][0]["id"] == "sleep"
    assert payload["modules"][0]["chapter_path"].startswith("references/modules/")


def test_search_knowledge_payload_returns_matches():
    payload = search_knowledge_payload("发酵 肠道")

    assert payload["query"] == "发酵 肠道"
    assert payload["results"][0]["module_id"] == "diet"


def test_get_module_payload_includes_assets_for_longevity():
    payload = get_module_payload("longevity")

    assert "imgs/diet_for_longevity.png" in payload["module"]["assets"]
    assert payload["medical_boundary"]


def test_build_life_plan_payload_includes_boundary_and_actions():
    payload = build_life_plan_payload("learning_focus")

    assert payload["plan"]["focus"] == "learning_focus"
    assert payload["plan"]["medical_boundary"]
    assert payload["plan"]["daily_actions"][0]["module_id"] == "learning_focus"


def test_get_graph_payload_exposes_nodes_and_edges():
    payload = get_graph_payload()

    assert any(node["id"] == "sleep" for node in payload["graph"]["nodes"])
    assert any(edge["target"] == "longevity" for edge in payload["graph"]["edges"])
