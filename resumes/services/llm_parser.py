from dotenv import load_dotenv

load_dotenv()

import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List


class Project(BaseModel):
    name: str
    description: str
    url: str


class Experience(BaseModel):
    company: str
    role: str
    years: str


class ResumeData(BaseModel):
    name: str
    email: str
    skills: List[str]
    soft_skills: List[str]
    experience: List[Experience]
    projects: List[Project]
    education: List[str]
    languages: List[str]
    urls: List[str]


parser = PydanticOutputParser(pydantic_object=ResumeData)


def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=api_key,
    )


def parse_resume_with_llm(resume_text: str):
    llm = get_llm()

    prompt = PromptTemplate(
        template="""
Extract structured information from the resume below.

{format_instructions}

Resume:
{resume_text}
""",
        input_variables=["resume_text"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | llm | parser
    return chain.invoke({"resume_text": resume_text})
