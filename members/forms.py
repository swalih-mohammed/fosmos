from django import forms
from .models import Member


class AddForm(forms.ModelForm):

    class Meta:
        model = Member
        # fields = ('first_name', 'last_name', 'phone_number', 'email', 'education', 'profession', 'graduated', 'address')
        fields = ('first_name', 'last_name', 'phone_number', 'email')


        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            # 'education': forms.TextInput(attrs={'class': 'form-control'}),
            # 'profession': forms.TextInput(attrs={'class': 'form-control'}),
            # 'graduated': forms.TextInput(attrs={'class': 'form-control'}),
            # 'address': forms.TextInput(attrs={'class': 'form-control'}),
        }