from django.shortcuts import render,redirect
from .models import tab
from .forms import create_form
# Create your views here.
def tables(request):
    if request.method=="POST":
        taskname=request.POST.get('name')
        description=request.POST.get('description')
        obj=tab(name=taskname,description=description)
        obj.save()
    return render(request,'form.html')

def disp(request):
    task=tab.objects.all()
    dict_task={
        'name':task
    }
    return render(request,'table.html',dict_task)

def update(request,update_id):
    task=tab.objects.get(id=update_id)
    form=create_form(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('table')
    return render(request,'update.html',{'form':form})

def delete(request,del_id):
    task=tab.objects.get(id=del_id)
    task.delete()
    return redirect('table')