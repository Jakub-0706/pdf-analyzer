import os
import streamlit as st
from pdf_reader import extract_text_from_pdf
from ai_analyzer import summarize_text

st.title("Streszczenie plików PDF")
st.write("Wgraj plik PDF, a aplikacja automatycznie przygotuje streszczenie jego treści i wyciągnie kluczowe informacje.")

uploaded_file = st.file_uploader("Wybierz plik PDF", type="pdf")

if uploaded_file is not None:
    temp_path = "temp.pdf"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Analizuj dokument"):
        try:
            with st.spinner("Analizowanie dokumentu..."):
                text = extract_text_from_pdf(temp_path)
                summary = summarize_text(text)
            
            st.subheader("Streszczenie dokumentu:")
            st.write(summary)

        except FileNotFoundError:
            st.error("Plik nie został znaleziony.")
        
        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy dokumentu: {e}")

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)