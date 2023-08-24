from graphene_django import DjangoObjectType
from .models import Post, PostUplaod, CommunityPost


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("related_to", "content", "created_at")
