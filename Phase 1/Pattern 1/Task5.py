'''Write a JobPosting model with these fields:

title — string, required
company — string, required
salary — float, required
is_remote — bool, defaults to False
tags — list of strings, defaults to empty list'''
from pydantic import BaseModel 
from typing import List , Optional
class JobPosting(BaseModel):
    title: str
    company: str
    salary: float
    its_remote: bool = False
    tags: List[str] = []

# Test 1 — valid posting
j = JobPosting(title="ML Engineer", company="Google", salary=200000.0, tags=["python", "ml"])
print(j)
print(j.model_dump())

# Test 2 — use model_validate
data = {"title": "AI Researcher", "company": "OpenAI", "salary": 250000.0, "is_remote": True}
j2 = JobPosting.model_validate(data) 
print(j2)
j2 = JobPosting(**data) #same as model_validate(data)
print(j2)

# Test 3 — intentionally pass wrong type 
try:
    j3 = JobPosting(title="Engineer", company="Meta", salary="not_a_number")
except Exception as e:
    print(e)
