from django.shortcuts import render
from first.models import InfectedPlace

from first.forms import InfectedPlaceForm
from django.http import HttpResponseRedirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InfectedPlaceSerializer

# Create your views here.


def index(request):
    context = {
        
    }
    return render(request, 'first/index.html', context)


def list(request):
    context = {
        'infectedplace': InfectedPlace.objects.all()
    }
    return render(request, 'first/list.html', context)


def create(request):
    if request.method == 'POST':
        form = InfectedPlaceForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/first/list/')
    form = InfectedPlaceForm()
    return render(request, 'first/create.html', {'form': form})


@api_view(['GET'])
def ipserializer(request):
    totalIP = InfectedPlace.objects.all()
    serializer = InfectedPlaceSerializer(totalIP, many=True)
    return Response(serializer.data)