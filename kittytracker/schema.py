import graphene

import kittytracker.tracker.schema
from graphene_django.debug import DjangoDebug


class Query(kittytracker.tracker.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    debug = graphene.Field(DjangoDebug, name='__debug')
    pass


schema = graphene.Schema(query=Query)
