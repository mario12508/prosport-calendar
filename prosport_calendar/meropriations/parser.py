import datetime
import ssl
from urllib.request import urlopen, Request
import PyPDF2
import re

import meropriations.models


def f():
    # Задаём URL PDF
    url = ('https://storage.minsport.gov.ru/cms-uploads/cms/'
           'II_chast_EKP_2024_14_11_24_65c6deea36.pdf')

    # Путь для сохранения PDF
    pdf_file_path = "../large_document.pdf"

    # Создание SSL контекста
    #context = ssl._create_unverified_context()
    #request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    # Загружаем PDF файл
    #with urlopen(request, context=context) as response:
    #    with open(pdf_file_path, "wb") as f:
    #        while chunk := response.read(1024 * 1024):
    #            f.write(chunk)

    # Извлекаем текст из PDF
    # with open(pdf_file_path, "rb") as f:
    #     reader = PyPDF2.PdfReader(f)
    #     text = ""
    #     for page_num, page in enumerate(reader.pages):
    #         page_text = page.extract_text()
    #         if page_text:
    #             text += page_text

    with open("duck.txt", encoding="utf-8") as f:
        text = f.read()

    text = re.sub(r'Стр\. \d+ из \d{4}', '', text)
    # Разбиение текста на строки
    lines = text.split("\n")

    meropriations.models.Tip.objects.all().delete()
    meropriations.models.Structure.objects.all().delete()
    meropriations.models.Group.objects.all().delete()
    meropriations.models.Meropriation.objects.all().delete()

    structure = meropriations.models.Structure.objects.create(
        name="Основной состав",
    )
    structure.save()
    structure = meropriations.models.Structure.objects.create(
        name="Молодежный (резервный) состав",
    )
    structure.save()

    group = meropriations.models.Group()
    meropriation = meropriations.models.Meropriation()
    meropriation_text = ""
    meropriation_place = ""

    date_pattern_start = r'(\d{2}\.\d{2}\.\d{4})(.*)'
    date_pattern_end = r'^(.*?)(\d{2}\.\d{2}\.\d{4})$'
    int_pattern = r'(.+?)(\d+)$'
    string_pattern = r'^[a-zA-Zа-яА-ЯёЁ\- ]+$'
    i_count = 15

    while i_count < len(lines):
        line = lines[i_count]
        if line == "Основной состав":
            structure = meropriations.models.Structure.objects.get(name="Основной состав")
        elif line == "Молодежный (резервный) состав":
            structure = meropriations.models.Structure.objects.get(name="Молодежный (резервный) состав")
        elif re.match(date_pattern_start, line):
            match = re.match(date_pattern_start, line)
            date = match.group(1)
            remaining_text = match.group(2)
            meropriation.date_end = datetime.datetime.strptime(date, '%d.%m.%Y').date()
            meropriation_place += remaining_text + "\n"
            meropriation.place = meropriation_place
            meropriation.save()
        elif re.match(date_pattern_end, line):
            match = re.match(date_pattern_end, line)
            remaining_text = match.group(1)
            date = match.group(2)
            meropriation.date_start = datetime.datetime.strptime(date, '%d.%m.%Y').date()
            meropriation_text += remaining_text + "\n"
            meropriation.text = meropriation_text
            meropriation.save()
        elif re.fullmatch(string_pattern, line) and line.isupper():
            group = meropriations.models.Group.objects.create(
                name=line,
            )
        elif line.isupper():
            list_line = line.split()
            tip_slug = list_line[0]
            tip_name = list_line[1]
            tip = meropriations.models.Tip.objects.filter(name=tip_name)
            if not tip:
                tip = meropriations.models.Tip.objects.create(
                    name=tip_name,
                )
            else:
                tip = tip.first()

            while lines[i_count + 1].isupper():
                i_count += 1
                meropriation.name += lines[i_count]

            meropriation = meropriations.models.Meropriation.objects.create(
                name=" ".join(list_line[1:]),
                tip=tip,
                group=group,
                slug=tip_slug,
                structure=structure
            )
            meropriation.save()
        elif line[-1].isdigit():
            match = re.match(int_pattern, line)
            text_part = match.group(1).strip()
            number_part = match.group(2)
            meropriation_text += text_part + "\n"
            meropriation.text = meropriation_text
            meropriation.count = int(number_part)
            meropriation.save()
        else:
            meropriation_text += line + "\n"
            meropriation.text = meropriation_text
            meropriation.save()
        i_count += 1
