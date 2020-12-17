from django.contrib import admin
from django import forms
from .models import Profile, Category, Location, Item, Item_Image, User

# Register your models here.
admin.site.register(Location)
# class ProfileAdminForm(forms.ModelForm):
#     bio = forms.CharField(widget=forms.Textarea,label='Özi hakda')
#     location = forms.ModelChoiceField(queryset=Location.objects.filter(), required=True, label='Ýerleşýän ýeri')
#     user = forms.ModelChoiceField(queryset=User.objects.all(), label='Ulanyjy')
#     birthday = forms.DateField(label='Doglan senesi')
#     timestamp = forms.DateField(label='Döredilen senesi')
#
#     class Meta:
#         model = Profile
#         exclude = ()


class ProfileAdmin(admin.ModelAdmin):


    list_display = ['user', 'location', 'birth_date', 'timestamp']

    fields = ['user', 'location', 'birth_date', 'img', 'bio', 'timestamp', 'updated']
    readonly_fields = ['user', 'timestamp', 'updated']

    # def list_favorite_items(self, obj):
    #     return "%s" % ','.join([fav_item.name for fav_item in obj.favorite_items.all()])
    #
    # list_favorite_items.short_description = "Profile favorite items"

    # def get_form(self, request, obj=None, **kwargs):
    #     kwargs['form'] = ProfileAdminForm
    #     return super(ProfileAdmin, self).get_form(request, obj, **kwargs)
    def get_queryset(self, request):
        qs = super(ProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.register(Profile, ProfileAdmin)


class Item_Image_Inline(admin.TabularInline):
    model = Item_Image
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'user', 'location', 'price']
    ordering = ['-price']
    list_editable = ['name', 'location', 'price']
    list_per_page = 15
    list_max_show_all = 50
    search_fields = ['name', 'price', 'description']
    list_filter = ['location', 'user', 'timestamp', 'price']
    fieldsets = [
        ['Item Info', {
            'fields': ['name', 'category', 'user_phone', 'location', 'price', 'description']
        }],
        ['Other', {
            'fields': ['user', 'timestamp', 'updated'],
            'classes': ['collapse', 'wide']
        }]
    ]
    readonly_fields = ['timestamp', 'updated', 'user']
    save_on_top = True
    # adds inline foreign object
    inlines = [
        Item_Image_Inline,
    ]

    def get_queryset(self, request):
        qs = super(ItemAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(Item, ItemAdmin)


class Item_ImageAdmin(admin.ModelAdmin):
    list_display = ['item', 'img', 'timestamp']
    fields = [('item', 'img'),('timestamp')]
    readonly_fields = ['timestamp']

    def get_queryset(self, request):
        qs = super(Item_ImageAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(item=Item.objects.filter(user=request.user))


admin.site.register(Item_Image, Item_ImageAdmin)


class ItemRelated(admin.TabularInline):
    model = Item
    readonly_fields = ['name', 'user', 'location', 'price', 'user_phone']
    exclude = ['description']
    can_delete = False


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_editable = ['name']
    inlines = [
        ItemRelated,
    ]


admin.site.register(Category, CategoryAdmin)

# class FavoriteItemAdmin(admin.ModelAdmin):
#     model = Favorite_item
#     list_display = ['user', 'item', 'timestamp']
#     readonly_fields = ['timestamp']
#
#
# admin.site.register(Favorite_item,FavoriteItemAdmin)
