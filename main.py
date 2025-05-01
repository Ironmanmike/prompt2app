import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_app_code(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ✅ widely available model
        messages=[
            {"role": "system", "content": "You are a senior Python developer. Generate a complete app based on the user's request."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content

