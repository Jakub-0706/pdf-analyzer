# AI Analizator Dokumentów

Narzędzie automatycznie analizuje dokumenty PDF (umowy, raporty, pisma) i wyciąga z nich kluczowe informacje — streszczenie, daty, kwoty i strony umowy — w kilka sekund, bez konieczności ręcznego przeglądania wielostronicowych plików.

## Dla kogo?

Dla firm i osób, które regularnie pracują z dużą liczbą dokumentów PDF i chcą zaoszczędzić czas na ich ręcznej analizie (biura prawne, działy administracyjne, freelancerzy zarządzający umowami klientów).

## Jak to działa

1. Wskazujesz plik PDF
2. Program wyciąga z niego tekst
3. Tekst jest analizowany przez AI (Google Gemini)
4. Wynik (streszczenie + kluczowe dane) zapisywany jest do pliku JSON

## Technologie

- Python 3.11
- pdfplumber — ekstrakcja tekstu z PDF
- Google Gemini API — analiza treści przez AI
- python-dotenv — bezpieczne zarządzanie kluczem API
- Streamlit — interfejs webowy

## Jak uruchomić

1. Sklonuj repozytorium:
```bash
   git clone https://github.com/Jakub-0706/pdf-analyzer.git
   cd pdf-analyzer
```

2. Stwórz i aktywuj środowisko wirtualne:
```bash
   python -m venv venv
   source venv/Scripts/activate
```

3. Zainstaluj zależności:
```bash
   pip install -r requirements.txt
```

4. Stwórz plik `.env` i dodaj swój klucz API:
GEMINI_API_KEY=twój_klucz_tutaj

(klucz można uzyskać za darmo na [aistudio.google.com](https://aistudio.google.com))

### Wersja webowa (zalecana)

```bash
streamlit run app.py
```
Otworzy się przeglądarka, gdzie można wgrać plik PDF i od razu zobaczyć wynik analizy.

### Wersja terminalowa

Wrzuć plik PDF do folderu `sample_pdfs/`, wskaż jego ścieżkę w `main.py`, następnie:
```bash
python main.py
```
Wynik zapisany zostanie w pliku `wynik.json`.

## Planowane rozszerzenia

- Obsługa wielu plików naraz (całe foldery)
- Obsługa zeskanowanych dokumentów (OCR)
- Wdrożenie aplikacji online (obecnie działa tylko lokalnie)

## Status projektu

Projekt demonstracyjny / portfolio — pokazuje integrację przetwarzania dokumentów z API sztucznej inteligencji.