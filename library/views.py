from .forms import BookForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Book
from django.db.models import Q
from django.http import Http404

def book_detail(request, pk):

    # book = get_object_or_404(Book, pk=pk)
    # book = Book.objects.get(pk=pk) 
    try:
        book = Book.objects.get(pk=pk) 
    except Book.DoesNotExist:
        raise Http404

    return render(request, 'library/book.html', {
                "book": book,
                }) 
    


def books_list(request):
    search = request.GET.get("search")

    if search is None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(
            Q(title__contains=search) |
            Q(author__contains=search)
        )

    return render(request, "library/books.html", {
        "books": books, "search": search,
    })
    

def book_create(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, "library/book_create.html", {
            "form": form,
        })
    else: 
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Book.objects.create(
                title = data["title"],
                author = data["author"],
                count = data["count"],
            ) 
            return redirect("books-list")
    return render(request, "library/book_create.html", {
        "form": form,
    })




    