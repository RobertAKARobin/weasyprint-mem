from django import http
import django.views.generic as views
from django.template import loader

import weasyprint

class IndexView(views.TemplateView):
    template_name = 'index.djt'

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
