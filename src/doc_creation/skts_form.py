from flask_wtf import FlaskForm
from wtforms import DateField, StringField
from wtforms.validators import DataRequired, Length


class SKTSForm(FlaskForm):
    собственник_ТС_имя = StringField(
        "Имя",
        validators=[
            DataRequired(message="Введите имя."),
            Length(min=2, max=100, message="Длина должна быть от 1 до 100 символов"),
        ],
    )

    собственник_ТС_фамилия = StringField(
        "Фамилия",
        validators=[
            DataRequired(message="Введите фамилию."),
            Length(min=2, max=100, message="Длина должна быть от 1 до 100 символов"),
        ],
    )

    собственник_ТС_отчество = StringField(
        "Отчество",
        validators=[
            DataRequired(message="Введите отчество."),
            Length(min=2, max=100, message="Длина должна быть от 1 до 100 символов"),
        ],
    )

    дата_рождения = DateField(
        "Дата рождения", validators=[DataRequired(message="Укажите дату рождения")]
    )

    паспорт_серия = StringField(
        "Паспорт (серия)",
        validators=[
            DataRequired(message="Укажите серию паспорта"),
            Length(
                min=4,
                max=4,
                message="Серия паспорта должен быть 4 символа",
            ),
        ],
    )

    паспорт_номер = StringField(
        "Паспорт (номер)",
        validators=[
            DataRequired(message="Укажите номер паспорта"),
            Length(
                min=6,
                max=6,
                message="Номер паспорта должен быть 6 символов",
            ),
        ],
    )

    инн = StringField(
        "ИНН",
        validators=[
            DataRequired(message="Укажите ИНН"),
            Length(min=10, max=12, message="ИНН должен быть 10 или 12 символов"),
        ],
    )

    адрес = StringField(
        "Адрес регистрации",
        validators=[
            DataRequired(message="Укажите адрес регистрации"),
            Length(
                min=10,
                max=300,
                message="Адрес должен быть от 10 до 300 символов и содержать город, улицу, дом",
            ),
        ],
    )
