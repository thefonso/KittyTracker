from kittytracker.tracker.models import Medication, Litter, Cat, CareLog, FosterAlert, VetVisit
from kittytracker.users.models import User
from rest_framework import viewsets
from .serializers import MedicationSerializer, LitterSerializer, CatSerializer, \
    CareLogSerializer, FosterAlertSerializer, VetVisitSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('name',)


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    filter_fields = ('slug', 'name',)


class LitterViewSet(viewsets.ModelViewSet):
    queryset = Litter.objects.all()
    serializer_class = LitterSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    filter_fields = ('slug', 'name',)


class CareLogViewSet(viewsets.ModelViewSet):
    queryset = CareLog.objects.all()
    serializer_class = CareLogSerializer
    filter_fields = ('cat__slug', 'cat__name', 'food_type')


class FosterAlertViewSet(viewsets.ModelViewSet):
    queryset = FosterAlert.objects.all()
    serializer_class = FosterAlertSerializer
    filter_fields = ('cat__slug', 'cat__name')


class VetVisitViewSet(viewsets.ModelViewSet):
    queryset = VetVisit.objects.all()
    serializer_class = VetVisitSerializer
    filter_fields = ('cat__slug', 'cat__name',)
