from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]

# @permission_required('catalog.can_mark_returned')
# def renew_book_librarian(request, pk):
#     book_instance = get_object_or_404(BookInstance, pk=pk)

#     #If this is a post request then process the form data
#     if request.method == 'Post':

#         #Create a form instance and Populate it with data from request (binding):
#         form = RenewBookForm(request.POST)

#         # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#             book_instance.due_back = form.cleaned_data['renewal_date']
#             book_instance.save()


#             # Redirect it to a new url:
#             return HttpResponseRedirect(reverse('all-borrowed'))

#     #If this is a get request (Or any other method) Create the default form.
#     else:
#         proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#         form = RenewBookForm(initial={'renewal_date' : proposed_renewal_date})


#     context = {
#         'form' : form,
#         'book_instance' : book_instance,
#     }


#     return render(request, 'catalog/book_renew_librarian.html', context)