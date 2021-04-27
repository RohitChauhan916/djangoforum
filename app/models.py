# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
import subprocess
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, null=True)
    emp_code = models.CharField(verbose_name="EMP Code", max_length=100, blank=True, null=True, unique=True)
    profile_photo = models.ImageField(verbose_name="Profile Photo", upload_to='Profile', blank=True, null=True)
    dob = models.CharField(verbose_name="D.O.B", max_length=50, blank=True, null=True)
    department = models.CharField(verbose_name="Department", max_length=100, blank=True)
    phone_number = models.CharField(verbose_name="Phone Number", max_length=20, blank=True, null=True)
    web_address = models.CharField(verbose_name="Web Address", max_length=100, blank=True, null=True)
    location = models.CharField(verbose_name="Location", max_length=100, blank=True, null=True)
    hire_date = models.CharField(verbose_name="Hire Date", max_length=100, blank=True, null=True)
    about = models.TextField(verbose_name="About", max_length=100, blank=True, null=True)
    gender = models.CharField(verbose_name="Gender", max_length=20, blank=True, null=True)
    zone = models.CharField(verbose_name="Zone", max_length=100, blank=True, null=True)
    aniversary = models.CharField(verbose_name="Aniversary", max_length=100, blank=True, null=True)
    designation = models.CharField(verbose_name="Designation", max_length=100, blank=True, null=True)
    reporting_to = models.CharField(verbose_name="Reporting To", max_length=100, blank=True, null=True)
    cover_photo = models.ImageField(verbose_name="Cover", upload_to="cover", blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
        
    def save(self, *args, **kwargs):
        super(discussion, self).save(*args, **kwargs)
        if self.profile_photo:
            img = Image.open(self.profile_photo.path)
            if img.height > 500 or img.width > 500:
                output_size = (500,500)
                img.thumbnail(output_size)
                img.save(self.profile_photo.path)
        if self.cover_photo:
            img = Image.open(self.cover_photo.path)
            if img.height > 500 or img.width > 500:
                output_size = (500,500)
                img.thumbnail(output_size)
                img.save(self.cover_photo.path)


class discussion(models.Model):
    discuss_id = models.AutoField(primary_key=True)
    username = models.CharField(null=True, max_length=100)
    description = models.TextField(max_length=200, verbose_name="Description", blank=True, null=True)
    photo = models.ImageField(verbose_name="Image", upload_to='content', blank=True, null=True)
    video = models.FileField(verbose_name="Video", upload_to='video', blank=True, null=True, default=None)
    date_published = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    liked = models.ManyToManyField(User, blank=True, related_name='Likes', default=None)
    commented = models.ManyToManyField(User, blank=True, related_name='Comment', default=None)

    def __str__(self):
        return self.description
    
    def save(self, *args, **kwargs):
        super(discussion, self).save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 960 or img.width > 960:
                output_size = (960,960)
                img.thumbnail(output_size)
                img.save(self.photo.path)
    
    def num_likes(self):
        return self.liked.all().count()

class suggestion(models.Model):
    emp_code = models.CharField(verbose_name="Emp Code", max_length=200, null=True, blank=True)
    subject = models.CharField(verbose_name="Subject", max_length=200, blank=True, null=True)
    message = models.TextField(verbose_name="Message", max_length=500, null=True, blank=True)
    date_published = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.subject


class advertisements(models.Model):
    a_id = models.AutoField(primary_key=True)
    image = models.ImageField(verbose_name="Image", upload_to='advertisement', null=True, blank=True)
    link = models.CharField(verbose_name="Link", max_length=200, null=True, blank=True)
    m_img = models.ImageField(upload_to="Banner", verbose_name="Mobile Banner", null=True, blank=True)
    def __str__(self):
        return str(self.a_id)

class announce(models.Model):
    an_id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="Announcements", max_length=250, null=True, blank=True)
    desc = RichTextUploadingField()
    
    def __str__(self):
        return self.title
    
class event(models.Model):
    Title = models.CharField(max_length=255, verbose_name="Event Title", null=True, blank=True)
    image = models.ImageField(verbose_name="Event Photo", upload_to="Event", null=True, blank=True)
    event_slug = models.CharField(max_length=255)
    date_published = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.Title

