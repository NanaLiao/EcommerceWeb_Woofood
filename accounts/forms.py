from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import UserProfile

class RegistrationForm(UserCreationForm): #inherit UserCreationForm
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(max_length=150,required=True)

    class Meta:    #Meta just like the property of the class, like picture has size
        model = User
        fields=(   #like the admin user fields
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
        )

    def save(self, commit=True): #commit = True means will add to database
        user = super(RegistrationForm,self).save(commit=False) #commit=False means don't save yet, haven't finish editting
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields=(   # you can aslo use exclude() instead of field, in our case here, we have more exclude then include, so we use field()
        'first_name',
        'last_name',
        'email',
        )
    def save(self, commit=True): #commit = True means will add to database
        user = super(UserChangeForm,self).save(commit=False) #commit=False means don't save yet, haven't finish editting
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user
