# -*- coding: utf-8 -*-
from .models import Person
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

def generate_pdf(request):
# Данные модели
people = Person.objects.all().order_by('last_name')

# Обработка шаблона
html_string = render_to_string('bedjango/pdf.html', {'people': people})
html = HTML(string=html_string)
result = html.write_pdf()

# Создание http ответа
response = HttpResponse(content_type='application/pdf;')
response['Content-Disposition'] = 'inline; filename=list_people.pdf'
response['Content-Transfer-Encoding'] = 'binary'
with tempfile.NamedTemporaryFile(delete=True) as output:
output.write(result)
output.flush()
output = open(output.name, 'r')
response.write(output.read())

return response