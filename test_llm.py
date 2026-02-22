from resumes.services.llm_parser import parse_resume_with_llm

sample_text = """
John Doe
Email: john.doe@gmail.com

Skills:
Python, Django, SQL

Experience:
Software Engineer at ABC Corp (2021-2023)

Education:
BSc Computer Science
"""

result = parse_resume_with_llm(sample_text)
print(result)

