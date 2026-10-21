import io
from pathlib import Path

from docxtpl import DocxTemplate
from flask import Flask, render_template, send_file

from doc_creation.skts_form import SKTSForm

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret-key-for-csrf"
app.config["WORD_TEMPLATE_PATH"] = BASE_DIR / "заявление_сктс_шаблон.docx"


@app.route("/", methods=["GET", "POST"])
def index():
    form = SKTSForm()

    if form.validate_on_submit():
        doc = DocxTemplate(app.config["WORD_TEMPLATE_PATH"])

        context = {
            "наименование_подразделения": "",
            "ФИО_заявителя": "",
            "Изменения": "",
            "ФИО_представителя_собственника": "",
            "Паспорт": "",
            "Адрес": "",
            "инициалы_и_фамилия": "",
        }

        doc.render(context)

        file_stream = io.BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)

        return send_file(
            file_stream,
            as_attachment=True,
            download_name=f"Заявление_СКТС_{form.собственник_ТС_имя.data}.docx",
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

    return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
