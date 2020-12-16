from app.models import advertisements, announce, UserProfile

def extras(request):
    ads = advertisements.objects.all()
    announced = announce.objects.all()
    profiling = None
    try:
        if request.user.is_authenticated:
            profiling = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profiling = None
    return {'ads':ads, 'announced':announced, 'profi':profiling}
