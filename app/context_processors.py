from app.models import advertisements, announce, UserProfile, Like, discussion

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

def notification(request):
    user_like = None
    try:
        if request.user.is_authenticated:
            user_notify = discussion.objects.filter(username=request.user)
            com = user_notify
            user_like = Like.objects.filter(discuss__in=com).order_by('-created')
    except Like.DoesNotExist:
        user_like = None

    return {'notify':user_like}