import streamlit as st

# アプリのタイトルと画像の設定
st.title("🍞 パン作りの魔法の計算機")

# ネット上のフリー画像などをここに差し込めます
st.image("https://unsplash.com", caption="焼き立てのパンをおうちで。")

st.markdown("---")

# 1. 粉の総量入力
total_flour = st.number_input("1. 粉の総量を決める (g)", min_value=50, max_value=2000, value=200, step=50)

# 2. パンのタイプ選択
bread_type = st.radio("2. パンの種類を選ぶ", ["食パン系（ふんわり）", "ハード系（リュスティックなど）", "おかず包み系（冷え冷えフィリング用）"])

# 3. オプション選択
is_overnight = st.checkbox("オーバーナイト（前夜仕込み・翌朝焼き）")

# --- 計算ロジック ---
water_pct = 70
salt_pct = 2.0
yeast_pct = 1.0

if bread_type == "食パン系（ふんわり）":
    water_pct = 68
    yeast_pct = 1.5
elif bread_type == "おかず包み系（冷え冷えフィリング用）":
    water_pct = 62
    yeast_pct = 1.5
elif bread_type == "ハード系（リュスティックなど）":
    water_pct = 80  # 高加水
    yeast_pct = 1.0

# オーバーナイトならイースト半量
if is_overnight:
    yeast_pct = yeast_pct * 0.5

# グラム計算
water_g = total_flour * (water_pct / 100)
salt_g = total_flour * (salt_pct / 100)
yeast_g = total_flour * (yeast_pct / 100)

# --- 結果の表示 ---
st.markdown("---")
st.subheader("📋 あなたの黄金レシピ")
st.write(f"・**強力粉:** {total_flour:.0f} g")
st.write(f"・**水:** {water_g:.0f} g (加水率 {water_pct}%)")
st.write(f"・**ドライイースト:** {yeast_g:.1f} g")
st.write(f"・**塩:** {salt_g:.1f} g")

if is_overnight:
    st.info("💡 **プロのTips:** 前日の夜にザッと混ぜたら、冷蔵庫の野菜室へポイッ。翌朝、室温に30分戻して焼きましょう！")
