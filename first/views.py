from django.shortcuts import render, get_object_or_404
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


def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        item = InfectedPlace.objects.get(pk=request.POST.get('id'))
        form = InfectedPlaceForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
    elif 'id' in request.GET:
        item = InfectedPlace.objects.get(pk=request.GET.get('id'))
        form = InfectedPlaceForm(instance=item)
        return render(request, 'first/update.html', {'form':form})
    return HttpResponseRedirect('/first/list/')


def detail(request):
    if 'id' in request.GET:
        item = get_object_or_404(InfectedPlace, pk=request.GET.get('id'))
        return render(request, 'first/detail.html', {'item': item})
    return HttpResponseRedirect('/first/list/')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(InfectedPlace, pk=request.GET.get('id'))
        item.delete()
    return HttpResponseRedirect('/first/list/')
        


@api_view(['GET'])
def ipserializer(request):
    totalIP = InfectedPlace.objects.all()
    serializer = InfectedPlaceSerializer(totalIP, many=True)
    return Response(serializer.data)