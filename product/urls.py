from django.urls import path
from . import views
from .views import ProductApi

urlpatterns = [
    
    #this path will be demonstrate for @api_view
    path('', views.product),
    
     #this path will demonstrate for APIView class 
    path('product-classbased/', ProductApi.as_view()),
 ]
