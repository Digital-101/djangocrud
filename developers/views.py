from django.shortcuts import render, redirect  
from developers.forms import DeveloperForm  
from developers.models import Developer

# Create your views here.  
# def index(request): # < here
#     return render(request, 'developers/index.html')

#function to add record
def dev(request):  
    if request.method == "POST":  
        form = DeveloperForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = DeveloperForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    developers = Developer.objects.all()  
    return render(request,"show.html",{'developers':developers})  

def edit(request, id):  
    developer = Developer.objects.get(id=id)  
    return render(request,'edit.html', {'developer':developer})  

def update(request, id):  
    developer = Developer.objects.get(id=id)  
    form = DeveloperForm(request.POST, instance = developer)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'developer': developer})  

def destroy(request, id):  
    developer = Developer.objects.get(id=id)  
    developer.delete()  
    return redirect("/show")