import pdfplumber

def extract_text_from_pdf(file_path: str) -> str:
    text_parts = []

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
    except FileNotFoundError:
        raise FileNotFoundError(f"Plik {file_path} nie został znaleziony.") 
        # program nadal się zatrzyma, ale komunikat będzie czytelny i konkretny, wskazujący dokładnie, o który plik chodzi

    full_text = "\n".join(text_parts)
    return full_text