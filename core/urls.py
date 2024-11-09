from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('404/', views.Error404.as_view(), name='404'),
    path('blog-single/', views.BlogSingle.as_view(), name='blog-single'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('portfolio-details/', views.PortfolioDetails.as_view(), name='portfolio-details'),
]