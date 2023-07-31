from django.shortcuts import render
from .models import Video
from .forms import VideoForm



def post_list(request):
    data = Video.objects.all
    return render(request,'viedeos/post.html',{'post':data})




def post_detail(request,post_id):
    data = Video.objects.get(id=post_id)
    return render(request,'viedeos/detail.html',{'post':data})



# Create your views here.

def new_post(request):
    if request.method == 'POST':
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        
        else:
            form = VideoForm()
    
    return render(request,'viedeos/post.html',{'form':form})


def edit_post(request,post_id):
    data = Video.objects.get(id=post_id)
    if request.method == 'POST':
        form = VideoForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
        
        else:
            form = VideoForm(instance=data)

    
    return render(request,'viedeos/edit.html',{'form':form})
