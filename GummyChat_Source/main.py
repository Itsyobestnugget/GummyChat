#This is version 1 of it. use this to generate a SET quiestion. for input use code below the green markdown up here
#
#import os
#import google.generativeai as genai
#
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
#GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
#
#genai.configure(api_key=GOOGLE_API_KEY)
#
#for m in genai.list_models():
#  if 'generateContent' in #m.supported_generation_methods:
#    print(m.name)
#
#model = genai.GenerativeModel(model_name="gemini-pro")
#
#response = model.generate_content("How do I bake a cake?")
#
# Access the parts of the response
#parts = response.parts
#
# Print each part of the response
#for part in parts:
#  print(part.text)

import os
import google.generativeai as genai

print("Getting API Key...")
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
print("If you see an error then you need to set up your API key. You can do that by going to gemini ai studio dashboard and copying it. Then paste it into the code above.")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
model = genai.GenerativeModel(model_name="gemini-pro")
print("Please ignore! this is to check gemini versions!")
print(
    "----------------------------------------------------------------------------------------"
)
print(
    "                                Gemini User Prompt System                                "
)
print()
print("Hiya! This is a Google AI ChatBot that i made. it makes use of the console built in to python. You can ask it questions and it will answer them. If you want to ask it a question, just type and hit enter its set up in a user friendly way and if you want to edit it just replace the api key. it doesnt have security because it uses replit security whn running. you will have to make your own")
print(
    "----------------------------------------------------------------------------------------"
)
## Main loop to keep prompting the user
while True:
    #    # Get user input
    user_prompt = input("You: ")
    
    #    # Generate content based on user input
    response = model.generate_content(user_prompt)
    #    # Access the parts of the response
    parts = response.parts
    #
    #    # Print each part of the response
    for part in parts:
        print("----------------------------------------------------------------------------------------")
        print("Gemini:"), print(part.text)
        print("----------------------------------------------------------------------------------------")
        print()
#
#
#
#
#
#import os
#import google.generativeai as genai
#import json
#import subprocess
#
## Get the Replit environment URL
#replit_url = os.environ['REPL_SLUG']
#
## Your API key (replace this with your actual key)
#GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
#
#genai.configure(api_key=GOOGLE_API_KEY)
#
## ... (Code for listing and selecting the model, as before) ...
#
#model = genai.GenerativeModel(model_name="gemini-pro")
#
#def handle_request(request):
#    try:
#        data = json.loads(request.get_data())
#        question = data['question']
#
#        response = model.generate_content(question)
#        answer = ""
#        for part in response.parts:
#            answer += part.text + "\n"
#
#        return json.dumps({'answer': answer})
#    except Exception as e:
#        return json.dumps({'error': str(e)})
#
## In a real application, you'd likely use a web framework like Flask for routing
#if __name__ == '__main__':
#    # ... (Your code to interact with Gemini and generate responses) ...
#
#    # Example response:
#    response = "This is a sample response from Gemini."
#
#    # ... (Handle any other requests as needed) ...

#
#        __                               __
#   .--.\ \        .--.--.        .----.\ \
#__/ ./ \ \ \      /  /    '       /  ./--\ \ \
#|  \ \_/ / \ \    |  :  /`./       |  /    \ \ \
#|  |\___/   \ \ .  |  :  ;_       |  :  _ \ \ \
#|  :/  /---. / /, |  :    `.     |  : | \ \ \ \
#|  :  /    / | |:  \  \  ' .    |  : \  \ \ \ \
#|  :  \  \ /  |;   `----'   `--.|  :  \  `----'
#|  \   \  \  /:  \             /  \   \ \
# \   `----'   \   \         /   '----'  )
#  `--..____,--'    `------'     __..--''
#       ____ ____        ____   ____ ____ 
#     .'    `.  \ `.----' .'    `.  \  `.  \
#    /`--..  \  \  / /`--.' \    / \  \   \  \
#   |  |  \  |  |/  / ;   \  |  | |  |   '  |
#    \  \   \.   .'  /  \   \ \  \ |  \   /|
#     `----'  `--'   `----'  `--' `--'  `--'
