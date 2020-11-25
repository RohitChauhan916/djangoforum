from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, UserExtend, ProfilePhoto, discussionForm, SuggestionForm, EditProfile
from django.core.files.base import ContentFile 
from .models import UserProfile, discussion, suggestion, advertisements, announce, event, galleryPhoto, gallery, performer, company, banner
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            form1 = UserExtend(request.POST)
            if form.is_valid() * form1.is_valid():
                user = form.save()
                prof = form1.save(commit=False)
                prof.user = user
                prof.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"New Account Created: {username}")
                return redirect("/register")
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            log = AuthenticationForm(request, data=request.POST)
            if log.is_valid():
                username = log.cleaned_data.get('username')
                password = log.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request,f"you are logged in {username}")
                    return redirect('/')
                else:
                    messages.error(request,"invalid username and password")
            else:
                messages.error(request,"invalid username and password")
        log = AuthenticationForm()
        form = SignUpForm()
        form1 = UserExtend()
    return render(request, "register.html", context={"form":form, "form1":form1,"log":log})
   

def homepage(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = discussionForm(request.POST, request.FILES)
            if form.is_valid():
                discuss = request.POST.get('description')
                image = form.cleaned_data.get('photo')
                if request.user.is_authenticated:
                    user_name = request.user
                    form, created = discussion.objects.get_or_create(username=user_name, description=discuss, photo=image)
                form.save()
        else:
            form = discussionForm()
        post = discussion.objects.all().order_by('-date_published')
        uservalue = request.user
        profile_photo = UserProfile.objects.get(user=uservalue)
        pic = discussion.objects.filter(profile=profile_photo)
        banners = banner.objects.all()
        return render(request, "homepage.html", {'profile':form, 'post':post, 'profiles':profile_photo, 'banners':banners, 'pic':pic})
    else:
        return redirect("/register")

def logout_req(request):
    logout(request)
    messages.info(request, "Logout successful")
    return redirect("/")

def profile(request, id):
    if request.user.is_authenticated:
        uservalue = request.user
        profile = UserProfile.objects.get(user=uservalue)
        return render(request, "profile.html", {'profile':profile})
    else:
        return redirect("/homepage")

def edit_profile(request, id):
    if request.user.is_authenticated:
        uservalue = request.user
        profile = UserProfile.objects.get(user=uservalue)
        return render(request, "edit_profile.html",{'profile':profile})

def update(request, id):
    if request.user.is_authenticated:
        uservalue = request.user
        profile = UserProfile.objects.get(user=uservalue)
        form = EditProfile(request.POST, request.FILES, instance=profile,)
        if form.is_valid():
            try:
                form.save()
                emp = form.cleaned_data.get('emp_code')
                messages.error()
                return redirect('/')
            except:
                pass
        return render(request,'edit_profile.html',{'profile':profile})

def timeline(request, id):
    if request.user.is_authenticated:
        uservalue = request.user
        profile = UserProfile.objects.get(user=uservalue)
        try:
            user_post = discussion.objects.filter(username=uservalue)
        except discussion.DoesNotExist:
            user_post = None
        return render(request, 'timeline.html', {'timeline':profile, 'post':user_post})
    else:
        return redirect("/profile/id")

def suggest(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SuggestionForm(request.POST)
            fullname = request.POST.get('name')
            emp = request.POST.get('emp_code')
            phone = request.POST.get('phone')
            departmant = request.POST.get('departmant')
            designation = request.POST.get('designation')
            report = request.POST.get('reporting_to')
            zone = request.POST.get('zone')
            subject = request.POST.get('subject')
            messages = request.POST.get('message')
            message = "Name" + " - " + fullname + "\n" + "EMP-Code" + " - " + emp + "\n" + "Phone" + " - " + phone + "\n" + "Department" + " - " + departmant + "\n" + "Designation" + " - " + designation + "\n" + "Report" + " - " + report + "\n" + "Zone" + " - " + zone + "\n" + "Subject" + " - " + subject + "\n" + "Message" + " - " + messages
            send_mail('Suggestion Form', message, settings.EMAIL_HOST_USER,['rohitc.aiplbrandbuzz@gmail.com'], fail_silently=False)

            if form.is_valid():
                form.save()
        else:
            form = SuggestionForm()
        return render(request, "suggestion.html", {'form':form})
    else:
        return redirect('/')

def advertisement(request):
    if request.user.is_authenticated:
        return render(request,"ads.html")


def announceView(request):
    if request.user.is_authenticated:
        return render(request,"announcement.html")

def single_slug(request, single_slug):
    if request.user.is_authenticated:
        events = [e.event_slug for e in event.objects.all()]
        if single_slug in events:
            this_events = gallery.objects.get(event_for__event_slug = single_slug)
            gall = this_events.id
            photos = galleryPhoto.objects.filter(gallery=gall)
            return render(request, 'gallery.html',{'gallery':this_events, 'photos':photos})

def eventView(request):
    try:
        context = event.objects.all()
    except event.DoesNotExist:
        context = None
    return render(request, 'event.html',{'event':context})

def perfomerView(request):
    if request.user.is_authenticated:
        perform = performer.objects.all()
        com = perform
        comp = company.objects.filter(perform=com)
        return render(request, 'performer.html',{'perform':perform, 'company':comp})

def offers(request):
    if request.user.is_authenticated:
        return render(request,'offers.html')

        