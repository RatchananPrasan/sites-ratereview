from django.http import HttpResponseNotFound
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .models import User, Message, Reply
from .forms import RegisterForm, MessageForm, ReplyForm, EditProfileForm, ImageUploadForm
import base64
import random
# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('sites:home')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.POST['next']:
                return redirect(request.POST['next'])
            else:
                return redirect('sites:home')
        else:
            return render(request, 'accounts/login.html', {'error':'Invalid Username or Password.'})
        
    return render(request, 'accounts/login.html')


def logout_view(request):
    if request.method == "POST":
        logout(request)
        
    return redirect('sites:home')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('sites:home')
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sites:home')
    else:
        form = RegisterForm()
        
    return render(request, 'accounts/register.html', {'form':form})

def profile_view(request, username):
    POST_PER_REQUEST = 5
    profile = get_object_or_404(User, username=username)
    message_form = MessageForm()
    reply_form = ReplyForm()
    messages = Message.objects.filter(post_to=profile)
    
    if request.method == "POST" and request.is_ajax():
        post_num = int(request.POST['post_num'])
        cut_messages = messages[post_num:post_num + POST_PER_REQUEST]
        if len(cut_messages) > 0:
            return render(request, 'accounts/post_message.html', {'profile':profile,
                                                                  'messages':cut_messages,
                                                                  'reply_form':reply_form,
                                                                 })
        else:
            return HttpResponseNotFound()
    
    messages = messages[:POST_PER_REQUEST]
    return render(request, 'accounts/profile.html', {'profile':profile,
                                                     'message_form':message_form,
                                                     'reply_form':reply_form,
                                                     'messages':messages,
                                                    })

@login_required
def profile_post(request, username):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.cleaned_data['post']
            user = get_object_or_404(User,username=username)
            m = Message.objects.create(post=post,post_to=user,post_by=request.user)
            if request.is_ajax():
                messages = Message.objects.filter(id=m.id)
                reply_form = ReplyForm()
                return render(request, 'accounts/post_message.html', {'profile':user,
                                                                      'reply_form':reply_form,
                                                                      'messages':messages
                                                                     })
            
    return redirect('accounts:profile', username)


@login_required
def post_reply(request, pk):
    if request.method == "POST" and request.is_ajax():
        form = ReplyForm(request.POST)
        message = get_object_or_404(Message,pk=pk)
        if form.is_valid():
            reply = form.cleaned_data['reply']
            Reply.objects.create(reply=reply,reply_by=request.user,message=message)
            
        return render(request, 'accounts/post_reply.html', {'message':message})
                
    return redirect('sites:home')


@login_required
def edit_profile(request):
    data = {}
    if request.method == "POST":
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            data['message'] = 'Saved Changes Successfully'
    else:
        form = EditProfileForm(instance=request.user)
        
    data['form'] = form
    return render(request, 'accounts/settings_edit_profile.html', data)


@login_required
def change_password(request):
    data = {}
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            data['message'] = 'Saved Changes Successfully'
    else:
        form = PasswordChangeForm(request.user)
    
    data['form'] = form
    return render(request, 'accounts/settings_change_password.html', data)


@login_required
def change_profile_pic(request):
    data = {}
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_data = request.POST['image64'][23:]
            random_int = random.randint(1,1000000)
            img_url = '\\media\\accounts\\profile\\' + request.user.get_username() + '_' + str(random_int) + '.jpg'
            file_name = settings.MEDIA_ROOT + img_url
            with open(file_name, 'wb') as fh:
                fh.write(base64.b64decode(img_data))
                request.user.image = img_url
                request.user.save()
                
            data['message'] = 'Saved Changes Successfully'
    else:
        form = ImageUploadForm()
        
    data['form'] = form
    return render(request, 'accounts/settings_change_profile_pic.html', data)


@login_required
def delete_message(request, pk):
    m = get_object_or_404(Message,pk=pk)
    if request.method == "POST":
        if m.post_to == request.user or m.post_by == request.user:
            m.delete()
            
    return redirect('accounts:profile', m.post_to.get_username())


@login_required
def delete_reply(request, pk):
    r = get_object_or_404(Reply,pk=pk)
    if request.method == "POST" and request.is_ajax():
        if request.user == r.reply_by or request.user == r.message.post_to:
            m = r.message;
            r.delete()
            return render(request, 'accounts/post_reply.html', {'message':m})
    
    return redirect('accounts:profile', r.message.post_to.get_username())