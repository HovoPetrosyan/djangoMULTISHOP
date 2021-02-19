from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, PasswordInput, Select, FileInput
from UserApp.models import UserProfile


# sign up form

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, label="username", widget=forms.TextInput(
        attrs={'placeholder': 'Username', }
    ))
    email = forms.EmailField(max_length=200, label="email", widget=forms.EmailInput(
        attrs={'placeholder': 'Email', }
    ))
    first_name = forms.CharField(max_length=100, label="first_name", widget=forms.TextInput(
        attrs={'placeholder': 'First name', }
    ))
    last_name = forms.CharField(max_length=100, label="last_name", widget=forms.TextInput(
        attrs={'placeholder': 'Last name', }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter password',
                                                    'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repeat password',
                                                    'class': 'form-control'}),
        }


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }


CITY = [
    ('Երևան', 'Երևան'),
    ('Աբովյան ', 'Աբովյան'),
    ('Ագարակ', 'Ագարակ'),
    ('Ալավերդի', 'Ալավերդի'),
    ('Աշտարակ', 'Աշտարակ'),
    ('Ախթալա', 'Ախթալա'),
    ('Ապարան', 'Ապարան'),
    ('Արարատ', 'Արարատ'),
    ('Արթիկ', 'Արթիկ'),
    ('Արմավիր', 'Արմավիր'),
    ('Արտաշատ', 'Արտաշատ'),
    ('Բերդ', 'Բերդ'),
    ('Բյուրեղավան', 'Բյուրեղավան'),
    ('Գավառ', 'Գավառ'),
    ('Գյումրի', 'Գյումրի'),
    ('Գորիս', 'Գորիս'),
    ('Դաստակերտ', 'Դաստակերտ'),
    ('Դիլիջան', 'Դիլիջան'),
    ('Եղեգնաձոր', 'Եղեգնաձոր'),
    ('Եղվարդ', 'Եղվարդ'),
    ('Թալին', 'Թալին'),
    ('Իջևան', 'Իջևան'),
    ('Ծաղկաձոր', 'Ծաղկաձոր'),
    ('Կապան', 'Կապան'),
    ('Հրազդան', 'Հրազդան'),
    ('Ճամբարակ', 'Ճամբարակ'),
    ('Մասիս', 'Մասիս'),
    ('Մարալիկ', 'Մարալիկ'),
    ('Մարտունի', 'Մարտունի'),
    ('Մեծամոր', 'Մեծամոր'),
    ('Մեղրի', 'Մեղրի'),
    ('Նոյեմբերյան', 'Նոյեմբերյան'),
    ('Նոր Հաճն', 'Նոր Հաճն'),
    ('Չարենցավան', 'Չարենցավան'),
    ('Ջերմուկ', 'Ջերմուկ'),
    ('Սիսիան', 'Սիսիան'),
    ('Սպիտակ', 'Սպիտակ'),
    ('Ստեփանավան', 'Ստեփանավան'),
    ('Սևան', 'Սևան'),
    ('Վաղարշապատ', 'Վաղարշապատ'),
    ('Վայք', 'Վայք'),
    ('Վանաձոր', 'Վանաձոր'),
    ('Վարդենիս', 'Վարդենիս'),
    ('Վեդի', 'Վեդի'),
    ('Տաշիր', 'Տաշիր'),
    ('Քաջարան', 'Քաջարան'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }
