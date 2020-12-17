from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class UserProfile(models.Model):
    UserProfile_id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, null=True)
    emp_code = models.CharField(verbose_name="EMP Code", max_length=100, blank=True, null=True, unique=True)
    profile_photo = models.ImageField(verbose_name="Profile Photo", upload_to='Profile', blank=True, null=True)
    dob = models.CharField(verbose_name="D.O.B", max_length=50, blank=True, null=True)
    department = models.CharField(verbose_name="Department", max_length=100, blank=True, null=True)
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
        return str(self.emp_code)


class discussion(models.Model):
    discuss_id = models.AutoField(primary_key=True, null=True)
    username = models.CharField(null=True, max_length=100)
    description = models.TextField(max_length=200, verbose_name="Description", blank=True, null=True)
    photo = models.ImageField(verbose_name="Image", upload_to='content', blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.description

class Likes(models.Model):
    like_id = models.AutoField(primary_key=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discuss = models.ForeignKey(discussion, on_delete=models.CASCADE)

class suggestion(models.Model):
    suggest_id = models.AutoField(primary_key=True, null=True)
    emp_code = models.CharField(verbose_name="Emp Code", max_length=200, null=True, blank=True)
    subject = models.CharField(verbose_name="Subject", max_length=200, blank=True, null=True)
    message = models.TextField(verbose_name="Message", max_length=500, null=True, blank=True)
    date_published = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.subject


class advertisements(models.Model):
    a_id = models.AutoField(primary_key=True, null=True)
    image = models.ImageField(verbose_name="Image", upload_to='advertisement', null=True, blank=True)
    link = models.CharField(verbose_name="Link", max_length=200, null=True, blank=True)
    m_img = models.ImageField(upload_to="Banner", verbose_name="Mobile Banner", null=True, blank=True)
    def __str__(self):
        return str(self.a_id)

class announce(models.Model):
    an_id = models.AutoField(primary_key=True, null=True)
    title = models.CharField(verbose_name="Announcements", max_length=250, null=True, blank=True)
    desc = RichTextUploadingField()
    
    def __str__(self):
        return self.title
    
class event(models.Model):
    event_id = models.AutoField(primary_key=True, null=True)
    Title = models.CharField(max_length=255, verbose_name="Event Title", null=True, blank=True)
    image = models.ImageField(verbose_name="Event Photo", upload_to="Event", null=True, blank=True)
    event_slug = models.CharField(max_length=255)
    date_published = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.Title

class gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True, null=True)
    event_for = models.ForeignKey(event, on_delete=models.SET_DEFAULT, default=1)
    title = models.CharField(max_length=255, verbose_name="Gallery Title", null=True, blank=True)
    desc = models.TextField()

    def __str__(self):
        return self.title

class galleryPhoto(models.Model):
    gp_id = models.AutoField(primary_key=True, null=True)
    gallery = models.ForeignKey(gallery, on_delete=models.CASCADE)
    photo = models.FileField(verbose_name="Gallery Photo", upload_to="Gallery", null=True, blank=True)

    def __str__(self):
        return str(self.gp_id)

class performer(models.Model):
    p_id = models.AutoField(primary_key=True, null=True)
    title = models.CharField(max_length=255, verbose_name="Title", null=True, blank=True)

    def __str__(self):
        return self.title

class company(models.Model):
    c_id = models.AutoField(primary_key=True, null=True)
    perform = models.ForeignKey(performer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Performer Name", null=True, blank=True)
    image = models.ImageField(upload_to="Performer", null=True, blank=True)
    company_name = models.CharField(max_length=255, verbose_name="Company Name", null=True, blank=True)

    def __str__(self):
        return self.company_name

class banner(models.Model):
    img_id = models.AutoField(primary_key=True, null=True)
    img = models.ImageField(upload_to="Banner", verbose_name="Banner", null=True, blank=True)
    def __str__(self):
        return str(self.img_id)
        