from time import sleep

from celery import current_task

from sinkron import app


@app.task(typing=False)
def do_work():
    total = 102
    for i in range(1, total):
        sleep(0.25)
        current_task.update_state(state='PROGRESS', meta={'current': i, 'total': total - 2})
