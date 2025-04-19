import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an expert executive assistant and academic planner."},
        {"role": "user", "content": "Is this document syllabus-related?"},
    ],
    temperature=0.2,
)
print(response.choices[0].message.content)
