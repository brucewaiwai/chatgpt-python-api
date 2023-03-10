
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

def read_preset(file):
    preset = ''
    try:
        with open(file, "r") as file:
            preset = file.read()
            # print(f'company_info: {company_info}')

    except Exception as e:
        print(e)

    return preset

def read_company_info(file):
    company_info = ''
    try:
        with open(file, "r") as file:
            company_info = file.read()
            # print(f'company_info: {company_info}')

    except Exception as e:
        print(e)

    return company_info

if __name__ == "__main__":
    api_key = setup_api_key("api_key.txt")
    company_info = read_company_info("customer_service/company/company_info.txt")
    preset = read_preset("customer_service/company/preset.txt")

    if api_key != '':
        # set up the API credentials
        openai.api_key = api_key

        messages = [{"role": "system", "content": f"{preset}, {company_info}"}]


        while True:
            message = input("User: ")
            # generate text with the GPT-3 model
            if message:
                messages.append({"role": "user", "content": message})

                chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=messages
                )

            # print the generated text
            reply = chat['choices'][0]['message']['content']

            print(f'Bot: {reply}')

    
