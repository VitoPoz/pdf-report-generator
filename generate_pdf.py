from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Task
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))

engine = create_engine('sqlite:///tasks.db')
Session = sessionmaker(bind=engine)
session = Session()

tasks = session.query(Task).all()

doc = SimpleDocTemplate("report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

styles['Title'].fontName = 'Arial-Bold'
title = Paragraph(f"Отчёт по задачам на {date.today().strftime('%d.%m.%Y')}", styles['Title'])
story.append(title)
story.append(Spacer(1, 20))

table_data = [['Объект', 'Задача', 'Срок', 'Статус', 'Ответственный']]

for task in tasks:
    table_data.append([
        task.object_name,
        task.task_name,
        task.end_date.strftime('%d.%m.%Y'),
        task.status,
        task.responsible
    ])

table = Table(table_data, colWidths=[80, 100, 70, 80, 90])

table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0F766E')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F3F4F6')]),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
]))

story.append(table)

doc.build(story)
print(f"Отчёт сохранён в report.pdf, задач в отчёте: {len(tasks)}")