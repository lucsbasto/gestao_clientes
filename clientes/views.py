from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PersonForm
from django.contrib.auth.decorators import login_required


from .models import Person


@login_required
def list_all(request):
    persons = Person.objects.all()
    return render(request, 'persons.html', {'persons' : persons});

@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)#instance = pessoa selecionada

    if form.is_valid():
        form.save()
        return redirect('list_all')
    return render(request, 'person_form.html', {'form': form})

@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_all')
    return render(request, 'person_form.html', {'form': form})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
        person.delete()
        return redirect('list_all')
    return render(request, 'person_delete_confirm.html', {'person': person})