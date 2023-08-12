import graphene
from graphene_django import DjangoObjectType
from .models import Post, PostUplaod, CommunityPost


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("related_to", "content", "created_at")


class PostQuery(graphene.ObjectType):
    all_posts = graphene.List(PostType)


schema = graphene.Schema(query=PostQuery)
