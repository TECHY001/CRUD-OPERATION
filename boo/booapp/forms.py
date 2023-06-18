from django import forms

class file(forms.Form):
    name=forms.CharField(label="enter name",max_length=20)
    file=forms.FileField()