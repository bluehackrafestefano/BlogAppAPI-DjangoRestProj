from rest_framework import serializers
from .models import (
    Blog,
    Comment
)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'commentor',
            'created',
            'content',
            'blog'
        )


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = (
        #     'id',
        #     'title',
        #     'created',
        #     'updated'
        #     'content',
        #     'image',
        #     'slug',
        #     'status',
        #     'category',
        #     'author',
        #     'view_count',
        #     'like_count',
        #     'comment_count',
        #     'comments',
        # )
        fields = '__all__'
