from django.urls import path

from second_app import views

urlpatterns = [
    path('uni/', views.ListAPIView.as_view()),
    path('uni/<int:pk>', views.ListAPIView.as_view()),
]
