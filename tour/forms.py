
from django import forms
from tour.models import countrymodel, citydetails, citygallary


class countryform(forms.ModelForm):
    class Meta:
        model = countrymodel
        fields = "__all__"


class citydetailsform(forms.ModelForm):
    class Meta:
        model = citydetails
        fields = "__all__"


class citygallaryform(forms.ModelForm):
    class Meta:
        model = citygallary
        fields = "__all__"
