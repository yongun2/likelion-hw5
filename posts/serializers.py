from rest_framework import serializers, status
from rest_framework.response import Response
from posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class PostListModelSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        fields = [
            'id',
            'image',
            'created_at',
            'view_count',
            'writer'
        ]

class PostCreateModelSerializer(PostModelSerializer):
    class Meta(PostModelSerializer.Meta):
        fields = [
            'image',
            'content'
        ]

class PostDetailModelSerializer(PostModelSerializer):
    pass

class PostHypelinkModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'