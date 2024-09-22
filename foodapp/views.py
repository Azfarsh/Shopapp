from django.shortcuts import render
from .models import Product
from math import ceil
from .models import Contact
from django.shortcuts import HttpResponse
from django.contrib import messages
def food(request):
    products = Product.objects.all()
    n = len(products)
    chunk_size = 4  # Number of products per slide
    nSlides = ceil(n / chunk_size)  # Calculate number of slides

    params = {
        'no_of_slides': nSlides,
        'range': range(nSlides),
        'products': products,
    }
    return render(request, 'foodapp/index.html', params)

def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(product_name__icontains=query)
    else:
        products = Product.objects.all()
    
    return render(request, 'foodapp/index.html', {'products': products})

def track(request):
    return render(request, 'foodapp/index.html')

def about(request):
    return render(request, 'foodapp/about.html')



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_address = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save data to model
        contact = Contact(Name=name, Email_Address=email_address, Subject=subject, Message=message)
        contact.save()

        messages.success(request, 'Thank you for your message!')
    return render(request, 'foodapp/contact.html')


def product(request):
    return render(request, 'foodapp/product.html')

def checkout(request):
    return render(request, 'foodapp/index.html')
