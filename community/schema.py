import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload
from .models import Communitys

class CommunitysType(DjangoObjectType):
    class Meta:
        model = Communitys
       

class Query(graphene.ObjectType):
    all_comunitys= graphene.List(CommunitysType)
    comunity = graphene.Field(CommunitysType , id=graphene.ID())

    def resolve_all_comunitys(self,info,**kwarg):
        return Communitys.objects.all()
    
    def resolve_comunity(self,info,id):
        return Communitys.objects.get(pk=id)


class CreateCommunity(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        image = Upload(required=False)
    
    community = graphene.Field(CommunitysType)

    def mutate(self, info, name, description, image=None):
        community = Communitys(name=name, description=description, image=image)
        community.save()
        return CreateCommunity(community=community)
    
class UpdateCommunity(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        description = graphene.String()
        image = Upload(required=False)

    community = graphene.Field(CommunitysType)

    def mutate(self, info, id, name=None, description=None, image=None):
        community = Communitys.objects.get(pk=id)
        if name:
            community.name = name
        if description:
            community.description = description
        if image:
            community.image = image
        community.save()
        return UpdateCommunity(community=community)


class DeleteCommunity(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    success = graphene.Boolean()

    def mutate(self, info, id):
        community = Communitys.objects.get(pk=id)
        community.delete()
        return DeleteCommunity(success=True)

class Mutation(graphene.ObjectType):
    create_community = CreateCommunity.Field()
    update_community = UpdateCommunity.Field()
    delete_community = DeleteCommunity.Field()

schema=graphene.Schema(query=Query, mutation=Mutation)