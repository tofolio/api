import graphene
from .models import Post
from .types import PostType


class CreatePost(graphene.Mutation):
    class Arguments:
        content = graphene.String()
        related_to = graphene.ID()

    post_model = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, content, related_to):
        post_model = Post(content=content, related_to=related_to)
        post_model.save()

        return CreatePost(post_model=post_model)


class UpdatePost(graphene.Mutation):
    class Arguments:
        content = graphene.String()
        related_to = graphene.ID()

    post_model = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, content, related_to):
        post_model = Post(content=content, related_to=related_to)
        post_model.save()

        return CreatePost(post_model=post_model)


class DeletePost(graphene.Mutation):
    class Arguments:
        post_id = graphene.ID()

    post_model = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, content, post_id):
        return


class PostMutation(graphene.ObjectType):
    CreatePost = CreatePost.Field()
    UpdatePost = UpdatePost.Field()
    DeletePost = DeletePost.Field()
