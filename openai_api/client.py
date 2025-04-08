import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

if not (api_key := os.getenv("GOOGLE_API_KEY")):
    raise ValueError("Chave de API não encontrada! Verifique seu arquivo .env")
genai.configure(api_key=api_key)



def get_car_ai_bio(model_name, brand, year):
    prompt = f"Escreva uma descrição com até 250 caracteres para um carro {brand} {model_name} {year}, destacando características específicas do modelo. seja direto e especifico e nao sujestões."
    model = genai.GenerativeModel(model_name="gemini-2.0-flash-thinking-exp-01-21")
    response = model.generate_content(prompt)
    
    return response.text.strip() if hasattr(response, "text") else "Erro: resposta vazia"
