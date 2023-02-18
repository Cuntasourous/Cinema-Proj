from django import forms
from django.forms import ModelForm
from cine_app.models import Movie_list, Genre, book3, timeslots
from django.contrib.auth.models import User
from cine_app.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

#create a booking form
class bookForm(forms.ModelForm):
#class bookForm(forms.Form):
    #movie_title2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'movie_title'}))
    movie_title = forms.CharField(widget=forms.HiddenInput())
    seats = forms.IntegerField()
    date = forms.DateField(localize=True,widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),)
    #time = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    time = forms.ModelChoiceField(timeslots.objects.all(), widget=forms.RadioSelect())
    #user = forms.ModelChoiceField(User.objects.all())
    class Meta:
        model = book3
        fields = ('movie_title','seats','date','time', 'user')

        widgets = {
           'movie_title': forms.TextInput(attrs={'id':'id_movie_title', 'value':'', 'type':'hidden'}),
           'user': forms.TextInput(attrs={'id':'id_user', 'value':'','type':'hidden'}),
        }
        #('movie_title','seats','date','time')

        #def __init__(self, *args, **kwargs):
        #    user = kwargs.pop('user')
        #    super(bookForm, self).__init__(*args, **kwargs)
        #    self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.filter(owner=None) | User.username.objects.filter(owner=user), required=False)

    #def __init__(self, *args, **kwargs):
    #    super(bookForm, self).__init__(*args, **kwargs)
    #    self.initial['movie_title'] = movie_instance

class MovieListForm(ModelForm):
    class Meta:
        model = Movie_list
        fields = '__all__'

class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.passwordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic', )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput()),
    first_name = forms.CharField(max_length=100, widget=forms.TextInput()),
    last_name = forms.CharField(max_length=100, widget=forms.TextInput()),

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        #self.fields['first_name'].widget.attrs['class'] = 'form-control'
        #self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'