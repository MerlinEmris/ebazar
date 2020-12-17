from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PIL import Image

from .models import Profile, Location, Item, Category, Item_Image


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Şu ýere ulanyjynyň adyny giriziň!'
            }
        ),
        label='Lakam'
    )
    first_name = forms.CharField(max_length=30,
                                 required=False,
                                 help_text='Hökmany däl!',
                                 label='Ady')
    last_name = forms.CharField(max_length=30,
                                required=False,
                                help_text='Hökmany däl!',
                                label='Familiýasy')
    email = forms.EmailField(max_length=254,
                             help_text='Hökmany!',
                             widget=forms.EmailInput(
                                 attrs={
                                     'placeholder': 'Email salgyňyzy giriziň!'
                                 }
                             ))
    # Profile.birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    # Profile.bio = forms.Textarea()
    # Profile.location = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',  'email', 'password1', 'password2',)
# 'birth_date', 'bio', 'location',


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea,label='Özi hakda')
    location = forms.ModelChoiceField(queryset=Location.objects.filter(), required=True, label='Ýerleşýän ýeri')
    years = []
    for year in range(1920,2010):
        years.append(str(year))
    empty_label = ("Choose Year", "Choose Month", "Choose Day")
    birth_date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=empty_label,
        years=years),
        required=False,
        label='Doglan Senesi'
    )
    # user = forms.IntegerField(widget=forms.HiddenInput)
    # img = forms.ImageField(required=False)

    class Meta:
        model = Profile
        exclude = ('user', 'favorite_items', 'img', )


class ItemForm(forms.ModelForm):
    name = forms.CharField(label='Ady')
    category = forms.ModelChoiceField(queryset=Category.objects.filter(), label='Görnüşi')
    user_phone = forms.CharField(label='Ulanyjynyň telefon belgisi')
    description = forms.CharField(widget=forms.Textarea, label='Düşündirilişi')
    location = forms.ModelChoiceField(queryset=Location.objects.filter(), label='Ýerleşýän ýeri')
    price = forms.IntegerField(label='Bahasy')

    class Meta:
        model = Item
        exclude = ('user',)


class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Item_Image
        fields = ('img', 'x', 'y', 'width', 'height',)

    def save(self):
        photo = super(PhotoForm,self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.img)
        cropped_image = image.crop((x,y,w+x,h+y))
        resized_image = cropped_image.resize((900,1200), Image.ANTIALIAS)
        resized_image.save(photo.img.path)

        return photo


class ProfilePhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Profile
        fields = ('img', 'x', 'y', 'width', 'height',)

    def save(self):
        photo = super(ProfilePhotoForm,self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.img)
        cropped_image = image.crop((x,y,w+x,h+y))
        resized_image = cropped_image.resize((900,1200), Image.ANTIALIAS)
        resized_image.save(photo.img.path)

        return photo

class SearchForm(forms.Form):
    search = forms.CharField(label='Gözle',
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder': 'Gözleg üçin söz giriz!',
                                     'class': 'form-control'
                                 }
                                ),
                             required=False
                             )
    location = forms.ModelChoiceField(queryset=Location.objects.all(),
                                      label='Ýerleşýän ýeri',
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      required=False)
    user = forms.ModelChoiceField(queryset=User.objects.all(),
                                  label='Ulanyjy',
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  required=False)
