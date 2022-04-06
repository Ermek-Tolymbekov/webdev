from django.urls import path
from api.views import product_list, get_product, category_list, get_category

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>/', get_product),
    path('categories/', category_list),
    path('categories/<int:id>/', get_category)
]