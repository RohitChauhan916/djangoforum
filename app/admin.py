from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile, discussion, suggestion, advertisements, announce, event, gallery, galleryPhoto, performer, company, banner,Like,Comment,Quiz,Topics,Score,userAnswer,inputUser
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class CustomSuggestionAdmin(admin.ModelAdmin):
    list_display = ('emp_code','subject','date_published')

class galleryphotoInline(admin.TabularInline):
    model = galleryPhoto
    extra = 3

class galleryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['title','desc','event_for',]}),]
    inlines = [galleryphotoInline]

class companyInline(admin.TabularInline):
    model = company
    extra = 1

class performerAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['title',]}),]
    inlines = [companyInline]
    
class quizInline(admin.StackedInline):
    model = Quiz
    extra = 0

class TopicAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['title','image','topic_slug',]}),]
    inlines = [quizInline]

class InputInline(admin.TabularInline):
    model = inputUser
    extra = 0

class AnswerAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['topicAnswer','userAnswer']}),]
    inlines = [InputInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(discussion)
admin.site.register(suggestion,CustomSuggestionAdmin)
admin.site.register(performer,performerAdmin)
admin.site.register(advertisements)
admin.site.register(announce)
admin.site.register(event)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(gallery,galleryAdmin)
admin.site.register(banner)
admin.site.register(Topics,TopicAdmin)
admin.site.register(Score)
admin.site.register(userAnswer,AnswerAdmin)