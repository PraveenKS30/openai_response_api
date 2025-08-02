from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="o4-mini",
  reasoning_effort= "low",
  messages=[
      {
          "role": "user",
          "content": "What is 3 body problem?"
      }
  ],
)

print(completion.choices[0].message.content)