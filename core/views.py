from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = "core/index.html"

class Error404(TemplateView):
    template_name = "core/404.html"

class Blog(TemplateView):
    template_name = "core/blog.html"
class BlogSingle(TemplateView):
    template_name = "core/blog-single.html"

class Contact(TemplateView):
    template_name = "core/contact.html"

class PortfolioDetails(TemplateView):
    template_name = "core/portfolio-details.html"
