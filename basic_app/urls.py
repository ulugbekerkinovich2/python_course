from django.urls import path

from basic_app import views

urlpatterns = [
    path('', views.BookCreateApiView.as_view(), name='index'),
    path('books/', views.BookListApi.as_view(), name='book-list'),
    # path('books/<int:pk>', views.DeleteApiView.as_view(), name='book-detail'),
    path('books/<int:pk>', views.BookDetailApiView.as_view()),
    path('books/<int:pk>/put', views.BookUpdateApiView.as_view(), name='book-update')
]
