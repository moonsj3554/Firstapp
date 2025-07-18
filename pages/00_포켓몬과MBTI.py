import streamlit as st

# MBTI별 추천 포켓몬과 이유
mbti_pokemon = {
    "ISTJ": ("리자몽", "성실하고 책임감 있는 ISTJ처럼 리자몽은 진중하고 강한 리더의 상징입니다."),
    "ISFJ": ("이브이", "배려심 깊고 조화로운 ISFJ는 다양한 진화를 통해 주변에 적응하는 이브이와 닮았습니다."),
    "INFJ": ("뮤", "이상주의자 INFJ는 신비롭고 고귀한 존재인 뮤와 같은 느낌을 줍니다."),
    "INTJ": ("뮤츠", "전략적이고 통찰력 있는 INTJ는 냉철하고 강력한 지능형 포켓몬 뮤츠와 잘 어울립니다."),
    "ISTP": ("겟핫무", "논리적이고 실용적인 ISTP는 날렵하고 전투에 능한 겟핫무와 유사합니다."),
    "ISFP": ("피카츄", "자유롭고 따뜻한 ISFP는 밝고 사랑스러운 피카츄와 잘 어울려요."),
    "INFP": ("세레비", "이상과 자연을 사랑하는 INFP는 시간여행자 세레비처럼 순수한 마음을 지녔습니다."),
    "INTP": ("레지기가스", "탐구심 많은 INTP는 고대의 지식과 힘을 간직한 레지기가스와 닮았습니다."),
    "ESTP": ("갸라도스", "대담하고 에너지 넘치는 ESTP는 폭발적인 힘을 가진 갸라도스와 잘 어울립니다."),
    "ESFP": ("토게키스", "사교적이고 긍정적인 ESFP는 희망과 행운을 상징하는 토게키스와 닮았습니다."),
    "ENFP": ("루카리오", "열정적이고 영감을 주는 ENFP는 정의감 넘치는 루카리오와 비슷합니다."),
    "ENTP": ("팬텀", "아이디어가 넘치는 ENTP는 장난기 많고 창의적인 팬텀과 유사합니다."),
    "ESTJ": ("코리갑", "체계적이고 실용적인 ESTJ는 규율을 중시하는 코리갑과 어울립니다."),
    "ESFJ": ("푸크린", "다정하고 사람을 잘 챙기는 ESFJ는 돌봄과 힐링의 포켓몬 푸크린과 잘 맞아요."),
    "ENFJ": ("아르세우스", "타인을 이끄는 카리스마 있는 ENFJ는 창조신 포켓몬 아르세우스와 비슷한 위엄이 있어요."),
    "ENTJ": ("다크라이", "리더십 있고 결단력 있는 ENTJ는 압도적인 카리스마의 다크라이와 어울립니다.")
}

# Streamlit 앱 구성
st.title("🌟 MBTI 기반 포켓몬 추천기")

st.write("MBTI를 선택하면, 당신에게 어울리는 포켓몬을 추천해드릴게요!")

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_pokemon.keys()))

if selected_mbti:
    pokemon, reason = mbti_pokemon[selected_mbti]
    st.subheader(f"🧬 {selected_mbti} 유형에게 어울리는 포켓몬은...")
    st.markdown(f"## 🎉 {pokemon}!")
    st.write(f"**추천 이유:** {reason}")
