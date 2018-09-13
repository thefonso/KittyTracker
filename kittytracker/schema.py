import graphene
from graphene_django import DjangoObjectType

import kittytracker.tracker.schema
from graphene_django.debug import DjangoDebug

from graphene_django.rest_framework.mutation import SerializerMutation
from kittytracker.tracker.api.serializers import MedicationSerializer, LitterSerializer, CatSerializer, CareLogSerializer
# from kittytracker.tracker.models import Cat


class catMutations(SerializerMutation):
    class Meta:
        serializer_class = CatSerializer


class Query(kittytracker.tracker.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    debug = graphene.Field(DjangoDebug, name='__debug')
    pass


schema = graphene.Schema(query=Query)
