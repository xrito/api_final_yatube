from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (GroupViewSet, UserViewSet,
                       PostViewSet, CommentViewSet, FollowViewSet)

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('users', UserViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
