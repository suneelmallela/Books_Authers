from django.shortcuts import render

from django.http import HttpResponse
from books.models import Book

#Contact form (forms)
from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.


def search_form(request):
    return render(request, 'search_form.html')

###Simple Seach box and show submit form with search string
'''
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' %request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
'''

### Search Hook with database
'''
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html', {'books':books, 'query':q})
    else:
        return HttpResponse('Please submit a search term')
''' 

### Display error in same search form
'''
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html', {'books':books, 'query':q})
    else:
        return render(request, 'search_form.html', {'error':True})
'''

### Elimate search_form() view
'''
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books':books, 'query':q})
    return render(request, 'search_form.html', {'error':error})
'''

### Simple Validation
'''
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error =True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books':books, 'query':q})
    return render(request, 'search_form.html', {'error':error})
'''

### List of error messages
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books':books, 'query':q})
    return render(request, 'search_form.html', {'errors':errors})

