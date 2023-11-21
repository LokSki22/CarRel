import json

from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    # if request.method == 'POST':
    #     if 'increment' in request.POST:
    #         item_id = request.POST.get('increment')
    #         item = items.get(id=item_id)
    #         item.amount += 1
    #         item.save()
    #         return HttpResponseRedirect(reverse('main:show_main'))
    #     elif 'decrement' in request.POST:
    #         item_id = request.POST.get('decrement')
    #         item = items.get(id=item_id)
    #         if item.amount == 1:
    #             item.amount -= 0
    #         else:
    #             item.amount -= 1
    #         item.save()
    #         return HttpResponseRedirect(reverse('main:show_main'))
    #     elif 'delete' in request.POST:
    #         item_id = request.POST.get('delete')
    #         item = items.get(id=item_id)
    #         item.delete()
    #         return HttpResponseRedirect(reverse('main:show_main'))
    total_items = items.count()
    context = {
        'name': request.user.username,
        'class': "PBP B",
        'items': items,
        'item_count': total_items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
 form = ItemForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     item = form.save(commit=False)
     item.user = request.user
     item.save()
     return HttpResponseRedirect(reverse('main:show_main'))

 context = {'form': form}
 return render(request, "create_item.html", context)



def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_item(request, id):
    # Get product berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def get_product_json(request):
    product_item = Item.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        categories = request.POST.get("categories")
        user = request.user

        new_product = Item(name=name, price=price, description=description, user=user, amount=amount, categories=categories)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponse(b"DELETED", status=201)

@csrf_exempt
def increment_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.amount += 1
    item.save()
    return HttpResponse(b"DELETED", status=201)

@csrf_exempt
def decrement_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.amount -= 1
    if item.amount<1:
        item.amount = 1
    item.save()
    return HttpResponse(b"DELETED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user=request.user,
            name=data["name"],
            amount=int(data["amount"]),
            price=int(data["price"]),
            description=data["description"],
            categories=data["categories"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

