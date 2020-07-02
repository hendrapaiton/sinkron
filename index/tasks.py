from sinkron.celery import app


@app.task(name='pertambahan')
def add(a, b):
    return a + b
