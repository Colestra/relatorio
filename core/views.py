import io
from django.http import FileResponse
from  django.views.generic import  View

from reportlab.pdfgen import canvas


from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

class IndexView(View):
    def get(self, request, *args, **kwargs):

        buffer = io.BytesIO()


        pdf = canvas.Canvas(buffer)


        pdf.drawString(100, 100, "Curso Django")


        pdf.showPage()
        pdf.save()


        buffer.seek(0)




        return FileResponse(buffer, filename='relatorio1.pdf')



class Index2View(View):
    def get(self, request, *args, **kwargs):
        texto = ['Curso Django', 'Fazendo print com WeasyPrint', 'Programação Web com Python-Django']

        html_string = render_to_string('relatorio.html', {'texto': texto})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/relatorio2.pdf')

        fs = FileSystemStorage('/tmp')


        with fs.open('relatorio2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio2.pdf"'
        return response
