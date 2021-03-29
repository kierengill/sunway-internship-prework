from django.urls import path

from . import views


urlpatterns = [
    path('', views.loginPage, name='home'),
    path('products/', views.products, name='products'),
    path('create_product/', views.createProduct, name='create_product'),
    path('products_no_login/', views.product_no_login, name='products_no_login'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name="logout"),

]
