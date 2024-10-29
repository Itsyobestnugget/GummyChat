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

#import resources
import os
import google.generativeai as genai

print("Getting API Key...")
GOOGLE_API_KEY = os.getenv('AIzaSyC9Ci8D8JLstQyxGXqoGXXrqpldPwgcllQ')
genai.configure(api_key='AIzaSyC9Ci8D8JLstQyxGXqoGXXrqpldPwgcllQ')
print("If you see an error then you need to set up your API key. You can do that by going to gemini ai studio dashboard and copying it. Then paste it into the code above.")
#check for models and list
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
#set model
model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction="Your name is Gummy. Your good at code. but you talk casually. your instructions are to follow whatever the user sets it as and these inital instructions",)
print("Please ignore! this is to check gemini versions!")

#clear setup screen
print("Using model: " + model.model_name)
print("System instructions: " + model._system_instruction)
os.system("clear")
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

