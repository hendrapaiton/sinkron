# SINKRON
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
where status is asynchronous using django application

## Technologies
* Django - version 3.0.8
* Celery - version 4.4.6
* Redis - version 5.0.9

## Setup
Before you setup the project you must clone this project and installing
redis server where you can download at [redis.io](https://redis.io/download). 
And for windows you can download old version at [tporadowski](https://github.com/tporadowski/redis/releases).

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
$ source venv/bin/activate
```
In your cloning project in local machine
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
>>> res = add.delay(1,2)
>>> print(res.state) # 'SUCCESS'
>>> print(res.info) # 3
```

## Features
List features ready
* Simple task using celery and get the data from the task

To-do list :
* Task to make counter range from 0 to 100 using task in celery
* Making endpoint in django where can access from http by the client
* Making function javascript to get data from django and presenting progress bar


## Inspiration
Project is inspired by [Celery Tutorial](https://medium.com/swlh/python-developers-celery-is-a-must-learn-technology-heres-how-to-get-started-578f5d63fab3)
and [Celery Progress Bar](https://buildwithdjango.com/blog/post/celery-progress-bars/)

## Contact
Created by [@hendrapaiton](https://github.com/hendrapaiton)
