from django.shortcuts import render,redirect # type: ignore
from .models import Crude
# Create your views here.
def Home(req):
    movies=Crude.objects.all()
    if req.method == 'POST':
        name = req.POST.get('name')
        image=req.FILES['image']
        message = req.POST.get('message')
        movie=Crude(name=name,image=image,message=message)
        movie.save()
    return render(req,"index.html",{"movies":movies})

def Display(req):
    movies=Crude.objects.all()
    return render(req,"display.html",{"movies":movies})
 
def Update(req, id):
    task = Crude.objects.get(id=id)
    if req.method == "POST":
        update_name = req.POST.get('name')
        update_message = req.POST.get('message') 
        task.name=update_name
        task.message=update_message
        if 'image' in req.FILES:
            update_image = req.FILES['image']
            task.image = update_image 
        task.save()
        task=Crude.objects.all()
        return redirect('home')
    return render(req, 'update.html', {'task': task})
def Delete(req,id):
    dele=Crude.objects.get(id=id)
    dele.delete()
    return redirect('home')


    
