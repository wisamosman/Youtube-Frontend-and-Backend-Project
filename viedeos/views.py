from django.shortcuts import render ,redirect
from .models import Video
from .forms import VideoForm
from django.views import generic





class PostList(generic.ListView):
    model = Video



class VideoDetail(generic.DetailView):
    model = Video


class VideoCreate(generic.CreateView):
    model = Video
    fields = ['name','title','views','author','description','dislikes','tags','video']
    success_url = '/viedeos/'


class VideoEdit(generic.UpdateView):
    model = Video
    fields = ['name','title','views','author','description','dislikes','tags','video']
    success_url = '/viedeos/'
    template_name = 'viedeos/edit.html'



class VideoDelete(generic.DeleteView):
    model = Video
    success_url = '/viedeos/'



def post_list(request):
    data = Video.objects.all
    return render(request,'viedeos/post.html',{'posts':data})



def post_detail(request,post_id):
    data = Video.objects.get(id=post_id)
    return render(request,'viedeos/detail.html',{'post':data})



# Create your views here

def new_post(request):
    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/viedeos/')
        
        else:
            form = VideoForm()
    
    return render(request,'viedeos/new.html',{'form':form})


def edit_post(request,post_id):
    data = Video.objects.get(id=post_id)
    if request.method == 'POST':
        form = VideoForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/viedeos/')
        
        else:
            form = VideoForm(instance=data)

    
    return render(request,'viedeos/edit.html',{})



