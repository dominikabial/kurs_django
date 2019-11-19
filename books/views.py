from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import Book
from .form import CommentForm
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(books, 10)
    books = paginator.get_page(page)
    return render(
        request,
        template_name='books/list.html',
        context={'books': books}
    )


class ListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/list.html'
    paginate_by = 10
    def get_queryset(self):
        return Book.objects.all()


class DetailView(generic.DetailView, generic.FormView):
    template_name = 'books/detail.html'
    model = Book
    form_class = CommentForm


def book_details(request, book_id):
    form = CommentForm()
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Question does not exist")
    # template = loader.get_template('detail_123.html')
    context = {
        'book': book,
        'form': form
    }
    print(context)
    # return HttpResponse(template.render(context, request))
    return render(
        request,
        template_name='books/detail.html',
        context=context
    )