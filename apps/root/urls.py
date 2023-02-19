from django import urls

from . import views

urlpatterns = (
    urls.path('', views.IndexView.as_view()),
    urls.path('log', views.LogView.as_view()),
    urls.path('pdf', views.PDFView.as_view()),
    urls.path('__debug__/', urls.include('debug_toolbar.urls')),
)
