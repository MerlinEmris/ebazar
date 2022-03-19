# from traceback import TracebackException

from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from django.core import serializers
from django.http import JsonResponse
from django.views import View
# import os
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes
# from django.utils.encoding import force_text
# from django.utils.http import urlsafe_base64_encode
# from django.utils.http import urlsafe_base64_decode
# from django.template.loader import render_to_string
from django.http import HttpResponse
import django_filters.rest_framework
from django.shortcuts import render, redirect
from .forms import ProfilePhotoForm, PhotoForm, SignUpForm, ProfileForm, ItemForm, SearchForm
from .models import User, Profile, Item, Category, Item_Image, Favorite_item
from ebazar import settings
from .serializers import (  CategorySerializer,
                            ItemSerializer,
                            UserSerializer,
                            Item_ImageSerializer,)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
# import django_filters.rest_framework
from rest_framework.generics import (
DestroyAPIView,
ListAPIView,
UpdateAPIView,
RetrieveAPIView,
CreateAPIView
)
from rest_framework.views import APIView
import shutil
import os
import datetime
import json


# print console logs
log_prefix = '['+datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")+']'
log_end = '********'
log_date = datetime.datetime.now().strftime("%d-%m-%y_%H:%M")


# redirect to create user (url(r'^$'))
def index(request):
    if request.user:
        return redirect('home')
    else:
        return redirect('home')


# create user with min information
def create_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(log_prefix+'user '+form.cleaned_data['username']+'is created'+log_end)
            # user.is_active = False
            # user.refresh_from_db()
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            # user.profile.bio = form.cleaned_data.get('bio')
            # user.profile.location = form.cleaned_data.get('location')

            # current_site = get_current_site(request)
            # subject = 'Activate Your MySite Account'
            # message = render_to_string('account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # user.email_user(subject, message)
            # return redirect('account_activation_sent')

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print(log_prefix + 'user ' + username + 'is logged in' + log_end)
            return redirect('home')
        else:
            form = SignUpForm(request.POST)
            return render(request, 'registration/create_user.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/create_user.html', {'form': form})


@login_required
def edit_profile(request):
    exist = 0
    try:
        profile = request.user.profile
        exist = 1
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            print(log_prefix + ' user ' + request.user.username + ' profile is changed ' + log_end)
            return redirect('home')
        else:
            return render(request, 'emarket/profile.html', {'form': form})
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'emarket/profile.html', {'form': form,'exist':exist})


def profile_change_photo(request, prof_id):
    if request.method == 'POST':
        profile = Profile.objects.filter(user_id=prof_id)[0]
        form = ProfilePhotoForm(request.POST, request.FILES, instance=profile)
        profile.img.delete(False)
        if form.is_valid():

            form.save()
            return redirect('profile')
    else:
        form = ProfilePhotoForm()
        return render(request, 'emarket/profile_add_image.html', {'form':form,})
    print(log_prefix + 'user ' + prof_id + 'profile img is changed' + log_end)


def user(request, user_id):
    items = Item.objects.filter(user_id=user_id)
    pics = Item_Image.objects.all()
    if items:
        paginator = Paginator(items, 9)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
    return render(request, 'emarket/user.html', {'items': items, 'pics': pics, })


@login_required
def create_item(request):
    if request.method == 'POST':
        item = Item(user=request.user)
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            print(log_prefix+'item:'+form.cleaned_data['name']+' is created at '+log_date+log_end)
            return redirect('add_item_img', item.id)
        else:
            return render(request, 'emarket/item_create.html', {'form': form})
    else:
        form = ItemForm()
        return render(request, 'emarket/item_create.html', {'form': form})


@login_required
def edit_item(request, it_id):
    try:
        item = Item.objects.filter(id=it_id)[0]
    except Item.DoesNotExist:
        redirect('home')
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            print(log_prefix + ' item ' + it_id + ' is changed ' + log_end)
            return redirect('show_item',it_id)
        else:
            form = ItemForm(instance=item)
            return render(request, 'emarket/item_edit.html',{'form':form})
    else:
        form = ItemForm(instance=item)
        return render(request, 'emarket/item_edit.html',{'form':form})


