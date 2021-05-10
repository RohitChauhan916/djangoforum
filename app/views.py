# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, UserExtend, ProfilePhoto, discussionForm, SuggestionForm, EditProfile,UserEdit
from django.core.files.base import ContentFile 
from .models import UserProfile, discussion, suggestion, advertisements, announce, event, galleryPhoto, gallery, performer, company, banner,Like, Comment,Quiz,Topics,Score,userAnswer,inputUser
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
                email = form.cleaned_data.get('email')
                message = f"Your are register Now: {username}"
                messages.success(request, f"New Account Created: {username}")
                message = f"Hey there, {username}\n\n\nThank you for joining AIPL Parivaar. We are going to do some amazing things here.\n\nSpeaking of amazing, the AGM 2021 was just too amazing.\n\nEveryone had a great time and the entry of legendry KAPIL DEV took our meet to the next level.\n\nWe all made some life-long memories and so we did manage to capture a few of them.\n\nHere is the like where you can download these memories and share them with your AIPL Parivaar.\n\nhttps://photos.app.goo.gl/WgjwxeKmuryQEYu7A\n\n So, browse, download &amp; Share at www.aiplparivaar.com\n\n\nLooking forward,\n\nTeam AIPL Parivaar"
                send_mail('Welcome to your Parivaar – AIPL Parivaar', message, settings.EMAIL_HOST_USER,[email], fail_silently=False)
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
        user_discuss = request.user.userprofile
        if request.method == 'POST':
            form = discussionForm(request.POST, request.FILES)
            if form.is_valid():
                discuss = request.POST.get('description')
                image = form.cleaned_data.get('photo')
                video = form.cleaned_data.get('video')
                if request.user.is_authenticated:
                    user_name = request.user
                    form, created = discussion.objects.get_or_create(username=str(user_name), description=discuss, photo=image, video=video, profile=user_discuss)
                form.save()
        else:
            form = discussionForm()
        post = discussion.objects.all().order_by('-date_published')
        uservalue = request.user
        profile_photo = UserProfile.objects.get(user=uservalue)
        banners = banner.objects.all()
        coment = Comment.objects.all()
        return render(request, "homepage.html", {'profile':form, 'post':post, 'profiles':profile_photo, 'banners':banners, 'comment':coment})
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
        users = User.objects.get(username=uservalue)
        try:
            score = Score.objects.filter(user_score=profile)
        except Score.DoesNotExist:
            score = "None"
        return render(request, "edit_profile.html",{'profile':profile,'users':users,'score':score})

def update(request, id):
    if request.user.is_authenticated:
        uservalue = request.user
        userid = request.user.id
        profile = UserProfile.objects.get(user=uservalue)
        users = User.objects.get(id=userid)
        form = EditProfile(request.POST, request.FILES, instance=profile,)
        form1 = UserEdit(request.POST, instance=users,)
        if form.is_valid() or form1.is_valid():
            try:
                form.save()
                form1.save()
                emp = form.cleaned_data.get('emp_code')
                messages.error()
                return redirect('/')
            except:
                pass
        return render(request,'edit_profile.html',{'profile':profile, 'users':users})

def like_unlike_post(request):
    if request.user.is_authenticated:
        userlike = request.user
        if request.method == "POST":
            post_id = request.POST.get('prof_id')
            post_obj = discussion.objects.get(discuss_id=post_id)
            liked = False

            if userlike in post_obj.liked.all():
                liked = False
                post_obj.liked.remove(userlike)
            else:
                liked = True
                post_obj.liked.add(userlike)

            like, created = Like.objects.get_or_create(userlikes=userlike, discuss_id=post_id)

            if not created:
                if like.value =='Like':
                    like.value='unlike'
                else:
                    like.value='Like'
            else:
                like.value='Like'
                    
            post_obj.save()
            like.save()
        return JsonResponse({"liked": liked, "count":post_obj.num_likes()})

def comment_post(request):
    if request.user.is_authenticated:
        user_comment = request.user.userprofile
        if request.method == "POST":
            comment = request.POST.get('comment_post')
            comment_id = request.POST.get('prof_id')
            comment, created = Comment.objects.get_or_create(userComment=user_comment, discuss_id=comment_id,comment=comment)

            comment.save()
        return redirect('/')

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
            emp = request.POST.get('emp_code')
            subject = request.POST.get('subject')
            messages = request.POST.get('message')
            message = "EMP-Code" + " - " + emp + "\n" + "Subject" + " - " + subject + "\n" + "Message" + " - " + messages
            send_mail('Suggestion Form', message, settings.EMAIL_HOST_USER,['rohitc.aiplbrandbuzz@gmail.com','hr@aiplabro.com','hrho@ajitindustries.com'], fail_silently=False)

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

def navbarView(request):
    if request.user.is_authenticated:
        return render(request,'navbar.html')
        
def remove_discuss(request, post_id):
    user_delete = get_object_or_404(discussion, pk=post_id)
    if request.user.username == user_delete.username:
        user_delete.delete()
        return redirect('/')
    else:
        return HttpResponse("Not Delete")
        
def remove_comment(request, comment_id):
    delete_comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.userprofile == delete_comment.userComment or request.user.userprofile != delete_comment.userComment:
        delete_comment.delete()
        return redirect('/')
    else:
        return HttpResponse("Not Delete")
        
def quiz(request):
    if request.user.is_authenticated:
        quizes = Topics.objects.all()
    else:
        return redirect('/')
    return render(request, 'quiz.html', {'quiz_topic':quizes})

def quiz_Test(request, single_slug):
    if request.user.is_authenticated:
        quiz = [q.topic_slug for q in Topics.objects.all()]
        if single_slug in quiz:
            test = Quiz.objects.filter(topic__topic_slug=single_slug)
    else:
        return HttpResponse("No test for unregister user")
    return render(request,"quiz_test.html", {'testing':test})

def test_quiz(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            users = request.user.userprofile
            quiz = Quiz.objects.all()
            topic = request.POST.get('Top')
            right = 0
            wrong = 0
            no_answer = 0
            
            allanswer, created = userAnswer.objects.get_or_create(topicAnswer=topic, userAnswer=users)
            allanswer.save()
            
            for questions in quiz:
                correct_answer = questions.Answer
                entered_answer = request.POST.get("value" + str(questions.quiz_id))
                print("User Click",entered_answer)
                if(entered_answer == correct_answer):
                    right+=1
                elif(entered_answer == "None"):
                    no_answer+=1
                else:
                    wrong+=1

                percentage = right / 10 * 100

                quest = request.POST.get("quiz_ques" + str(questions.quiz_id))
                print("quest", quest)
                print(allanswer)
                useans = userAnswer.objects.get(ansid=allanswer.ansid)
                try:
                    extendAns = inputUser.objects.create(question=str(quest), quizAnswer=str(entered_answer), Answer=useans)
                except inputUser.DoesNotExist:
                    extendAns = None
                extendAns.save()
            
            try:
                scoring, created = Score.objects.get_or_create(user_score=users, Scoring=str(percentage), right=str(right), wrong=str(wrong), no_answer=str(no_answer), Topic_score=topic)
            except Score.DoesNotExist:
                scoring = None
            scoring.save()
        context = {"right":right, "wrong":wrong, "no_answer":no_answer, "percentage":percentage}
        return render(request, "quiz_result.html", context)