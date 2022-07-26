from django import forms
from .models import Account


class RegisterationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',
    }))
    Mobile = forms.CharField(label='Mobile', required=True, widget=forms.NumberInput)
    class Meta:
        model = Account
        fields = ['Name','Role','email','Mobile','Country','Nationality','password']
        
        
    def __init__(self,*args,**kwargs):
        super(RegisterationForm, self).__init__(*args,**kwargs)
        self.fields['Name'].widget.attrs['placeholder'] = 'Enter Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['Mobile'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['Role'].widget.attrs['placeholder'] = 'Select Role'
        self.fields['Country'].widget.attrs['placeholder'] = 'Enter Country'    
        self.fields['Nationality'].widget.attrs['placeholder'] = 'Enter Nationality'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
            
    def clean(self):
        cleaned_data = super(RegisterationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError(
                "password does not match"
            )
