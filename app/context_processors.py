from app.models import advertisements, announce, UserProfile

def extras(request):
    ads = advertisements.objects.all()
    announced = announce.objects.all()
    profile = UserProfile.objects.all()
    return {'ads':ads, 'announced':announced, 'profiles':profile}
