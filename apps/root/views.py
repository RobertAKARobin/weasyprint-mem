import collections
import datetime
import os
import psutil

from django import http
import django.views.generic as views
from django.template import loader

import weasyprint

log_max = 50
log = collections.deque([], log_max)
data_unit = 'mb'

pid = os.getpid()
mem = psutil.Process(pid).memory_full_info()
fields = [field for field in mem._fields]

words = 'all work and no play makes jack a dull boy'.split(' ')
words = words + words + words
cols = [*range(11)]
rows = [*range(10)]
table = []
for rownum in rows:
    row = []
    table.append(row)
    for colnum in cols:
        row.append(words[colnum + rownum])

class IndexView(views.TemplateView):
    template_name = 'index.djt'

    def dispatch(self, request, *args, **kwargs):
        pid = os.getpid()
        mem = psutil.Process(pid).memory_full_info()
        now = datetime.datetime.now()

        output = self._output_type(request)
        kwargs.update({
            'data_unit': data_unit,
            'fields': fields,
            'log': log,
            'log_max': log_max,
            'output': output,
        })

        entry = {
            'time': now,
            'output': output,
        }
        for field in fields:
            entry[field] = round(getattr(mem, field) / 1000000)
        log.appendleft(entry)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if kwargs['output'] == 'pdf':
            response = http.HttpResponse(self._to_pdf())
            response['Content-Type'] = 'application/pdf'
            return response
        return super().get(request, *args, **kwargs)

    def _output_type(self, request):
        output = request.GET.get('output', '').lower()
        if output == 'pdf':
            return 'pdf'
        return 'html'

    def _to_pdf(self):
        template = loader.get_template('pdf.djt')
        html = template.render({
            'table': table,
        })
        font_config = weasyprint.text.fonts.FontConfiguration()
        return weasyprint.HTML(
            string=html,
            encoding='utf-8'
        ).write_pdf(
            font_config=font_config,
        )
