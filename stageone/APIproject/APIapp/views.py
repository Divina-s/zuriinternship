from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime


def my_endpoint(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')
    current_day = datetime.now().strftime('%A')
    utc_time = datetime.utcnow().isoformat(timespec='seconds') + 'Z'
    github_file_url = 'https://github.com/username/repo/blob/main/file_name.ext'
    github_repo_url = 'https://github.com/username/repo'
    status_code = 200
    
    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }
    
    return JsonResponse(data)

# Create your views here.
