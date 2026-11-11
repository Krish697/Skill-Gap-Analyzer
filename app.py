import streamlit as st
from skill_gap import Skill_Gap

st.title("SkillGap Analyzer" , text_alignment="center")

st.header("1) Resume")

uploaded_resume_file = st.file_uploader(
    "Upload Your Resume : ",
    type=["txt","pdf"]
)
st.header("2) Job Description")

uploaded_jd_content = st.text_area(
    "Enter Job Description Skills",
    placeholder="e.g. Python, SQL, Flask, Django, Machine Learning..."
)

if st.button("Find Skill Gap"):
    # st.write(type(uploaded_resume_file))
    # st.write(type(uploaded_jd_content))
    if uploaded_resume_file is not None and uploaded_jd_content is not None:

        skills = Skill_Gap(uploaded_resume_file , uploaded_jd_content)

        st.subheader("Missing Skills")

        for i, skill in enumerate(skills , start=1):
            st.markdown(f'{i}. :rainbow[{skill}]')
    else:
        st.warning("Please upload a resume and enter JD Skills")

