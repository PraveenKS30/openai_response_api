from openai import OpenAI

client = OpenAI()

completion = client.responses.create(
  model="gpt-4.1",
  input=[
      {
          "role": "user",
          "content": "Write a one-sentence bedtime story about a unicorn."
      }
  ],
)

first_response_id = completion.id
print(completion.output_text)



# Now let's chain another request based on the first response
follow_up_completion = client.responses.create( 
    model="gpt-4.1",
    previous_response_id= first_response_id,
    input=[
        {
            "role": "user",
            "content": f" What did unicorn do after that?"
        }
    ],
    )

print(follow_up_completion.output_text)