def show_item(request, item_id):
    user = request.user
    exist = 1
    # if user and request.method == "GET":
    #     favs = Favorite_item.objects.filter(user=user)
    #
    #     for fav in favs:
    #         if fav.item_id == int(item_id):
    #             print(fav.item_id)
    #             exist = 1
    #         else:
    #             exist = 0
    item = Item.objects.filter(id=item_id)[0]
    item_images = Item_Image.objects.filter()
    return render(request, 'emarket/item_detail.html', {'item': item,
                                                        'pics': item_images,
                                                        'exist': exist})


@login_required
def favorite_items(request, user_id):
    user = User.objects.filter(id=user_id)
    fav_items = Favorite_item.objects.filter(user = user)
    item_images = Item_Image.objects.filter()
    return render(request, 'emarket/favorite_items.html', {'fav_items': fav_items,
                                                           'pics': item_images})


# @login_required
# def add_to_fav(request):
#     return redirect('home')


def show_category(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    items = Item.objects.filter(category=cat)
    pics = Item_Image.objects.all()
    if items:
        paginator = Paginator(items, 9)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
    return render(request, 'emarket/show_category.html', {'cat':cat, 'items':items, 'pics':pics})


def home(request):
    cats = Category.objects.all()
    # item_pic = {}
    items = Item.objects.order_by('-price')[0:9]
    item_images = Item_Image.objects.filter()
    # print(item_images)
    # print(items)
    # print(categories)
    return render(request, 'emarket/home.html', {'cats': cats, 'items': items, 'pics': item_images, })


def search(request, search_word=None):
    message = 'Ähli goşlar:'
    pics = Item_Image.objects.all()
    items = Item.objects.all()
    form = SearchForm
    if request.method == 'POST':
        form = SearchForm(request.POST)
        search_word = request.POST.get('search')
        location = request.POST.get('location')
        user = request.POST.get('user')
        if location and user:
            items = Item.objects.filter(name__icontains=search_word).filter(user=user).filter(location=location)
        elif user:
            items = Item.objects.filter(name__icontains=search_word).filter(user=user)
        elif location:
            items = Item.objects.filter(name__icontains=search_word).filter(location=location)
        else:
            items = Item.objects.filter(name__icontains=search_word)
        if items:
            message = 'Netijeler:'
        else:
            message = 'Hiç zat ýok'
            items = None
    if items:
        paginator = Paginator(items, 18)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

    return render(request, 'emarket/expo.html', {'items': items, 'pics': pics, 'ms': message, 's_word': search_word, 'form':form})


@login_required
def add_item_img(request, it_id):
    photos = Item_Image.objects.filter()
    if request.method == 'POST':
        item_img = Item_Image(item_id=it_id)
        form = PhotoForm(request.POST, request.FILES, instance=item_img)
        if form.is_valid():
            form.save()
            print(log_prefix+'item_'+it_id+' added image'+str(form.cleaned_data['img'])+log_end)
            return redirect('show_item', it_id)
        else:
            return render(request, 'emarket/item_add_image.html', {'form': form, 'photos': photos})
    else:
        form = PhotoForm()
        return render(request, 'emarket/item_add_image.html', {'form':form, 'photos': photos})


@login_required
def delete_item(request, it_id):
    item = Item.objects.filter(id=it_id)

    if item:
        item.delete()
        items_path = os.path.join(settings.MEDIA_ROOT, 'items')
        item_id = 'item_'+str(it_id)
        item_path = os.path.join(items_path, item_id)
        shutil.rmtree(item_path)
        print(log_prefix+item_id+' is deleted'+log_end)
        return redirect('home')
    else:
        return redirect('home')


class UserCreate(APIView):
    def post(selfs, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                print(user)
                username = serializer.data.get('username')
                print(username)
                raw_password = serializer.data.get('password')
                print(raw_password)
                user_log = authenticate(username=username, password=raw_password)
                login(request, user_log)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print('user create error')
        else:
            print('user validation failed')


# api for item
class ItemViewSet(ListAPIView):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    search_fields = ('name',)
    ordering_fields = '__all__'


class Item_ImageViewSet(ListAPIView):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    queryset = Item_Image.objects.all()
    serializer_class = Item_ImageSerializer


class Item_ImageDetailViewSet(ListAPIView):
    queryset = Item_Image.objects.all()
    serializer_class = Item_ImageSerializer

    def get_queryset(self):
        item = self.kwargs['item']
        return Item_Image.objects.filter(item=item)


class ItemCreateViewSet(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailViewSet(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemUpdateViewSet(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDeleteViewSet(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# api for category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





