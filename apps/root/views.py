import os

from django import http
import django.views.generic as views
from django.template import loader

import weasyprint

logfile_name = 'log.txt'

try:
    os.remove(logfile_name)
except OSError: # If file doesn't exist
    pass
logfile = open(logfile_name, 'a')
logfile.close()

class IndexView(views.TemplateView):
    template_name = 'index.djt'

class LogView(views.View):
    def get(self, request, *args, **kwargs):
        with open(logfile_name, 'r') as logfile:
            log = logfile.read()
            return http.HttpResponse(log, content_type='text/plain')

    def post(self, request, *args, **kwargs):
        with open(logfile_name, 'a') as logfile:
            logfile.write(request.body)

class PDFView(views.View):
    def get(self, request, *args, **kwargs):
        response = http.HttpResponse(self.to_pdf())
        response['Content-Type'] = 'application/pdf'
        return response

    def to_pdf(self):
        template = loader.get_template('pdf.djt')
        html = template.render()
        font_config = weasyprint.text.fonts.FontConfiguration()
        return weasyprint.HTML(
            string=html,
            encoding='utf-8'
        ).write_pdf(
            font_config=font_config,
        )
