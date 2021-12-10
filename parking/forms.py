from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from parking.models import Parking, Profile


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Profile
        fields = ('username', 'role')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = Profile
        fields = ('username', 'role')


class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        exclude = 'for_reserved',

    def __init__(self, *args, **kwargs):
        super(ParkingForm, self).__init__(*args, **kwargs)
        self.fields['start_date'] = forms.SplitDateTimeField(
            input_date_formats=['%d.%m.%Y'],
            input_time_formats=['%H:%M'],
            widget=widgets.AdminSplitDateTime(
                attrs={'class': 'form-control'}))

        self.fields['end_date'] = forms.SplitDateTimeField(
            input_date_formats=['%d.%m.%Y'],
            input_time_formats=['%H:%M'],
            widget=widgets.AdminSplitDateTime(
                attrs={'class': 'form-control'}))
