import openai
import os

def generate_app_code(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a senior software engineer who builds apps."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response['choices'][0]['message']['content']
