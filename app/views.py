from django.shortcuts import render,redirect
from .models import basedata
from .forms import BaseForm
from django.contrib import messages
from django.db.models import Q



# edit data
def edit_data(request, data_id):
    data = basedata.objects.get(id=data_id)
    if request.POST:
        form = BaseForm(request.POST, instance=data)
        if form.is_valid():
            if form.save():
                return redirect('/mdsp/shortdata', messages.success(request, 'Data was successfully updated.', 'alert-success'))
            else:
                return redirect('/mdsp/shortdata', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/mdsp/shortdata', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        base_form = BaseForm(instance=data) 
        
       
        return render(request, 'edit.html', {'base_form':base_form})



# Show data in short form
def short_data(request):
    queryset_list = basedata.objects.all().order_by('id')    

    # Searching
    query_d = request.GET.get('d', None)
    query_up = request.GET.get('up', None)
    query_un = request.GET.get('un', None)
    query_m = request.GET.get('m', None) 

    if query_d:
        queryset_list = queryset_list.filter(Q(district__icontains=query_d))
    elif query_up:
        queryset_list = queryset_list.filter(Q(upazilla__icontains=query_up))
    elif query_un:
        queryset_list = queryset_list.filter(Q(s_union__icontains=query_un)) 
    elif query_m:
        queryset_list = queryset_list.filter(Q(mouza__icontains=query_m)) 
        
    

    template = 'shortdata.html'
    context = {
        'Sdata': queryset_list,
        'dis' : query_d,
        'upz' : query_up,
        'uni' : query_un,
        'moz' : query_m,
        
    }

    return render(request, template, context)


# show data in detail form
def detail_data(request):
    queryset_list = basedata.objects.all().order_by('id')    

    # Searching
    query_d = request.GET.get('d', None)
    query_up = request.GET.get('up', None)
    query_un = request.GET.get('un', None)
    query_m = request.GET.get('m', None) 

    if query_d:
        queryset_list = queryset_list.filter(Q(district__icontains=query_d))
    elif query_up:
        queryset_list = queryset_list.filter(Q(upazilla__icontains=query_up))
    elif query_un:
        queryset_list = queryset_list.filter(Q(s_union__icontains=query_un)) 
    elif query_m:
        queryset_list = queryset_list.filter(Q(mouza__icontains=query_m)) 
        
    

    template = 'detaildata.html'
    context = {
        'Ddata': queryset_list,
        'dis' : query_d,
        'upz' : query_up,
        'uni' : query_un,
        'moz' : query_m,
        
    }

    return render(request, template, context)


# map view
def map(request):
    return render(request,'map.html')

