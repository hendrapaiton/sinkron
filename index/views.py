import json

from celery.result import AsyncResult
from django.http import HttpResponse
from django.shortcuts import render

from index.tasks import do_work


def index(request):
    job = do_work.delay()
    return render(request, 'index.html', {'task': job.id})


def progress(request, task):
    job = AsyncResult(task)
    res = {
        'state': job.state,
        'info': job.info
    }
    return HttpResponse(json.dumps(res), content_type='application/json')
