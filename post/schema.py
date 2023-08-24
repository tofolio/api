from .queries import PostQuery
from .mutations import PostMutation
import graphene


schema = graphene.Schema(query=PostQuery, mutation=PostMutation)
