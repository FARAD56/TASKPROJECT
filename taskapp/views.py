from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import TaskModel
from .forms import TaskModelForm, TaskUpdateForm


#create your views here
def index(request):
    #ORM
    if request.method == 'POST':
         form = TaskModelForm(request.POST )
         if form.is_valid():
               form.save()
               return redirect('/')
    else :
          form = TaskModelForm()
    
    data = TaskModel.objects.all().order_by('-date')
    total_data = data.count()
    completed_data = TaskModel.objects.filter(isComplete = True).count()
    uncompleted_data = total_data - completed_data

    context = {
        'data' : data,
        'form' : form,
        'total_data' : total_data,
        'completed_data':completed_data,
        'uncompleted_data': uncompleted_data,
    }
    return render(request, 'taskapp/index.html', context)
 

def delete(request, pk):
    item = TaskModel.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'taskapp/delete.html')


def edit(request, pk):
    item = TaskModel.objects.get(id = pk)
    if request.method =='POST':
        form = TaskUpdateForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
       form = TaskUpdateForm(instance = item)
    context ={
        'form': form,
    }
    return render(request, 'taskapp/edit.html', context)
def about(request):
        return render(request,'taskapp/about.html')