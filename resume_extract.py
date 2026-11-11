import pymupdf as pf

def read_file(path):
    print(path)
    filename = path.name

    if filename.lower().endswith(".txt"):
        print("TXt")
        # with open(path, "r", encoding='utf-8') as file:  # used encoding to ignore some of the special Characters
        #     content = file.read()
        content = path.getvalue().decode("utf-8")
    
    elif filename.lower().endswith(".pdf"):
        print("PDF")
        pdf = pf.open(stream=path.getvalue() , filetype="pdf")
        # pdf = pf.open(path)
        content = ""
        
        for page in pdf:
            content += page.get_text()
        print(content)
    
    return content



    return content      # returns str

def find_skill_section(content):
    section_heading = ["Experience","Work Experience","Projects","Education","Certifications","Achievements"]
    start = content.find("Skills Summary")

    end_pos = []
    for i in  section_heading:
        end_pos.append(content.find(i , start))

    valid_pos = []

    for i in end_pos:
        if i != -1 and i > start:
            valid_pos.append(i)

    end = min(valid_pos)
    text = content[start:end]
    return text         # returns the skills section as a str

def extract_skills(text):

    lines = text.splitlines()          # splits the whole text string on different lines in a list
    lines = lines[1:]           # removes the Skills Summary section
    skill_section = []          # only the skills not its category

    for line in lines:          # removes the category and separates the individual skills 
        colon_pos = line.find(":")
        
        line = line[colon_pos+1:]
        skill_section.append(line.split(","))

    final_skills= []        # refined skills 

    for skills in skill_section:        #refining of the skills by removing white spaces from the ends
        for skill in skills:
            final_skills.append(skill.strip())

    return final_skills             # returns a list of individual skills



def Resume_Extract(path):
    content = read_file(path)
    text = find_skill_section(content)
    resume_skills = extract_skills(text)
    return resume_skills