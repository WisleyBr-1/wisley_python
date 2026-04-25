from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key= "AIzaSy...")

resposta = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents= input("Qual a sua dúvida? ")
)
print(resposta.text)
