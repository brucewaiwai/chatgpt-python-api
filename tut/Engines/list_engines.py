import os
import openai

def setup_api_key(file):
    api_key = ''
    try:
        with open(file, "r") as file:
            api_key = file.read()
            print(f'api_key: {api_key}')

    except Exception as e:
        print(e)

    return api_key

openai.api_key = setup_api_key("api_key.txt")

print(openai.Engine.list())