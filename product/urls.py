from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path("", views.product,name='product'),
    path("category/<slug:val>", views.category,name='category'),
    path("productdetail/<int:id>", views.productdetail,name='productdetail'),
    path("test/", views.test,name='test'),
    
]