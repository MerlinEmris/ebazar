class ProfileForm(forms.ModelForm):

    biography = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    location = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your location here'
            }
        ),
        help_text='your location please!'
    )
    birth_date = forms.DateField(
        widget=forms.widgets.DateInput(format="%d/%m/%Y"),
        help_text='input date by day month year !'
    )
    # user = forms.ChoiceField(
    #     choices=[(o.id, str(o)) for o in User.objects.all()],
    #     # widget=forms.HiddenInput(),
    # )


    # def clean(self):
        # super(ProfileForm, self).full_clean()
        # cleaned_data = super(ProfileForm, self).clean()
        # biography = cleaned_data.get('biography')
        # location = cleaned_data.get('location')
        # birth_date = cleaned_data.get('birth_date')
        # if not biography and not location and not birth_date:
        #     raise forms.ValidationError('You have to write something!')

    class Meta:
        model = Profile
        # fields = ('biography', 'location', 'birth_date', )
        exclude = ()