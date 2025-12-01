
from django.views.generic import TemplateView

about = TemplateView.as_view(template_name='pages/about.html')
rules = TemplateView.as_view(template_name='pages/rules.html')
