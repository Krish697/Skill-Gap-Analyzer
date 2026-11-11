from resume_extract import Resume_Extract
from jd_extract import Extract_JD

def Skill_Gap(resume_path , jd_content):

    resume_skills = Resume_Extract(resume_path)
    jd_skills = Extract_JD(jd_content)

    resume_set= set(resume_skills)
    jd_set= set(jd_skills)

    skill_gap = jd_set - resume_set
    return skill_gap
