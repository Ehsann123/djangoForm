from django import forms

class StepOneForm(forms.Form):
    first_name = forms.CharField(label="first name", max_length=100)
    last_name = forms.CharField(label="last name", max_length=100)

class StepTwoForm(forms.Form):
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone Number")

class StepThreeForm(forms.Form):
    message = forms.CharField(label="Message", widget=forms.Textarea)
    
