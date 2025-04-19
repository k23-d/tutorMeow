import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def validate_pdf_with_ai(text: str) -> bool:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert executive assistant and academic planner."},
            {"role": "user", "content": "Is this document syllabus-related?"},
        ],
        temperature=0.2,
    )
    print(response.choices[0].message.content)
    result = response.choices[0].message.content.strip().lower()

    if result == "yes":
        return True
    elif result == "no":
        return False
    else:
        # Optional: Log this or raise an exception
        print(f"⚠️ Unexpected response from AI: {result}")
        return False  # fallback to safe

