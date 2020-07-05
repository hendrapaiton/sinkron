from time import sleep

from celery import task, current_task


@task()
def do_work():
    total = 102
    for i in range(1, total):
        sleep(0.25)
        current_task.update_state(state='PROGRESS', meta={'current': i, 'total': total - 2})
