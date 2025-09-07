from openai import OpenAI


client = OpenAI()


# getting response 
response = client.responses.create(
    model= "gpt-5-mini",
    input = "Write a poem about the sea in the style of Shakespeare",
    reasoning = {"effort": "low"},
    text = {"verbosity" : "low"}
   
)

print(response.output_text)
print(response.usage.total_tokens)
print(response.usage.input_tokens)
print(response.usage.output_tokens)
print(response.usage.output_tokens_details.reasoning_tokens)
