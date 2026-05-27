QUESTION_TREE = {

    "Q1": {
        "text": "你的收入主要來源是什麼？",
        "subtitle": "請選最主要的一項",
        "options": {
            "薪資": "Q2A",
            "公司營業所得": "Q2B",
            "股票、基金、不動產等資本利得": "Q2C",
        }
    },

    "TAX_INTRO": {
        "text": "先了解一下台灣的所得稅級距",
        "subtitle": "這會幫助你理解為什麼這些節稅方法有效",
        "type": "info_page",
        "content": [
            "台灣所得稅採「累進稅率」，收入越高、稅率越高：",
            "",
            "課稅所得 0 ～ 56 萬：稅率 5%",
            "課稅所得 56 ～ 126 萬：稅率 12%",
            "課稅所得 126 ～ 252 萬：稅率 20%",
            "課稅所得 252 ～ 472 萬：稅率 30%",
            "課稅所得 472 萬以上：稅率 40%",
            "",
            "📌 課稅所得 = 你的收入，扣掉各種扣除額之後的金額",
            "📌 節稅的核心：合法讓課稅所得降低，適用更低的稅率",
            "📌 舉例：年收入 150 萬的上班族，透過合法扣除額多扣 30 萬後，課稅所得降到 126 萬以下，稅率從 20% 降到 12%，每年少繳約 2.4 萬元",
        ],
        "next": "Q1",
    },

    "Q2A": {
        "text": "除了薪資之外，你有以下情況嗎？",
        "subtitle": "可以複選，選完後點確認",
        "type": "multi_select",
        "options": {
            "有扶養父母、子女或其他親屬": ["dependent_deduction", "elder_live_in", "elder_separate"],
            "有租屋支出":    ["rent_deduction"],
            "有房貸支出":    ["mortgage_interest"],
            "公司有給股票選擇權":  ["esop_timing"],
        },
        "always_include": ["salary_defer", "labor_pension"],
    },

    "Q2B": {
        "text": "公司目前的年營業額大概是？",
        "subtitle": "",
        "options": {
            "500萬以下": "Q3B1",
            "500萬～3000萬":       "Q3B2",
            "3000萬以上":          "Q3B3",
        }
    },

    "Q3B1": {
        "text": "公司目前有哪些主要支出？",
        "subtitle": "",
        "options": {
            "人事費用": "RESULT_B1_SALARY",
            "設備、車輛、軟體等採購":           "RESULT_B1_ASSET",
            "都有":                             "RESULT_B1_ALL",
        }
    },

    "Q3B2": {
        "text": "你有把公司獲利以股利形式分給自己嗎？",
        "subtitle": "",
        "options": {
            "有，每年都分":       "RESULT_B2_DIVIDEND",
            "沒有，留在公司裡":   "RESULT_B2_RETAIN",
            "不確定怎麼做比較好": "RESULT_B2_UNSURE",
        }
    },

    "Q3B3": {
        "text": "公司股權目前的狀況？",
        "subtitle": "",
        "options": {
            "全部自己持有":       "RESULT_B3_SOLO",
            "有家人一起持股":     "RESULT_B3_FAMILY",
            "考慮未來傳給下一代": "RESULT_B3_INHERIT",
        }
    },

    "Q2C": {
        "text": "你的資產主要是哪種形式？",
        "subtitle": "",
        "options": {
            "股票": "Q3C1",
            "不動產":   "Q3C2",
            "現金或存款為主":         "Q3C3",
        }
    },

    "Q3C1": {
        "text": "這些股票你打算怎麼處理？",
        "subtitle": "",
        "options": {
            "長期持有，不打算賣": "RESULT_C1_HOLD",
            "未來會賣，想規劃節稅": "RESULT_C1_SELL",
            "想傳給下一代": "RESULT_C1_INHERIT",
        }
    },

    "Q3C2": {
        "text": "不動產的用途？",
        "subtitle": "",
        "options": {
            "出租收租金":         "RESULT_C2_RENT",
            "自住，未來可能出售": "RESULT_C2_SELL",
            "想傳承給子女":       "RESULT_C2_INHERIT",
        }
    },

    "Q3C3": {
        "text": "這些資金未來的規劃？",
        "subtitle": "",
        "options": {
            "想投資但不確定怎麼節稅": "RESULT_C3_INVEST",
            "想做財富傳承規劃":       "RESULT_C3_INHERIT",
        }
    },
}

RESULT_MAP = {
    "RESULT_B1_SALARY":   ["salary_expense", "owner_salary"],
    "RESULT_B1_ASSET":    ["asset_depreciation", "expense_maximize"],
    "RESULT_B1_ALL":      ["salary_expense", "owner_salary", "asset_depreciation", "expense_maximize"],
    "RESULT_B2_DIVIDEND": ["dividend_vs_retain", "personal_vs_corp_tax"],
    "RESULT_B2_RETAIN":   ["retained_earnings", "dividend_vs_retain"],
    "RESULT_B2_UNSURE":   ["personal_vs_corp_tax", "dividend_vs_retain", "retained_earnings"],
    "RESULT_B3_SOLO":     ["family_company", "personal_vs_corp_tax"],
    "RESULT_B3_FAMILY":   ["family_company", "family_salary"],
    "RESULT_B3_INHERIT":  ["family_company", "trust_business", "gift_plan"],
    "RESULT_C1_HOLD":     ["unrealized_gain", "stock_pledge"],
    "RESULT_C1_SELL":     ["unrealized_gain", "art_investment"],
    "RESULT_C1_INHERIT":  ["gift_plan", "trust_wealth"],
    "RESULT_C2_RENT":     ["rental_expense", "rental_tax_optimize"],
    "RESULT_C2_SELL":     ["land_value_tax", "gift_plan"],
    "RESULT_C2_INHERIT":  ["gift_plan", "trust_wealth", "land_value_tax"],
    "RESULT_C3_INVEST":   ["art_investment", "unrealized_gain", "stock_pledge"],
    "RESULT_C3_INHERIT":  ["trust_wealth", "gift_plan"],
}

def get_next_question(current_q, answer):
    if current_q not in QUESTION_TREE:
        return None
    return QUESTION_TREE[current_q]["options"].get(answer)

def is_result(key):
    return key is not None and key.startswith("RESULT_")

def is_info_page(key):
    return key in QUESTION_TREE and QUESTION_TREE[key].get("type") == "info_page"

def is_multi_select(key):
    return key in QUESTION_TREE and QUESTION_TREE[key].get("type") == "multi_select"

def get_strategies(result_id):
    return RESULT_MAP.get(result_id, [])

def get_strategies_from_multiselect(question_key, selected_options):
    q = QUESTION_TREE[question_key]
    result = []
    for option in selected_options:
        for s in q["options"].get(option, []):
            if s not in result:
                result.append(s)
    for s in q.get("always_include", []):
        if s not in result:
            result.append(s)
    if not result:
        result = list(q.get("always_include", []))
    return result
