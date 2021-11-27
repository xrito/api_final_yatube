from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from posts.models import Group, Post, User

from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer, UserSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        post_id = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        new_queryset = post_id.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post_id = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post_id)


class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    pass


class FollowViewSet(CreateRetrieveViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    def get_queryset(self):
        user_id = get_object_or_404(User, pk=self.request.user.pk)
        queryset = user_id.follower.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
