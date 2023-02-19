from django import urls

from . import views

urlpatterns = (
    urls.path('', views.IndexView.as_view()),
)