class gallery(models.Model):
    event_for = models.ForeignKey(event, on_delete=models.SET_DEFAULT, default=1)
    title = models.CharField(max_length=255, verbose_name="Gallery Title", null=True, blank=True)
    desc = models.TextField()

    def __str__(self):
        return self.title

class galleryPhoto(models.Model):
    gp_id = models.AutoField(primary_key=True)
    gallery = models.ForeignKey(gallery, on_delete=models.CASCADE)
    photo = models.FileField(verbose_name="Gallery Photo", upload_to="Gallery", null=True, blank=True)
    video = models.FileField(verbose_name="Videos", upload_to="Gallery", null=True, blank=True)

    def __str__(self):
        return str(self.gp_id)
        
    def save(self, *args, **kwargs):
        super(galleryPhoto, self).save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 960 or img.width > 960:
                output_size = (960,960)
                img.thumbnail(output_size)
                img.save(self.photo.path)
        if self.video:
            paths = self.video.path
            videos = subprocess.run('ffmpeg', -8, '-i' ,paths, '-s' '640x480', 'output.mp4')
            videos.save(self.video.path)

class performer(models.Model):
    p_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Title", null=True, blank=True)

    def __str__(self):
        return self.title

class company(models.Model):
    c_id = models.AutoField(primary_key=True)
    perform = models.ForeignKey(performer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Performer Name", null=True, blank=True)
    image = models.ImageField(upload_to="Performer", null=True, blank=True)
    company_name = models.CharField(max_length=255, verbose_name="Company Name", null=True, blank=True)

    def __str__(self):
        return self.company_name
        
    def save(self, *args, **kwargs):
        super(discussion, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 500 or img.width > 500:
                output_size = (500,500)
                img.thumbnail(output_size)
                img.save(self.image.path)

class banner(models.Model):
    img_id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="Banner", verbose_name="Banner", null=True, blank=True)
    def __str__(self):
        return str(self.img_id)

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
        
class Like(models.Model):
    userlikes = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    discuss = models.ForeignKey(discussion, on_delete=models.CASCADE, blank=True, null=True)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.userlikes)

class Comment(models.Model):
    userComment = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    discuss = models.ForeignKey(discussion, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=255, verbose_name="Comment", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment)
        
class Topics(models.Model):
    topic_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Title", blank=True, null=True)
    image = models.ImageField(upload_to="quiz", verbose_name="Image", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    topic_slug = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255, verbose_name="Question", blank=True, null=True)
    option_one = models.CharField(max_length=255, verbose_name="Option_one", blank=True, null=True)
    option_two = models.CharField(max_length=255, verbose_name="Option_two", blank=True, null=True)
    option_three = models.CharField(max_length=255, verbose_name="Option_three", blank=True, null=True)
    Option_four = models.CharField(max_length=255, verbose_name="Option_Four", blank=True, null=True)
    Answer = models.CharField(max_length=255, verbose_name="Answer", blank=True, null=True)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.question)

class Score(models.Model):
    score_id = models.AutoField(primary_key=True)
    user_score = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    Scoring = models.CharField(max_length=255, verbose_name="Score", blank=True, null=True)
    right = models.CharField(max_length=50, verbose_name="Right", blank=True, null=True)
    wrong = models.CharField(max_length=50, verbose_name="Wrong", blank=True, null=True)
    no_answer = models.CharField(max_length=50, verbose_name="No_Answer", blank=True, null=True)
    Topic_score = models.CharField(max_length=255, verbose_name="Topic", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.score_id)

class userAnswer(models.Model):
    ansid = models.AutoField(primary_key=True)
    topicAnswer = models.CharField(max_length=255, verbose_name="Topic", blank=True, null=True)
    userAnswer = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name="User", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ansid)

class inputUser(models.Model):
    inputid = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255, verbose_name="Question", blank=True, null=True)
    quizAnswer = models.CharField(max_length=255, verbose_name="Answer", blank=True, null=True)
    Answer = models.ForeignKey(userAnswer, on_delete=models.CASCADE,blank=True, null=True )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.inputid)