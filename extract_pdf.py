import pypdf

def extract_text(pdf_path, output_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Successfully wrote to {output_path}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    pdf_path = "projectphase1.pdf"
    output_path = "project_text.txt"
    extract_text(pdf_path, output_path)
