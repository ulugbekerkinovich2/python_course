from django.urls import path
from rest_framework.routers import SimpleRouter

from basic_app import views, views2
from basic_app.views import BookViewSet

router = SimpleRouter()
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    # path('post/', views2.Post.as_view(), name='index'),
    # path('get/', views2.List.as_view(), name='book-list'),
    # path('del/<int:pk>', views2.Del.as_view(), name='book-detail'),
    # path('put/<int:pk>', views2.Put.as_view()),
    # path('get/<int:pk>', views2.ListID.as_view())
]
urlpatterns = urlpatterns + router.urls
