import graphene
from .types import PostType
from .models import Post


class PostQuery(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    def resolve_all_posts(self):
        return Post.objects.all()
