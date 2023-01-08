import openai  
#import os
openai.api_key = "ENTER YOUR! Privat API KEY"
#openai.api_key = os.getenv("OPEN_AI_KEY")
chatbot = openai.Completion()
while True:
    user_input = input("Please ask a question or press 0 to exit:")
    if user_input == "0":
        break
    response = chatbot.create(engine="text-davinci-003", prompt=user_input, max_tokens=2000)
    print(response.choices[0].text)
