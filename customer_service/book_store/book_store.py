
import openai

bookstore_info = {
    "name": "mumu is so cute",
    "street_address": "mumu house.",
    "city": "HK",
    "phone_number": "(852) 12345678",
    "email": "mumu@mybookstore.com"
}

def setup_api_key(file):
    api_key = ''
    try:
        with open(file, "r") as file:
            api_key = file.read()
            print(f'api_key: {api_key}')

    except Exception as e:
        print(e)

    return api_key

def read_bookstore_info(file):
    bookstore_info = ''
    try:
        with open(file, "r") as file:
            bookstore_info = file.read()
            print(f'bookstore_info: {bookstore_info}')

    except Exception as e:
        print(e)

    return bookstore_info

if __name__ == "__main__":
    api_key = setup_api_key("api_key.txt")
    bookstore_info = read_bookstore_info("customer_service/book_store/book_store_info.txt")

    if api_key != '':
        # set up the API credentials
        openai.api_key = api_key

        model = "text-davinci-002"
        messages = [{"role": "system", "content": f"You are a customer service of book store named Mumu is so Cute, infomation of the book store are {bookstore_info}"}]
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
            reply = chat['choices'][0]['message']['content']

            print(f'Bot: {reply}')

    
