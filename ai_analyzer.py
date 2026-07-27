import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def summarize_text(text):
    prompt = f"""Jesteś asystentem analizującym dokumenty biznesowe (umowy, raporty, pisma).

Przeanalizuj poniższy dokument i zwróć:
1. Krótkie streszczenie (maksymalnie 3-4 zdania)
2. Najważniejsze daty, jeśli występują
3. Kluczowe kwoty/liczby, jeśli występują
4. Główne strony/podmioty umowy, jeśli to umowa

Odpowiadaj wyłącznie po polsku, rzeczowo, bez zbędnych ozdobników.

Dokument do analizy:
{text}
"""
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )
    return response.text