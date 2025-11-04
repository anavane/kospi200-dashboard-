# app.py
import streamlit as st
import pandas as pd

# -------------------------------
# PAGE SETTINGS
# -------------------------------
st.set_page_config(
    page_title="KOSPI200 주식 추천 시스템",
    page_icon="📈",
    layout="wide"
)

st.title("📈 코스피200 주식 추천 시스템")
st.caption("초보자도 쉽게 이해하는 주식 분석 도구")

# Sidebar
st.sidebar.header("설정")
st.sidebar.markdown("### ⚙️ API 인증 정보")
st.sidebar.write("데모 버전에서는 인증이 필요하지 않습니다.")

# Analysis Settings
st.sidebar.markdown("### 📊 분석 설정")
top_n = st.sidebar.slider("추천할 종목 개수", 1, 10, 5)
min_volume = st.sidebar.number_input("최소 거래 규모 (억원)", value=100, step=10)

if st.sidebar.button("🔍 분석 시작하기"):
    st.session_state["analyze"] = True

if st.sidebar.button("🔄 새로 분석하기"):
    st.session_state["analyze"] = False

# -------------------------------
# MOCK DATA (DEMO)
# -------------------------------
dummy_data = [
    {"rank": 1, "name": "NAVER", "price": 280000, "score": 9.0, "volume": 4935, "return": 11.6, "volatility": "높음"},
    {"rank": 2, "name": "삼성전자", "price": 109900, "score": 7.5, "volume": 25052, "return": 4.7, "volatility": "보통"},
    {"rank": 3, "name": "카카오", "price": 64900, "score": 7.5, "volume": 1996, "return": 6.6, "volatility": "높음"},
    {"rank": 4, "name": "현대차", "price": 189000, "score": 7.2, "volume": 1230, "return": 5.4, "volatility": "보통"},
    {"rank": 5, "name": "삼성물산", "price": 120000, "score": 6.9, "volume": 950, "return": 3.1, "volatility": "낮음"},
]

df = pd.DataFrame(dummy_data)

# -------------------------------
# MAIN CONTENT
# -------------------------------
st.markdown("---")
st.subheader(f"🎯 추천 종목 TOP {top_n}")
st.write("점수가 높을수록 지금 매수하기 좋은 종목입니다.")

cols = st.columns(top_n)

for i, row in df.head(top_n).iterrows():
    with cols[i]:
        st.markdown(f"### {row['rank']}위. {row['name']}")
        st.metric("현재가", f"{row['price']:,}원", f"{row['return']}%")
        st.metric("추천 점수", f"{row['score']}점")
        st.markdown(f"📊 **평균 거래액:** {row['volume']:,}억원")
        st.markdown(f"📈 **가격 변동성:** {row['volatility']}")
        st.markdown("✅ **매수 신호:** 상승 추세 진입<br>✅ 강한 상승세 지속 중<br>✅ 적정 가격대 유지", unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# FOOTER
# -------------------------------
st.caption("데이터는 데모용이며 실제 투자 조언이 아닙니다.")
