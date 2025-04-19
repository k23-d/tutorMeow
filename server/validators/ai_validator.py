import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def validate_pdf_with_ai(text: str) -> bool:
    prompt = f"""
    A user uploaded this document. Determine if it's syllabus-related or academic material.

    Content:
    {text}

    Respond only with YES or NO.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    result = response.choices[0].message.content.strip().lower()
    return "yes" in result
