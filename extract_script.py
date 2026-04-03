import fitz
import docx
import os

os.makedirs("tmp_texts", exist_ok=True)

try:
    doc = docx.Document("시뮬.docx")
    text = "\n".join([p.text for p in doc.paragraphs])
    with open("tmp_texts/simul_docx.txt", "w", encoding="utf-8") as f:
        f.write(text)
except Exception as e:
    print("Error reading docx:", e)

try:
    doc1 = fitz.open("제23회 한국 대학생 컴퓨터 시뮬레이션 경진대회 안내 및 규칙.pdf")
    text1 = ""
    for page in doc1:
        text1 += page.get_text() + "\n"
    with open("tmp_texts/rule_pdf.txt", "w", encoding="utf-8") as f:
        f.write(text1)
except Exception as e:
    print("Error reading rule pdf:", e)

try:
    doc2 = fitz.open("제23회 한국 대학생 컴퓨터 시뮬레이션 경진대회 예선 문제.pdf")
    text2 = ""
    for page in doc2:
        text2 += page.get_text() + "\n"
    with open("tmp_texts/problem_pdf.txt", "w", encoding="utf-8") as f:
        f.write(text2)
except Exception as e:
    print("Error reading problem pdf:", e)

print("Extraction complete.")
