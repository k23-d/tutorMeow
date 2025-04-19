import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def validate_pdf_with_ai(text: str) -> bool:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You're a strict academic assistant. Reply only with YES or NO. Do not elaborate. If the text is a syllabus for a university-level course, say YES. Otherwise, say NO."
            },
            {
                "role": "user",
                "content": f"Here is the text: {text}\n\nIs this a syllabus document?"
            }
        ],
        temperature=0
    )
    print("This is the response")
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

