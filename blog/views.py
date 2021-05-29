from django.shortcuts import render,redirect,get_object_or_404
from .models import registration,Post,Preference,Comment,Subcomment
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers



# Create your views here.
def index(request):
    p={
        'post':Post.objects.all()
    }
    return render(request,'index.html',p)

def login(request):
    if request.method == 'POST':
        try:
            p=request.POST.get('Password')
            u=registration.objects.get(Email=request.POST.get('Email'))
            if check_password(p,u.Password):
                request.session['Email']=request.POST.get('Email')
                Email=request.session['Email']
            
                return redirect('profile')

            else:
                messages.success(request,'Email or Password is invalid')
            

        except registration.DoesNotExist as e:
            messages.success(request,'Email or Password is invalid')

    return render(request,'login.html')
    

def register(request):
    if request.method=='POST' and  request.FILES['image']:
        FirstName=request.POST.get('FirstName')
        LastName=request.POST.get('LastName')
        Email=request.POST.get('Email')
        Password=make_password(request.POST.get('Password'))
        ConfirmPassword=request.POST.get('ConfirmPassword')
        UserName=request.POST.get('UserName')
        image=request.FILES['image']
        registration(FirstName=FirstName,LastName=LastName,UserName=UserName,Email=Email,Password=Password,image=image).save()
        return redirect('login')

    else:
        return render(request,'register.html')
     
    return render(request,'register.html')
    
   

def profile(request):
    r=registration.objects.get(Email=request.session['Email'])
    return render(request,'profile.html',{'info':r})


def newpost(request):
    if request.method=='POST' and request.FILES['Thumbnail']:
        Title=request.POST.get('Title')
        Overview=request.POST.get('Overview')
        Author=request.POST.get('Author')
        Category=request.POST.get('Category')
        Email=request.POST.get('Email')
        Thumbnail=request.FILES['Thumbnail']
        request.session['Author']=request.POST.get('Author')
       
        Post(Title=Title,Overview=Overview,Author= Author,Email=Email,Category=Category,Thumbnail=Thumbnail).save()
        messages.success(request,'Post has been added succesfully')
        return render(request,'newpost.html')
    return render(request,'newpost.html')


def logout(request):
    try:
        del request.session['Email']
    except:
        p={
        'post':Post.objects.all()
        }
        return redirect('index.html',p)

    p={
        'post':Post.objects.all()
    }

    return render(request,'index.html',p)

    
def mypost(request):
    e=request.session['Email']
    p={
        'post':Post.objects.filter(Email=e)
    }
    return render(request,'mypost.html',p)


def viewpost(request,pk):
    posts=Post.objects.get(id=pk)
    if request.method=='POST':
        comm=request.POST.get('comm')
        comm_id=request.POST.get('comm_id')
        if comm_id:
            r=registration.objects.get(Email=request.session['Email'])
            Subcomment(post=posts,user_id=request.session['Email'],ima=r.image,comm=comm,comment=Comment.objects.get(id=int(comm_id))).save()

        else:
            r=registration.objects.get(Email=request.session['Email'])
            Comment(post=posts, user_id=request.session['Email'],im=r.image,comm=comm).save()

    comments=[]
    for c in Comment.objects.filter(post=posts):
        comments.append([c,Subcomment.objects.filter(comment=c)])
    
    return render(request,'viewpost.html',{'posts':posts,'comments':comments})




def change(request):
    if request.method=='POST':
        posts=registration.objects.get(Email=request.POST.get('Email'))
        posts.Password=make_password(request.POST.get('Password'))
        posts.save()

        
        messages.success(request,'Password has been Changed Succesfully')
        return redirect('login')

    return render(request,'change.html')



def update(request,pk):
    d=Post.objects.get(id=pk)
    if request.method=='POST' and request.FILES['thumbnail']:
        d.Title=request.POST.get('title')
        d.save()
        d.Overview=request.POST.get('overview')
        d.save()
        d.Category=request.POST.get('category')
        d.save()
        d.Thumbnail=request.FILES['thumbnail']
        d.save()

        messages.success(request,'Post has been Edited Succesfully')
        return render(request,'update.html',{"Post":d})

    return render(request,'update.html',{"Post":d})


def postpreference(request,pk):
    if request.method=='POST':
        eachpost= Post.objects.get(id=pk)


        c=request.POST.get('like')
        d=request.POST.get('dislike')
        if c:
            v=int(c) #preference
        else:
            v=int(d) #preference


        try:
            ob=Preference.objects.get(user_id= request.session['Email'], post_id=eachpost.id)
            val=ob.value
            val=int(val)
            us=v
            if val!=us:
                ob.delete()
                upref= Preference()
                upref.user_id= request.session['Email']
                upref.post_id= eachpost.id
                upref.value= us
                if us==1 and val!=1:
                    eachpost.likes+=1
                    eachpost.dislikes-=1

                elif us==2 and val!=2:
                    eachpost.dislikes+=1
                    eachpost.likes-=1

                upref.save()
                eachpost.save()

                return render(request,'viewpost.html',{'posts':eachpost})


            elif val==us:
                ob.delete()
                if us==1:
                    eachpost.likes-=1

                elif us==2:
                    eachpost.dislikes-=1

                eachpost.save()
                return render(request,'viewpost.html',{'posts':eachpost})



        except Preference.DoesNotExist:
            us=v
            upref= Preference()
            upref.user_id= request.session['Email']
            upref.post_id= eachpost.id
            upref.value= us
            us=v
            if us==1:
                eachpost.likes+=1

            elif us==2:
                eachpost.dislikes+=1


            upref.save()
            eachpost.save()                            
            return render(request,'viewpost.html',{'posts':eachpost})







    return render(request,'viewpost.html',{'posts':eachpost})





def searchbar(request):
    if request.method=='POST':
        q = request.POST.get('search')
        p = Post.objects.filter(Title__icontains=q)
        return render(request,'searchbar.html',{'p':p})

    return render(request,'searchbar.html')
   



def updateprofile(request):
    u=registration.objects.get(Email=request.session['Email'])
    if request.method=='POST' and  request.FILES['image']:
        u.FirstName=request.POST.get('FirstName')
        u.save()
        u.LastName=request.POST.get('LastName')
        u.save()
        u.Email=request.POST.get('Email')
        u.save()
        u.image=request.FILES['image']
        u.save()
        u.UserName=request.POST.get('UserName')
        u.save()
        messages.success(request,'Profile has been changed Succesfully')
        return render(request,'updateprofile.html')
        
    return render(request,'updateprofile.html')



def popular(request):
    p=Post.objects.all().values_list('likes')
    p=list(p)
    x=int(max(p)[0])
    v=Post.objects.filter(likes=x)

    return render(request,'popular.html',{'m':v}) 