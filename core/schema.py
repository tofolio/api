from post.schema import PostQuery
import graphene

schema = graphene.Schema(query=PostQuery)
