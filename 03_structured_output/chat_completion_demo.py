from openai import OpenAI
from pydantic import BaseModel, Field

class Story(BaseModel):
    title: str = Field(description="Title of the story")
    characters : list[str] = Field(description="Characters in the story")
    story : str = Field(description="The story content")

client = OpenAI()

completion = client.chat.completions.parse(
  model="gpt-4.1",
  messages=[
      {
          "role": "user",
          "content": "Write a one-sentence bedtime story about a unicorn."
      }
  ],
  response_format=Story
)

print(completion.choices[0].message.content)