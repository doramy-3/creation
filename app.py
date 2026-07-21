import streamlit as st

st.title("🍞 プロ仕様・パン作りのカスタム計算機")
st.image("https://unsplash.com", caption="配合を自由にデザインしよう。")
st.markdown("---")

# 1. 基本設定
st.header("1. 基本のボリューム")
total_flour = st.number_input("粉の総量を決める (g)", min_value=50, max_value=2000, value=200, step=50)

st.markdown("---")

# 2. 粉の配分をカスタマイズ
st.header("2. 粉のブレンド比率（合計100%にしてください）")
st.caption("強力粉以外の粉を増やすと、強力粉の量が自動で引き算されます。")

rice_pct = st.slider("🌾 米粉の割合 (%)", min_value=0, max_value=50, value=0, step=5)
whole_wheat_pct = st.slider("🟤 全粒粉の割合 (%)", min_value=0, max_value=50, value=0, step=5)

# 強力粉は残りのパーセント
wheat_pct = 100 - rice_pct - whole_wheat_pct

# 100%を超えてしまった場合の警告
if wheat_pct < 0:
    st.error("⚠️ 粉の合計が100%を超えています！米粉や全粒粉の割合を減らしてください。")
    st.stop()

st.write(f"・現在のベース粉（強力粉）の割合: **{wheat_pct}%**")

st.markdown("---")

# 3. 水分・副材料の微調整
st.header("3. 水分・ベーカーズパーセントの微調整")

# デフォルト値を少し高加水寄りに設定
water_pct = st.slider("💧 水分量（加水率 %）", min_value=50, max_value=90, value=75, step=1)
yeast_pct = st.slider("🧪 ドライイースト (%)", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
salt_pct = st.slider("🧂 塩 (%)", min_value=0.0, max_value=3.0, value=2.0, step=0.1)

# おまけの砂糖・油脂カスタム
sugar_pct = st.slider("🍬 砂糖 (%)", min_value=0, max_value=25, value=0, step=1)
fat_pct = st.slider("🧈 油脂 (%)", min_value=0, max_value=25, value=0, step=1)

# --- グラム計算 ---
wheat_g = total_flour * (wheat_pct / 100)
rice_g = total_flour * (rice_pct / 100)
whole_wheat_g = total_flour * (whole_wheat_pct / 100)

water_g = total_flour * (water_pct / 100)
yeast_g = total_flour * (yeast_pct / 100)
salt_g = total_flour * (salt_pct / 100)
sugar_g = total_flour * (sugar_pct / 100)
fat_g = total_flour * (fat_pct / 100)

# --- 結果の表示 ---
st.markdown("---")
st.subheader("📋 あなたがデザインした黄金レシピ")

st.write(f"・**強力粉:** {wheat_g:.0f} g ({wheat_pct}%)")
if rice_g > 0:
    st.write(f"・**米粉:** {rice_g:.0f} g ({rice_pct}%)")
if whole_wheat_g > 0:
    st.write(f"・**全粒粉:** {whole_wheat_g:.0f} g ({whole_wheat_pct}%)")

st.write(f"・**水:** {water_g:.0f} g (加水率 {water_pct}%)")
st.write(f"・**ドライイースト:** {yeast_g:.1f} g ({yeast_pct}%)")
st.write(f"・**塩:** {salt_g:.1f} g ({salt_pct}%)")

if sugar_g > 0:
    st.write(f"・**砂糖:** {sugar_g:.1f} g ({sugar_pct}%)")
if fat_g > 0:
    st.write(f"・**油脂:** {fat_g:.1f} g ({fat_pct}%)")

# 動的な警告アドバイス
st.markdown("---")
st.subheader("💡 配合診断アドバイス")
if rice_pct > 20:
    st.warning("⚠️ **米粉が20%を超えています:** グルテンが不足して膨らみにくくなる可能性があります。少ししっかりめに捏ねるか、型に入れて焼くのが安全です。")
if water_pct >= 80:
    st.info("💧 **超・高加水モードです:** 生地がかなりドロドロになります。捏ねずに、タッパーの中で『折りたたむ』ようにして発酵させ、リュスティック風にスプーンやカードで切り分けて焼きましょう！")
