from openai import OpenAI
from pydantic import BaseModel, Field

client = OpenAI()

class Story(BaseModel):
    title: str = Field(description="Title of the story")
    characters : list[str] = Field(description="Characters in the story")
    story : str = Field(description="The story content")

response = client.responses.parse(
  model="gpt-4.1",
  input=[
      {
          "role": "user",
          "content": "Write a one-sentence bedtime story about a unicorn."
      }
  ],
  text_format= Story
)

print(response.output[0].content[0].text)

