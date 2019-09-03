from django.shortcuts import render
from testapp.models import Book
def available_book(request):
    book_library=Book.objects.all()
    return render(request,'testapp/index.html',{'library':book_library})
def rating(request):
    return render(request,'testapp/rating.html')    
# Create your views here.
