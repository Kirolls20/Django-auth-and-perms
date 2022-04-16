from django.shortcuts import render,redirect
from .forms import SignupForm,CreatePostForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import Group,Permission,User
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .models import Post


@login_required(login_url=reverse_lazy('login'))
def home(request):
   posts= Post.objects.all()

   if request.method == "POST" :
      post_id = request.POST.get('post-id')
      user_id = request.POST.get('user_id')
      if post_id:
         post= Post.objects.filter(id=post_id).first()
         if post and( post.auther == request.user or request.user.has_perm("auth_management.delete_post")) :
            post.delete()
      elif user_id:
         user= User.objects.filter(id=user_id).first()
         if user and request.user.is_staff:
            try:
               group= Group.objects.get(name='default')
               group.user_set.remove(user)
               
               messages.success(request,"The user has been  Baned! ")
            except :
               pass
            try:
               group = Group.objects.get(name='mod')
               group.user_set.remove(user)
            except:
               pass

   return render(request,'main/home.html',{'posts':posts})

# Create New User View
def sign_up(request):
   if request.method == 'POST':
      form= SignupForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('login')
   else:
      form= SignupForm()
   return render(request,'registration/sign-up.html',{'form':form})


# Create Post Function
@login_required(login_url=reverse_lazy('login'))
@permission_required("auth_management.add_post",login_url=reverse_lazy('login'),raise_exception=True)
def create_post(request):
   if request.method =='POST':
      form= CreatePostForm(request.POST)
      if form.is_valid():
         post=form.save(commit=False)
         post.auther = request.user
         post.save()
         return redirect("/")
   
   else:
      form= CreatePostForm()
   return render(request,'main/create_post.html',{'form':form})


# def csrf_failure(request, reason=""):    
#   context = RequestContext(request)    
#   response = render_to_response('main/error403.html', context)    
#   response.status_code = 403    
#   return response