from django.utils.html import format_html

def full_address(self):
    return format_html('%s - <b>%s,%s</b>' % (self.address, self.city, self.state))

# null derek yazylmaly hat
admin.site.empty_value_display = '???'


admin.site.register(Item)

# str funksivany ady bilen gorkezyar
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', '__str__']


# ozine gora hat chykarmat
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'upper_case_city_state']

    def upper_case_city_state(self, obj):

        return ("%s %s" % (obj.city, obj.state)).upper()
        upper_case_city_state.short_description = 'City/State'


# email domain ady gaytar
class Store(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    def email_domain(self):
        return self.email.split("@")[-1]
    email_domain.short_description = 'Email domain'
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name','email_domain']


# how to sort manually created field that related with db
# models.py
from django.db import models
from django.utils.html import format_html
class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30,unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    def full_address(self):
        return format_html('%s - <b>%s,%s</b>' % (self.address,self.city,self.state))
    full_address.admin_order_field = '-city'
# admin.py
from django.contrib import admin
from coffeehouse.stores.models import Store
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name','full_address']


# gerekli column link goyyar
list_display_links = ['name', 'user', 'location', 'price']


# filtr ulananda detail girip chykanda filtirsyz edip gorkezyar
preserve_filters = False


#doredilen wagtyna gora filtrlemek uchin
date_hierarchy = 'created'


# yokarda yerleshen action manu-ny ayyryar
actions_on_top = False


#show only this fields
fields = ['address','city','state','email']


# changing type of field
formfield_overrides = {
    models.CharField: {'widget': forms.Textarea}
}


# fills address field with sluged type of city and state field
prepopulated_fields = {'address': ['city','state']}


# create button that clone the record
save_as = True
save_as_continue = False #after cloning go to main page


# go to the page ayyryar
view_on_site = False


# if you want manually enter foreignkey ang manytomanyfield values
raw_id_fields = ["menu"]


#show foreignkeys and manytomanyfield like radio button
radio_fields = {"location": admin.HORIZONTAL}


# change admin form for user type
class MyModelAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            kwargs['form'] = MySuperuserForm
        return super(MyModelAdmin, self).get_form(request, obj, **kwargs)


#foreignkey values according to user
class MyModelAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "car":
            kwargs["queryset"] = Car.objects.filter(owner=request.user)
        return super(MyModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

# manytomanyfield values according to user
class MyModelAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "cars":
            kwargs["queryset"] = Car.objects.filter(owner=request.user)
        return super(MyModelAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

#calls this after admin delete
def response_delete(request, obj_display, obj_id):
    Determines the HttpResponse for the delete_view() stage.
    response_delete is called after the object has been deleted.
    You can override it to change the default behavior after the object has been deleted.
    obj_display is a string with the name of the deleted object.
    obj_id is the serialized identifier used to retrieve the object to be deleted.






# colored admin field
from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=6)

    def colored_first_name(self):
        return format_html(
            '<span style="color: #{};">{}</span>',
            self.color_code,
            self.first_name,
        )

    colored_first_name.admin_order_field = 'first_name'

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'colored_first_name')


#cvbsxfgbsfdgs


list_select_related = ('organization', 'user')





