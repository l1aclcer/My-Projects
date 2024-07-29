from openai import OpenAI


# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key = "sk-proj-7oYusWcD7q7dQAJTJfnnT3BlbkFJ75vvxcIBBEtFEAtXhBCm",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in everything in general skills like Alexa and Google Cloud"},
    {"role": "user", "content": "W hat is programming"}
  ]
)

print(completion.choices[0].message)