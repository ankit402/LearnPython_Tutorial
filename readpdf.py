import pdfplumber

# Load the PDF
with pdfplumber.open("yourfile.pdf") as pdf:
    text_content = ""
    for page in pdf.pages:
        text_content += page.extract_text() + "\n"

# Print or save the extracted content
print("Extracted PDF Text:\n")
print(text_content)

# Optional: Save to .txt for further inspection
with open("CardAudit_OMPAY_output.txt", "w", encoding="utf-8") as f:
    f.write(text_content)
