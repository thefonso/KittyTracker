# cookbook/ingredients/schema.py
# import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Medication, Litter, Cat, CareLog, FosterAlert, VetVisit, User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['name']
        interfaces = (relay.Node,)


class MedicationNode(DjangoObjectType):
    class Meta:
        model = Medication
        filter_fields = ['name']
        interfaces = (relay.Node,)


class LitterNode(DjangoObjectType):
    class Meta:
        model = Litter
        filter_fields = ['name']
        interfaces = (relay.Node,)


class CatNode(DjangoObjectType):
    class Meta:
        model = Cat
        filter_fields = ['name']
        interfaces = (relay.Node,)


class CareLogNode(DjangoObjectType):
    class Meta:
        model = CareLog
        filter_fields = ['cat']
        interfaces = (relay.Node,)


class FosterAlertNode(DjangoObjectType):
    class Meta:
        model = FosterAlert
        filter_fields = ['cat']
        interfaces = (relay.Node,)


class VetVisitNode(DjangoObjectType):
    class Meta:
        model = VetVisit
        filter_fields = ['cat']
        interfaces = (relay.Node,)


class Query(object):
    users = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    medication = relay.Node.Field(MedicationNode)
    all_medications = DjangoFilterConnectionField(MedicationNode)

    litters = relay.Node.Field(LitterNode)
    all_litters = DjangoFilterConnectionField(LitterNode)

    cat = relay.Node.Field(CatNode)
    all_cats = DjangoFilterConnectionField(CatNode)

    carelog = relay.Node.Field(CareLogNode)
    all_carelogs = DjangoFilterConnectionField(CareLogNode)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_medications(self, info, **kwargs):
        return Medication.objects.all()

    def resolve_all_litters(self, info, **kwargs):
        return Litter.objects.all()

    def resolve_all_cats(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Cat.objects.select_related('litter').all()

    def resolve_all_carelogs(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return CareLog.objects.select_related('cat').all()

    def resolve_medication(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Medication.objects.get(pk=id)

        if name is not None:
            return Medication.objects.get(name=name)

        return None

    def resolve_cat(self, info, **kwargs):
        slug = kwargs.get('slug')
        name = kwargs.get('name')

        if slug is not None:
            return Cat.objects.get(slug=slug)

        if name is not None:
            return Cat.objects.get(name=name)

        return None

    def resolve_carelog(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Cat.objects.get(pk=id)

        if name is not None:
            return Cat.objects.get(name=name)

        return None
