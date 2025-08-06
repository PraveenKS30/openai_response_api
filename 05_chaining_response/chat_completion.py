from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4.1",
  messages=[
      {
          "role": "user",
          "content": "Write a one-sentence bedtime story about a unicorn."
      }
  ],
)

first_response = completion.choices[0].message.content
print(first_response)

# Now let's chain another request based on the first response
follow_up_completion = client.chat.completions.create( 
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": f" What did unicorn do after that?: {first_response}"
        }
    ],
    )

print(follow_up_completion.choices[0].message.content)
