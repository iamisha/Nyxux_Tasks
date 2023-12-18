from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.views import View


# Create your views here.
class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'media_app/home.html')
    
def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_form')
    else:
        form = ProductForm()

    return render(request, 'media_app/product_form.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'media_app/product_list.html', {'products': products})
