from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.serializers import PostModelSerializer


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer