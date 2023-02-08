from django import urls

from . import views

urlpatterns = (
    urls.path('', views.TestView.as_view),
)
