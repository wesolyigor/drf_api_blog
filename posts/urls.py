from django.urls import path

from posts import views

urlpatterns = [
    path('v1/posts', views.PostList.as_view()),
    path('v1/posts/<int:pk>', views.PostDetail.as_view())
]
