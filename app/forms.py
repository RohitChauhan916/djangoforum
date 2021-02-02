from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, discussion, suggestion, Comment

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class UserExtend(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('emp_code', )

class ProfilePhoto(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'

class EditProfile(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('emp_code','phone_number','dob','department','about','location','web_address','hire_date','gender','zone','aniversary','designation','reporting_to','profile_photo','cover_photo')

class discussionForm(forms.ModelForm):

    class Meta:
        model = discussion
        fields = ('description','photo',)

class SuggestionForm(forms.ModelForm):

    class Meta:
        model = suggestion
        fields = ('emp_code','subject','message',)
