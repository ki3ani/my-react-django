from django.urls import path
from django.views.generic import TemplateView

app_name = 'wishes'


urlpatterns = [
    path('', TemplateView.as_view(template_name='wishes/index.html'), name='index'),
    ]



