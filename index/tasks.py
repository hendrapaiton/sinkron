from time import sleep

from celery import task, current_task


@task()
def do_work():
    total = 100
    for i in range(1, total):
        sleep(1.0)
        current_task.update_state(state='PROGRESS', meta={'current': i, 'total': total})
