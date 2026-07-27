import json
from pdf_reader import extract_text_from_pdf
from ai_analyzer import summarize_text

pdf_path = "sample_pdfs/sample_text.pdf"

text = extract_text_from_pdf(pdf_path)
summary = summarize_text(text)

result = {
    "plik": pdf_path,
    "streszczenie": summary
}

with open("wynik.json", "w", encoding="utf-8") as f: # otwiera (a jeśli nie istnieje, tworzy) 
                        # plik wynik.json w trybie zapisu ("w" = write)
                        # encoding="utf-8" gwarantuje poprawną obsługę polskich znaków
    json.dump(result, f, ensure_ascii=False, indent=4) # zapisuje słownik result do otwartego pliku f
    # ensure_ascii=False — bez tego polskie znaki zapisałyby się jako kody typu \u0105
    # formatuje JSON z wcięciami

print("Gotowe! Wynik zapisano w pliku wynik.json.")