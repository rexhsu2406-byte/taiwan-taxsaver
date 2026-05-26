import streamlit as st

from engine.decision_tree import (
    QUESTION_TREE,
    get_next_question,
    get_strategies,
    get_strategies_from_multiselect,
    is_info_page,
    is_multi_select,
    is_result,
)
from knowledge.strategies import STRATEGIES


TAG_COLORS = {
    "上班族": "#16a34a",
    "企業主": "#f97316",
    "高資產": "#dc2626",
}


def init_state():
    if "current_key" not in st.session_state:
        st.session_state["current_key"] = "TAX_INTRO"
    if "history" not in st.session_state:
        st.session_state["history"] = []


def go_back():
    if st.session_state["history"]:
        previous_key, _ = st.session_state["history"].pop()
        st.session_state["current_key"] = previous_key
        st.rerun()


def render_subtitle(subtitle):
    if subtitle:
        st.caption(subtitle)


def render_back_button():
    if st.session_state["history"]:
        left, _ = st.columns([1, 3])
        with left:
            if st.button("← 上一題", use_container_width=True):
                go_back()


def render_question_page(current_key):
    question = QUESTION_TREE[current_key]
    st.title(question["text"])
    render_subtitle(question.get("subtitle", ""))
    st.write("")

    for option in question["options"]:
        if st.button(option, use_container_width=True):
            next_key = get_next_question(current_key, option)
            st.session_state["history"].append((current_key, option))
            st.session_state["current_key"] = next_key
            st.rerun()

    st.write("")
    render_back_button()


def render_info_page(current_key):
    page = QUESTION_TREE[current_key]
    st.title(page["text"])
    render_subtitle(page.get("subtitle", ""))
    st.write("")

    for line in page.get("content", []):
        if line.strip():
            st.info(line)

    st.write("")
    if st.button("了解了，開始評估我的節稅方案 →", use_container_width=True):
        st.session_state["history"].append((current_key, "了解"))
        st.session_state["current_key"] = page["next"]
        st.rerun()

    st.write("")
    render_back_button()


def render_multi_select_page(current_key):
    question = QUESTION_TREE[current_key]
    st.title(question["text"])
    render_subtitle(question.get("subtitle", ""))
    st.write("")

    selected_options = []
    for option in question["options"]:
        if st.checkbox(option, key=f"{current_key}_{option}"):
            selected_options.append(option)

    st.write("")
    if st.button("確認，看我的節稅方案 ✅", use_container_width=True):
        strategies = get_strategies_from_multiselect(current_key, selected_options)
        st.session_state["result_strategies"] = strategies
        st.session_state["current_key"] = "RESULT_MULTI"
        st.rerun()

    st.write("")
    render_back_button()


def tag_badge(tag):
    color = TAG_COLORS.get(tag, "#64748b")
    return (
        f"<span style='background:{color}; color:white; padding:0.15rem 0.55rem; "
        "border-radius:999px; font-size:0.78rem; font-weight:700; "
        "vertical-align:middle; white-space:nowrap;'>"
        f"{tag}</span>"
    )


def render_strategy_card(strategy):
    tag = strategy["tag"]
    st.markdown(
        f"### {strategy['title']} {tag_badge(tag)}",
        unsafe_allow_html=True,
    )
    st.markdown(f"**節稅潛力：** {strategy['節稅潛力']}")
    st.write(strategy["白話說明"])

    case = strategy["真實案例"]
    st.success(f"**{case['標題']}**\n\n{case['內容']}")
    st.warning(f"**注意事項：** {strategy['注意事項']}")

    with st.expander("法規依據"):
        st.write(strategy["法規依據"])


def render_result_page(current_key):
    st.title("你的節稅方案")
    st.caption("根據你的狀況，以下是最值得優先執行的建議")
    st.write("")

    if current_key == "RESULT_MULTI":
        strategy_ids = st.session_state.get("result_strategies", [])
    else:
        strategy_ids = get_strategies(current_key)

    visible_strategy_ids = strategy_ids[:3]
    for index, strategy_id in enumerate(visible_strategy_ids):
        strategy = STRATEGIES.get(strategy_id)
        if not strategy:
            continue
        render_strategy_card(strategy)
        if index < len(visible_strategy_ids) - 1:
            st.divider()

    remaining_count = len(strategy_ids) - len(visible_strategy_ids)
    if remaining_count > 0:
        st.markdown(
            f"<p style='color:#6b7280; font-size:0.88rem;'>還有 {remaining_count} 個相關策略，建議諮詢專業會計師了解更多</p>",
            unsafe_allow_html=True,
        )

    st.write("")
    if st.button("重新評估 🔄", use_container_width=True):
        st.session_state.clear()
        st.session_state["current_key"] = "TAX_INTRO"
        st.session_state["history"] = []
        st.rerun()


def main():
    st.set_page_config(page_title="台灣節稅專家系統", page_icon="💰")
    init_state()

    current_key = st.session_state["current_key"]
    if current_key == "RESULT_MULTI" or is_result(current_key):
        render_result_page(current_key)
    elif is_info_page(current_key):
        render_info_page(current_key)
    elif is_multi_select(current_key):
        render_multi_select_page(current_key)
    else:
        render_question_page(current_key)


if __name__ == "__main__":
    main()
