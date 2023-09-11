from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime


def my_endpoint(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')
    current_day = datetime.now().strftime('%A')
    utc_time = datetime.utcnow().isoformat(timespec='seconds') + 'Z'
    github_file_url = 'https://github.com/Divina-s/zuriinternship/blob/master/stageone/APIproject/APIapp/views.py'
    github_repo_url = 'https://github.com/Divina-s/zuriinternship'
    status_code = 200
    if None in [slack_name, utc_time, track,github_file_url,github_repo_url,current_day]:
        return JsonResponse ({'error':'Missing required fields'}, status=400)
    try:
        status_code= int(request.GET.get('status_code','200'))
        if not (100 <= status_code <= 599):
            raise ValueError()
    except ValueError:
        return JsonResponse({'error':'Invalid status code'}, status=400)
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
