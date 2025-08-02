from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  model="o4-mini",
  reasoning = {"effort": "low"},
  input=[
      {
          "role": "user",
          "content": "What is 3 body problem?"
      }
  ],
)

print(response.output_text)