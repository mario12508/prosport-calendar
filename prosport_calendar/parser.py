import sqlite3
import ssl
from urllib.request import urlopen, Request
import PyPDF2

# Задаём URL PDF
url = ('https://storage.minsport.gov.ru/cms-uploads/cms/'
       'II_chast_EKP_2024_14_11_24_65c6deea36.pdf')

# Путь для сохранения PDF
pdf_file_path = "large_document.pdf"

# Создание SSL контекста
context = ssl._create_unverified_context()
request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# Загружаем PDF файл
with urlopen(request, context=context) as response:
    with open(pdf_file_path, "wb") as f:
        while chunk := response.read(1024 * 1024):
            f.write(chunk)

# Извлекаем текст из PDF
with open(pdf_file_path, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for page_num, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if page_text:
            text += page_text

# Разбиение текста на строки
lines = text.split("\n")
