from pathlib import Path
from docxtpl import DocxTemplate

BASE_DIR = Path(__file__).resolve().parent

TEMPLATE_PATH = BASE_DIR / "templates" / "заявление_сктс_шаблон.docx"

doc = DocxTemplate(TEMPLATE_PATH)

context = {
    'наименование_подразделения': "",
    'ФИО_заявителя': "",
    'Изменения': "",
    
    'ФИО_представителя_собственника': "",
    'Паспорт': "",
    'Адрес': "",
    'инициалы_и_фамилия': ""
}

doc.render(context)

DESKTOP_PATH = Path.home() / "Desktop"

output_file_path = DESKTOP_PATH / "сктс.docx"
doc.save(output_file_path)

print(f"Файл успешно сохранен на рабочий стол: {output_file_path}")