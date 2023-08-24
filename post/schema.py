import graphene
from .types import PostType


class PostQuery(graphene.ObjectType):
    all_posts = graphene.List(PostType)


schema = graphene.Schema(query=PostQuery)
