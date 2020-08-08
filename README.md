# SINKRON ![Django CI](https://github.com/hendrapaiton/sinkron/workflows/Django%20CI/badge.svg)
> Simple Django Celery Example

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General Info
This project has a simple goal which is to create a progress bar 
where status is asynchronous using django application, celery and redis.

## Technologies
* Django - version 3.1
* Celery - version 4.4.7
* Redis - version 3.5.3

## Setup
Before you setup the project you must clone this project and installing
redis server where you can download at [redis.io](https://redis.io/download), 
and for windows you can download old version redis at [tporadowski](https://github.com/tporadowski/redis/releases).

#### Clone
Clone this repo to your local machine 
```
$ git clone https://github.com/hendrapaiton/sinkron.git
```

#### Installation
Making virtual environment for the project
```
$ cd sinkron
$ pip install virtualenv
$ virtual venv
$ source venv/bin/activate # On linux
$ .\venv\Scripts\activate # on Windows
```
Installing Django, Celery and Redis Library for Python
```
$ pip install -r requirements.txt
```
Run the project
```
$ python manage.py runshell
```
Run the celery
```
$ celery -A sinkron worker -l info
```
__Notes__ : Add arguments `--pool=solo` if you using Windows 10

#### Testing
In python console
```
>>> from index.tasks import add
>>> job = do_work.delay(1,2)
>>> print(job.info) 
{'current': 3, 'total': 100} # None if state is success
>>> print(job.state) 
PROGRESS # state is 'SUCCESS' if job is finished
```

## Features
- [x] Simple task using celery and get the data from the task
- [x] Task to make counter range from 1 to 100 using task in celery
- [x] Making endpoint in django where can access from http by the client
- [x] Making function javascript to get data from django and presenting progress bar


## Inspiration
Project is inspired by [Celery Tutorial](https://medium.com/swlh/python-developers-celery-is-a-must-learn-technology-heres-how-to-get-started-578f5d63fab3)
and [Celery Progress Bar](https://buildwithdjango.com/blog/post/celery-progress-bars/)

## Contact
Created by [@hendrapaiton](https://github.com/hendrapaiton)
