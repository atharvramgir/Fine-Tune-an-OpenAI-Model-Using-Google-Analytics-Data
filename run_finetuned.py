from openai import OpenAI
client = OpenAI()


completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:nyx::AR1d3Gbr",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": " Does the dataset show any interesting user behaviors?"}
  ]
)
print(completion.choices[0].message)