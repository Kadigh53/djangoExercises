from django.urls import path
from rest_framework.routers import SimpleRouter
# from .views import PostList, PostDetail, UserList, UserDetail
from .views import PostVieswSet, UserViewSet

router=SimpleRouter()

router.register('users',UserViewSet, basename='users')
router.register('',PostVieswSet, basename='posts')

# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
# ]
urlpatterns = router.urls
