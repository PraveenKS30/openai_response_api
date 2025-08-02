from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  model="gpt-4.1",
  input=[
      {
          "role": "user",
          "content": "Write a one-sentence bedtime story about a unicorn."
      }
  ],
)

print(response.output[0].content[0].text)
print(response.output_text)