from django.urls import path
from . import views

urlpatterns = [

    path('ProductCreation', views.ProductCreation.as_view(), name='ProductCreation'),
    path('AllProductView', views.AllProductView.as_view(), name='AllProductView'),
    path('AllProductView1', views.AllProductView1.as_view(), name='AllProductView1'),
    path('ProductViewALL', views.ProductViewALL.as_view(), name='ProductViewALL'),
    path('ProductList', views.ProductList.as_view(), name='ProductList'),
    path('ProductDetail/<int:pk>', views.ProductDetail.as_view(), name='ProductDetail'),


]