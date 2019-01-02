from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from datetime import date, datetime

def index(request):
	
	badgeCountFilterS= Posts.objects.exclude(status='Failed') & Posts.objects.exclude(lastcomplete_date__lt=date(2018, 12, 1))
	badgeCountForSuccess = badgeCountFilterS.count()
	
	badgeCountFilterF= Posts.objects.exclude(status='Success') & Posts.objects.exclude(lastcomplete_date__lt=date(2018, 12, 1))
	badgeCountForFailed = badgeCountFilterF.count()

	context = {
		'badgeCountForSuccess': badgeCountForSuccess,
		'badgeCountForFailed': badgeCountForFailed
	}

	return render(request, 'posts/index.html', context)

