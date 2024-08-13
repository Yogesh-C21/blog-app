from django import forms

class ProfileForm(forms.Form):
    # user_image = forms.FileField()
    
    # when only dealing with images
    user_image = forms.ImageField()