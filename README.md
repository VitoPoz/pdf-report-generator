# PDF Report Generator

Скрипт для генерации PDF-отчёта с таблицей задач на основе данных из базы SQLite.

## Возможности

- Выгрузка данных из базы в оформленную таблицу PDF
- Корректная поддержка кириллицы (регистрация TTF-шрифта)
- Чередующаяся заливка строк для удобства чтения

## Стек

Python, ReportLab, SQLAlchemy

## Установка и запуск

```bash
git clone https://github.com/VitoPoz/pdf-report-generator.git
cd pdf-report-generator
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Понадобится файл базы данных `tasks.db` с таблицей `tasks` (структура — см. `models.py`).

Сгенерировать отчёт:
```bash
python generate_pdf.py
```

Результат — файл `report.pdf` в корне проекта.

## Планы по развитию

- Параметризация: выбор диапазона дат, фильтр по объекту/статусу
- Диаграммы/графики в отчёте вместо только таблицы
- Автоматическая отправка отчёта на email по расписанию