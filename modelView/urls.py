from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',views.Product.as_view({'get':'list','post':'create'})),
    path('productUpdate/<int:pk>',views.Product.as_view({'put':'update'})),
    path('productDelete/<int:pk>',views.Product.as_view({'delete':'destroy'})),
    path('productPatch/<int:pk>',views.Product.as_view({'patch':'partialupdate'})),

    path('readProducts/',views.ProductRead.as_view({'get':'list'})),
    path('readProduct/<int:pk>',views.ProductRead.as_view({'get':'retrieve'})),
]
