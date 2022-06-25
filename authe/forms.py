from django import forms
from authe.models import registermodel
from django.contrib.auth.hashers import make_password
class registerform(forms.ModelForm):
    repassword=forms.CharField()
    class Meta:
        model=registermodel
        fields=['username','first_name','last_name','email','age','gender','phone','address','password']
    def save(self, commit=True):
        user=super().save(commit=False)
        user.password=make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    def clean(self):
        user=self.cleaned_data['username']
        if not(user[0].isupper()):
            raise forms.ValidationError("username first letter should be upper case")
        pas=self.cleaned_data['password']
        repas=self.cleaned_data['repassword']
        print(pas,repas)
        if not(pas == repas):
            raise forms.ValidationError("password and repassword should be same")

