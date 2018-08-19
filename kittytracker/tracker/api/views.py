from kittytracker.tracker.models import Medication, Litter, Cat, CareLog, FosterAlert, VetVisit
from rest_framework import viewsets
from .serializers import MedicationSerializer, LitterSerializer, CatSerializer, \
    CareLogSerializer, FosterAlertSerializer, VetVisitSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    filter_fields = ('cat__slug', 'cat__name')
    filter_backends = ('django_filters.rest_framework.DjangoFilterBackend',)


class LitterViewSet(viewsets.ModelViewSet):
    queryset = Litter.objects.all()
    serializer_class = LitterSerializer
    filter_backends = ('django_filters.rest_framework.DjangoFilterBackend',)


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    filter_fields = ('slug', 'name')
    filter_backends = ('django_filters.rest_framework.DjangoFilterBackend',)


class CareLogViewSet(viewsets.ModelViewSet):
    queryset = CareLog.objects.all()
    serializer_class = CareLogSerializer
    filter_fields = ('cat__slug', 'cat__name', 'food_type')
    filter_backends = ('django_filters.rest_framework.DjangoFilterBackend',)


class FosterAlertViewSet(viewsets.ModelViewSet):
    queryset = FosterAlert.objects.all()
    serializer_class = FosterAlertSerializer
    filter_fields = ('cat__slug', 'cat__name')
    filter_backends = ('django_filters.rest_framework.DjangoFilterBackend',)


class VetVisitViewSet(viewsets.ModelViewSet):
    queryset = VetVisit.objects.all()
    serializer_class = VetVisitSerializer
    filter_fields = ('cat__slug', 'cat__name',)
    filter_backends = ('django_filters.rest_framework.DjangoFilterBackend',)
