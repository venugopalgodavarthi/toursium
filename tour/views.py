from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView
from tour.models import countrymodel, statemodel, citymodel, citygallary, citydetails
from tour.forms import countryform, citydetailsform, citygallaryform
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.


class countrycreate(CreateView):
    template_name = "base.html"
    model = countrymodel
    form_class = countryform
    fields = '__all__'
    success_url = '/tour/success/'
    permission_required = ('admin.can_view')


class countryselect(PermissionRequiredMixin, ListView):
    permission_required = "tour.view_countrymodel"
    template_name = "cselect.html"
    model = countrymodel
    context_object_name = 'res'
    fields = '__all__'


class countryupdate(UpdateView):
    template_name = "base.html"
    model = countrymodel
    fields = '__all__'
    success_url = '/tour/success/'


class countrydelete(DeleteView):
    template_name = "delete.html"
    model = countrymodel
    fields = '__all__'
    success_url = '/tour/success/'


class statecreate(CreateView):
    template_name = "base.html"
    model = statemodel
    fields = '__all__'
    success_url = '/tour/success/'


class stateupdate(UpdateView):
    template_name = "base.html"
    model = statemodel
    fields = '__all__'
    success_url = '/tour/success/'


class statedelete(DeleteView):
    template_name = "delete.html"
    model = statemodel
    fields = '__all__'
    success_url = '/tour/success/'


class successview(TemplateView):
    template_name = "success.html"


class citycreate(CreateView):
    template_name = "base.html"
    model = citymodel
    fields = '__all__'
    success_url = '/tour/success/'


class cityselect(ListView):
    template_name = "ciselect.html"
    model = citymodel
    context_object_name = 'res'
    fields = '__all__'


class cityupdate(UpdateView):
    template_name = "base.html"
    model = citymodel
    fields = '__all__'
    success_url = '/tour/success/'


class citydelete(DeleteView):
    template_name = "delete.html"
    model = citymodel
    fields = '__all__'
    success_url = '/tour/success/'


def selectstate(request, pk):
    res = statemodel.objects.filter(couid_id=pk)
    return render(request, 'sselect.html', {'res': res})


def selectcity(request, pk):
    res = citymodel.objects.filter(stateid_id=pk)
    print(res)
    return render(request, 'ciselect.html', {'res': res})


def show(request):
    form = countryform()
    print('hello')
    print(form)
    return HttpResponse('haii')


class citydetailscreate(CreateView):
    template_name = 'base.html'
    model = citydetails
    form_class = citydetailsform
    success_url = '/tour/success/'


'''
class citygallarycreate(CreateView):
    template_name = 'base.html'
    model = citygallary
    form_class = citygallaryform
    success_url = '/tour/success/'
'''


def citygallarycreate(request):
    if request.method == 'GET':
        form = citygallaryform()
        res = citygallary.objects.all()
        return render(request, 'citygallary.html', {"res": res, 'form': form})

    if request.method == 'POST' and request.FILES:
        form = citygallaryform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/tour/citygallary/')


def citygallaryselect(request, pk):
    if request.method == 'GET':
        res1 = citydetails.objects.get(cityid_id=pk)
        res = citydetails.objects.filter(cityid_id=pk).values_list('id')
        res = citygallary.objects.filter(citydetails_id=res[0][0])
        return render(request, 'cityhome.html', {"res": res, 'res1': res1})
