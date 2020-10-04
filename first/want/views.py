from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import include, reverse_lazy, reverse
from django import forms
from .models import want
from .forms import add_items, del_items, update_items


def index(request):

    return HttpResponse("""<h1>Let's get it done!, you are in WANT view</h1>
                           <a href = {% url }""")


def my_list(request):

    list_items = want.objects.values()
    context = {
        'things' : list_items
    }
    return render(request, 'want/my_list.html', context)


def lets_add(request):

    list_items = want.objects.values()
    item = want()

    if request.method == 'POST':
        form = add_items(request.POST)

        if form.is_valid():
            item.item_name = form.cleaned_data['item_name']
            item.save()

            return HttpResponseRedirect(reverse_lazy('want:my_list'))
        
    else:
        # form = want_items(initial={'item_name' : 'Enter item name'})
        form = add_items()

    context = {
        'form' : form,
        'things' : list_items
    }

    return render(request, 'want/lets_add.html', context)


def lets_del(request):

    list_items = want.objects.values()

    if request.method == 'POST':
        form = del_items(request.POST)

        if form.is_valid():
            try:
                item = want.objects.get(pk = form.cleaned_data['item_no'])
                item.delete()
                return HttpResponseRedirect(reverse_lazy('want:my_list'))
            except:
                return HttpResponse(form.cleaned_data['item_no'])

    else:
        # form = want_items(initial={'item_name' : 'Enter item name'})
        form = del_items()

    context = {
        'form' : form,
        'things' : list_items
    }

    return render(request, 'want/lets_del.html', context)


def lets_update(request):

    list_items = want.objects.values()

    if request.method == 'POST':
        form = update_items(request.POST)

        if form.is_valid():
            try:
                item = want.objects.get(pk = form.cleaned_data['item_no'])
                item.item_name = form.cleaned_data['item_name']
                item.save()

                return HttpResponseRedirect(reverse_lazy('want:my_list'))
            except:
                return HttpResponse("<h2>This item id does not exist " + form.cleaned_data['item_no'] + "</h2")

    else:
        # form = want_items(initial={'item_name' : 'Enter item name'})
        form = update_items()

    context = {
        'form' : form,
        'things' : list_items
    }

    return render(request, 'want/lets_update.html', context)