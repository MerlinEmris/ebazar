from django.conf.urls import url, include
from django.contrib import admin
from emarket import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'items/list', views.ItemDetailViewSet.as_view())
# router.register(r'items/detail', views.ItemDetailViewSet.as_view())
# router.register(r'items/update', views.ItemUpdateViewSet.as_view())
# router.register(r'items/delete', views.ItemDeleteViewSet.as_view())
# router.register(r'cats', views.CategoryViewSet)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/', views.edit_profile, name='profile'),
    url(r'^profile_chage_photo/(?P<prof_id>[\w\-]+)/$', views.profile_change_photo, name='profile_change_photo'),
    url(r'^create_item/$', views.create_item, name='create_item'),
    url(r'^item/(?P<item_id>[\w\-]+)/$', views.show_item, name='show_item'),
    # url(r'^favorites/(?P<user_id>[\w\-]+)/$', views.favorite_items, name='favorite_items'),
    url(r'^add_item_img/(?P<it_id>[\w\-]+)/$', views.add_item_img, name='add_item_img'),
    url(r'^user/(?P<user_id>[\w\-]+)/$', views.user, name='user'),
    url(r'^category/(?P<cat_id>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^search/', views.search, name='search'),
    url(r'^delete_item/(?P<it_id>[\w\-]+)/$', views.delete_item, name='delete_item'),
    url(r'^edit_item/(?P<it_id>[\w\-]+)/$', views.edit_item, name='edit_item'),
    # rest api
    url(r'^rest-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/register/', views.UserCreate.as_view(), name='account_create'),
    # url(r'^rest/', include(router.urls, namespace='rest')),
    url(r'^rest/items/$', views.ItemViewSet.as_view(), name='rest_item_all'),
    url(r'^rest/items_image/$', views.Item_ImageViewSet.as_view(), name='rest_item-image_all'),
    url(r'^rest/items_image/(?P<item>[\w-]+)/$', views.Item_ImageDetailViewSet.as_view(), name='rest_item-image'),
    url(r'^rest/items/create/$', views.ItemCreateViewSet.as_view(), name='rest_item_create'),
    url(r'^rest/items/(?P<pk>[\w-]+)/$', views.ItemDetailViewSet.as_view(), name='rest_item_detail'),
    url(r'^rest/items/(?P<pk>[\w-]+)/edit/$', views.ItemUpdateViewSet.as_view(), name='rest_item_update'),
    url(r'^rest/items/(?P<pk>[\w-]+)/delete/$', views.ItemDeleteViewSet.as_view(), name='rest_item_delete'),

]
