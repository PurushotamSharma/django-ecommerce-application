from django.shortcuts import render
from product.models import ProductItem
from django.http import HttpResponse


# Create your views here.
def product(request):

    product = ProductItem.objects.all()
    context = {
        'product': product
    }
    return render(request, 'product/product.html',context)


def category(request, val):

    product = ProductItem.objects.filter(CATAGORY_CHOICES=val)
    title = ProductItem.objects.filter(CATAGORY_CHOICES=val).values('P_name')
    context = {
        'val': val,
        'product': product,
        'title': title,
    }
    return render(request, 'product/category.html', context)

def productdetail(request, id):
    pro = ProductItem.objects.get(pk=id)
    context = {
        'pro': pro
    }

    return render(request, 'product/productdetail.html',context)

def test(request):
   return render(request, 'product/test.html')