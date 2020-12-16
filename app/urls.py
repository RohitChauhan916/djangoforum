
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name='app'

urlpatterns = [
   path('sw.js', (TemplateView.as_view(template_name="sw.js", content_type='application/javascript', )), name='sw.js'),
   path('',views.homepage, name="homepage"),
   path('register/',views.register, name="register"),
   path('profile/<int:id>',views.profile, name="profile"),
   path('edit_profile/<int:id>',views.edit_profile, name="edit_profile"),
   path('update/<int:id>',views.update, name="update"),
   path('timeline/<int:id>',views.timeline, name="timeline"),
   path('suggest/',views.suggest, name="suggest"),
   path('ads/',views.advertisement, name="advertisement"),
   path('announce/',views.announceView, name="announce"),
   path('event/',views.eventView, name="event"),
   path('event/<single_slug>',views.single_slug, name="single_slug"),
   path('perform/',views.perfomerView, name="perform"),
   path('offers/',views.offers, name="offers"),
   path('navbar/',views.navbarView, name="navbar"),
   path("logout", views.logout_req, name="logout"),
   
   path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"), name="password_reset"),

   path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

   path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)