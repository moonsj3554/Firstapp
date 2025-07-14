import streamlit as st

# MBTI별 직업 추천 사전
mbti_jobs = {
    "ISTJ": ["회계사", "행정관리자", "법률사무원"],
    "ISFJ": ["간호사", "초등교사", "사회복지사"],
    "INFJ": ["상담가", "작가", "심리학자"],
    "INTJ": ["전략기획가", "과학자", "IT 컨설턴트"],
    "ISTP": ["엔지니어", "기술 분석가", "경찰관"],
    "ISFP": ["예술가", "디자이너", "물리치료사"],
    "INFP": ["작가", "심리상담사", "사회운동가"],
    "INTP": ["데이터 과학자", "연구원", "소프트웨어 개발자"],
    "ESTP": ["세일즈 매니저", "기업가", "운동선수"],
    "ESFP": ["배우", "이벤트 플래너", "여행가이드"],
    "ENFP": ["기획자", "마케터", "인적자원 전문가"],
    "ENTP": ["스타트업 창업자", "변호사", "기획 컨설턴트"],
    "ESTJ": ["군인", "경영 관리자", "프로젝트 매니저"],
    "ESFJ": ["간호사", "교사", "호텔매니저"],
    "ENFJ": ["상담사", "교육자", "홍보전문가"],
    "ENTJ": ["CEO", "변호사", "전략 컨설턴트"]
}

# Streamlit 앱 구성
st.title("MBTI 기반 직업 추천 웹앱")

st.write("당신의 MBTI 유형을 선택하면 어울리는 직업 3가지를 추천해드릴게요.")

selected_mbti = st.selectbox("MBTI를 선택하세요:", list(mbti_jobs.keys()))

if selected_mbti:
    st.subheader(f"🔍 {selected_mbti} 유형에게 추천하는 직업:")
    for i, job in enumerate(mbti_jobs[selected_mbti], 1):
        st.write(f"{i}. {job}")
