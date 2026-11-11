def read_jd(path):      # read the JD file and return the content as str
    with open(path,"r",encoding='utf-8') as file:
        content = file.read()
        return content

def extract_jd_skill(content):      # extract the skills from it and a return a list of skills
    skills = content.split(',')
    stripped_skills = []
    for skill in skills:
        stripped_skills.append(skill.strip())
    return stripped_skills

# def Extract_JD(path):
#     content = read_jd(path)
#     return extract_jd_skill(content)
    
def Extract_JD(content):
    # content = read_jd(path)
    return extract_jd_skill(content)