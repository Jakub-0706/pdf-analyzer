from pdf_reader import extract_text_from_pdf
from ai_analyzer import summarize_text

pdf_path = "sample_pdfs/sample_text.pdf"

text = extract_text_from_pdf(pdf_path)
print("------TEKST:------")
print(text[:300] + "...") # Print first 300 characters

summary = summarize_text(text)
print("\n------STRESZCZENIE:------")
print(summary)