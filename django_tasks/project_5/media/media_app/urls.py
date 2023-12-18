from django.urls import path
from django.conf import settings
from .views import product_form, product_list
from django.conf.urls.static import static
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product-form/', product_form, name='product_form'),
    path('product-list/', product_list, name='product_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
