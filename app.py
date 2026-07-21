import streamlit as st

st.title("🍞 プロ仕様・パン作りのカスタム計算機")
st.image("https://unsplash.com", caption="王道レシピをベースに、配合を自由にカスタマイズ。")
st.markdown("---")

# 1. 基本設定
st.header("1. 基本のボリューム")
total_flour = st.number_input("粉の総量を決める (g)", min_value=50, max_value=2000, value=200, step=50)

st.markdown("---")

# 【新機能】王道ベースの選択
st.header("2. 編集するベースのパンを選ぶ")
st.caption("選んだパンの『王道の比率』が下のスライダーに自動セットされます。そこから自由に微調整してください。")

base_type = st.selectbox(
    "ベースのパンを選択",
    [
        "高加水＆こねない系（リュスティック等）",
        "フランスパン系（準強力粉風・シンプル）",
        "食パン系（ふんわり・毎日用）",
        "基本の成形パン（甘め・菓子パン系）",
        "基本の成形パン（おかず・惣菜系）"
    ]
)

# 各ベースの初期値設定
init_water = 75
init_yeast = 1.0
init_salt = 2.0
init_sugar = 0
init_fat = 0

if base_type == "高加水＆こねない系（リュスティック等）":
    init_water = 80
    init_yeast = 0.5
    init_salt = 2.0
elif base_type == "フランスパン系（準強力粉風・シンプル）":
    init_water = 70
    init_yeast = 1.0
    init_salt = 2.0
elif base_type == "食パン系（ふんわり・毎日用）":
    init_water = 68
    init_yeast = 1.5
    init_salt = 2.0
    init_sugar = 5
    init_fat = 5
elif base_type == "基本の成形パン（甘め・菓子パン系）":
    init_water = 65
    init_yeast = 1.5
    init_salt = 1.5
    init_sugar = 15
    init_fat = 15
elif base_type == "基本の成形パン（おかず・惣菜系）":
    init_water = 62
    init_yeast = 1.5
    init_salt = 2.0
    init_sugar = 8
    init_fat = 8

st.markdown("---")

# 3. 粉の配分をカスタマイズ
st.header("3. 粉のブレンド比率（合計100%にしてください）")
st.caption("強力粉以外の粉を増やすと、強力粉の量が自動で引き算されます。")

rice_pct = st.slider("🌾 米粉の割合 (%)", min_value=0, max_value=50, value=0, step=5, key="rice")
whole_wheat_pct = st.slider("🟤 全粒粉の割合 (%)", min_value=0, max_value=50, value=0, step=5, key="whole")

# 強力粉は残りのパーセント
wheat_pct = 100 - rice_pct - whole_wheat_pct

# エラーバグ修正：st.emptyを使って画面描写を安定させる
error_placeholder = st.empty()
if wheat_pct < 0:
    error_placeholder.error("⚠️ 粉の合計が100%を超えています！米粉や全粒粉の割合を減らしてください。")
    st.stop()
else:
    st.write(f"・現在のベース粉（強力粉）の割合: **{wheat_pct}%**")

st.markdown("---")

# 4. 水分・副材料の微調整（初期値にベースパンの数値を連動！）
st.header("4. 水分・ベーカーズパーセントの微調整")
st.caption("上で選んだパンの基準値になっています。スライダーで好みに書き換えてOK！")

water_pct = st.slider("💧 水分量（加水率 %）", min_value=50, max_value=90, value=init_water, step=1, key="water")
yeast_pct = st.slider("🧪 ドライイースト (%)", min_value=0.1, max_value=3.0, value=float(init_yeast), step=0.1, key="yeast")
salt_pct = st.slider("🧂 塩 (%)", min_value=0.0, max_value=3.0, value=float(init_salt), step=0.1, key="salt")
sugar_pct = st.slider("🍬 砂糖 (%)", min_value=0, max_value=25, value=init_sugar, step=1, key="sugar")
fat_pct = st.slider("🧈 油脂 (%)", min_value=0, max_value=25, value=init_fat, step=1, key="fat")

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

# 粉がフランスパン系のときは「準強力粉（または強力粉＋薄力粉）」と表示する粋な演出
flour_label = "準強力粉（または強力粉8割＋薄力粉2割）" if base_type == "フランスパン系（準強力粉風・シンプル）" else "強力粉"

st.write(f"・**{flour_label}:** {wheat_g:.0f} g ({wheat_pct}%)")
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

# 動的なアドバイス表示
st.markdown("---")
st.subheader("💡 配合診断アドバイス")
advice_placeholder = st.empty()

if rice_pct > 20:
    st.warning("⚠️ **米粉が20%を超えています:** グルテンが不足して膨らみにくくなる可能性があります。少ししっかりめに捏ねるか、型に入れて焼くのが安全です。")
if water_pct >= 80:
    st.info("💧 **超・高加水モードです:** 生地がかなりドロドロになります。捏ねずに、タッパーの中で『折りたたむ』ようにして発酵させ、リュスティック風にスプーンやカードで切り分けて焼きましょう！")
if base_type == "フランスパン系（準強力粉風・シンプル）" and (sugar_pct > 0 or fat_pct > 0):
    st.info("🥖 **アレンジTips:** 本格フランスパンは砂糖・油脂0%ですが、あえて少し加えることで、皮が柔らかく食べやすいソフトフランスになりますよ！")
