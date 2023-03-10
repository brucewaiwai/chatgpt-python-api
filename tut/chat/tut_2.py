# Here is a simple example that uses the GPT-3 model to generate text:


import openai

# set up the API credentials
openai.api_key = "key"

model = "text-davinci-002"
messages = [{"role": "system", "content": "You are a helpful assistant"}]
# create a prompt


while True:
    message = input("User: ")
    # generate text with the GPT-3 model
    if message:
        messages.append({"role": "user", "content": message})

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    # print the generated text
    reply = chat.choices[0].message.content

    print(f'Bot: {reply}')
