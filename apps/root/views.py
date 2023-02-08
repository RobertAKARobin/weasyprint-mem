from django import http
import django.views.generic as views
from django.template import loader

import weasyprint

class TestView(views.TemplateView):
    template_name = 'test.djt'

    def get(self, request, *args, **kwargs):
        if not request.GET.get('pdf'):
            return super.get(request, *args, **kwargs)

        response = http.HttpResponse(self.to_pdf())
        response['Content-Type'] = 'application/pdf'
        return response

    def to_pdf(self):
        template = loader.get_template(self.template_name)
        html = template.render()
        font_config = weasyprint.text.fonts.FontConfiguration()
        return weasyprint.HTML(
            string=html,
            encoding='utf-8'
        ).write_pdf(
            font_config=font_config,
        )
