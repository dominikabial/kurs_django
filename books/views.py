from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_http_methods

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
    form = CommentForm
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


# POST book/1/comment

@require_http_methods(["POST"])
def book_comment(request, pk):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        book = Book.objects.get(pk=pk)
        comment.book = book
        comment.save()
        return HttpResponseRedirect(reverse('book:details', args=(pk,)))
