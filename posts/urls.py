from rest_framework.routers import SimpleRouter

from posts import views

router = SimpleRouter()
router.register('v1/users', views.UserViewSet, basename='users')
router.register('v1/post', views.PostViewSet, basename='post')

urlpatterns = router.urls

