from django.shortcuts import render, get_object_or_404, redirect
from first.models import InfectedPlace

from first.forms import InfectedPlaceForm, UpdateInfectedPlaceForm
from django.http import HttpResponseRedirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InfectedPlaceSerializer

from django.core.paginator import Paginator

# Create your views here.


def index(request):
    context = {
        
    }
    return render(request, 'first/index.html', context)


def list(request):
    theinfectedplace = InfectedPlace.objects.all()
    paginator = Paginator(theinfectedplace, 5)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    context = {
        'infectedplace': items
    
    }
    return render(request, 'first/list.html', context)

# def list(request):
#     context = {
#         'infectedplace': InfectedPlace.objects.all()
#     }
#     return render(request, 'first/list.html', context)


def create(request):
    if request.method == 'POST':
        form = InfectedPlaceForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/first/list/')
    form = InfectedPlaceForm()
    return render(request, 'first/create.html', {'form': form})


def update(request, id):
    if request.method == 'POST':
        item = get_object_or_404(InfectedPlace, pk=id)
        password = request.POST.get("password", "")
        form = UpdateInfectedPlaceForm(request.POST, instance = item)
        if form.is_valid() and password == 'dsc52dk':
            item = form.save()
    elif request.method == 'GET':
        item = get_object_or_404(InfectedPlace, pk=id)
        form = InfectedPlaceForm(instance=item)
        return render(request, 'first/update.html', {'form': form, 'item': item})
    return HttpResponseRedirect('/first/list/')

# def update(request):
#     if request.method == 'POST' and 'id' in request.POST:
#         item = InfectedPlace.objects.get(pk=request.POST.get('id'))
#         form = InfectedPlaceForm(request.POST, instance=item)
#         if form.is_valid():
#             item = form.save()
#     elif 'id' in request.GET:
#         item = InfectedPlace.objects.get(pk=request.GET.get('id'))
#         form = InfectedPlaceForm(instance=item)
#         return render(request, 'first/update.html', {'form':form})
#     return HttpResponseRedirect('/first/list/')


def detail(request, id):  # restaurant의 id (pk)를 직접 url path parameter을 통해 전달 받습니다.
    if id is not None:
        item = get_object_or_404(InfectedPlace, pk=id)
        return render(request, 'first/detail.html', {'item': item})
    return HttpResponseRedirect('/third/list/')


# def detail(request):
#     if 'id' in request.GET:
#         item = get_object_or_404(InfectedPlace, pk=request.GET.get('id'))
#         return render(request, 'first/detail.html', {'item': item})
#     return HttpResponseRedirect('/first/list/')


def delete(request, id): 
	item = get_object_or_404(InfectedPlace, pk=id)
	if request.method == 'POST' and 'password' in request.POST:
		if 'dsc52dk' == request.POST.get('password'):
			item.delete()
			return redirect('list')  # 리스트 화면으로 이동합니다. # HttpResponseRedirect와 무슨 차이지
		return redirect('infectedplace-detail', id=id) # 비밀번호가 입력되지 않으면 상세페이지로 되돌아감.
	return render(request, 'first/delete.html', {'item': item})


# def delete(request):
#     if 'id' in request.GET:
#         item = get_object_or_404(InfectedPlace, pk=request.GET.get('id'))
#         item.delete()
#     return HttpResponseRedirect('/first/list/')
        


@api_view(['GET'])
def ipserializer(request):
    totalIP = InfectedPlace.objects.all()
    serializer = InfectedPlaceSerializer(totalIP, many=True)
    return Response(serializer.data)