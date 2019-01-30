# pages/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'