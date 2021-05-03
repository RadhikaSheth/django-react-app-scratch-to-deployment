from django.shortcuts import render
from .models import Spell
from .serializers import SpellSerializer
from rest_framework.generics import ListAPIView,CreateAPIView


# Create your views here.

class AddSpell(ListAPIView):
    queryset=Spell.objects.all()
    serializer_class = SpellSerializer

class GetSpell(CreateAPIView):
    queryset=Spell.objects.all()
    serializer_class = SpellSerializer