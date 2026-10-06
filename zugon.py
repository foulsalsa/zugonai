from openai import OpenAI

while True:

    client = OpenAI(
        api_key="INSERT_API_KEY",
        base_url="https://openrouter.ai/api/v1"
    )

    user_input = input("U: ")

    resp = client.chat.completions.create(
        model="cognitivecomputations/dolphin-mistral-24b-venice-edition",
        messages=[{"role": "user", "content": user_input}]
    )

    print("Zugon: " + resp.choices[0].message.content)
