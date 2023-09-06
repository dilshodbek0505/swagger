from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description","created_at"]
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['created_at'] = instance.created_at.strftime("%b %d %Y")
        return res

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "title", "text", "post", "created_at")
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['created_at'] = instance.created_at.strftime("%b %d %Y")
        res['post'] = instance.post.title
    
    