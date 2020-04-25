from cStringIO import StringIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def hello_pdf(request):
    # Создаём объект HttpResponse с соответствующим PDF заголовком.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    temp = StringIO()

    # Создаём объект PDF, используя объект StringIO как файл.
    p = canvas.Canvas(temp)

    # Выводим в PDF необходимую информацию. Здесь генерируется содержимое PDF.
    # Обратитесь к документации на ReportLab для подробностей.
    p.drawString(100, 100, "Hello world.")

    # Явно закрываем объект PDF.
    p.showPage()
    p.save()

    # Получаем данные из буфера StringIO и пишем отклик.
    response.write(temp.getvalue())
    return response