# Here is a simple example that uses the GPT-3 model to generate text:


import openai
import json

# set up the API credentials
openai.api_key = "key"

# create a prompt
prompt = "Once upon a time,"

# generate text with the GPT-3 model
model = "text-davinci-002"
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.7,
)

# print the generated text
print(response.choices[0].text.strip())