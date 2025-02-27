job_roles = [
    {"role": "Software Engineer", "skills": ["Python", "Java", "C++", "Git", "Algorithms", "Data Structures"]},
    {"role": "Data Analyst", "skills": ["SQL", "Excel", "Python", "Power BI", "Tableau", "Statistics"]},
    {"role": "Machine Learning Engineer", "skills": ["Python", "TensorFlow", "PyTorch", "Deep Learning", "NLP", "Computer Vision"]},
    {"role": "Frontend Developer", "skills": ["HTML", "CSS", "JavaScript", "React", "Vue.js", "UI/UX Design"]},
    {"role": "Backend Developer", "skills": ["Node.js", "Django", "Flask", "Databases", "REST API", "Microservices"]},
    {"role": "DevOps Engineer", "skills": ["Docker", "Kubernetes", "AWS", "CI/CD", "Terraform", "Linux"]},
    {"role": "Cybersecurity Specialist", "skills": ["Penetration Testing", "Network Security", "Ethical Hacking", "Cryptography", "SIEM"]},
    {"role": "Database Administrator", "skills": ["SQL", "NoSQL", "MySQL", "MongoDB", "PostgreSQL", "Database Optimization"]},
    {"role": "Product Manager", "skills": ["Agile", "Scrum", "Business Analysis", "Market Research", "Communication", "Leadership"]},
    {"role": "UX/UI Designer", "skills": ["Figma", "Adobe XD", "Sketch", "User Research", "Wireframing", "Prototyping"]}
]

my_skills = ['SQL', 'Python', 'Power BI']
for job in job_roles:
    quantity = True
    for skill in my_skills:
        if skill not in job['skills']:
            quantity = False
            break
        print(job)

job_data = [
    {
        "remote": True,
        "job_title": "Software Engineer",
        "job_skills": ["Python", "Django", "REST API", "Docker"]
    },
    {
        "remote": False,
        "job_title": "Data Analyst",
        "job_skills": ["SQL", "Excel", "Tableau", "Python"]
    },
    {
        "remote": True,
        "job_title": "Machine Learning Engineer",
        "job_skills": ["Python", "TensorFlow", "Scikit-Learn", "Deep Learning"]
    },
    {
        "remote": False,
        "job_title": "Network Administrator",
        "job_skills": ["Networking", "Linux", "Firewall", "Cisco"]
    },
    {
        "remote": True,
        "job_title": "Frontend Developer",
        "job_skills": ["JavaScript", "React", "CSS", "HTML"]
    },
    {
        "remote": False,
        "job_title": "Cybersecurity Analyst",
        "job_skills": ["Cybersecurity", "Penetration Testing", "SIEM", "Ethical Hacking"]
    },
    {
        "remote": True,
        "job_title": "DevOps Engineer",
        "job_skills": ["AWS", "Kubernetes", "Jenkins", "Terraform"]
    },
    {
        "remote": False,
        "job_title": "Product Manager",
        "job_skills": ["Project Management", "Agile", "Scrum", "Business Analysis"]
    }
]

# Hiển thị danh sách công việc
for job in job_data:
    print(f"Job Title: {job['job_title']}, Remote: {job['remote']}, Skills: {', '.join(job['job_skills'])}")