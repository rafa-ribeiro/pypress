from os import environ

bind = "127.0.0.1:7000"
workers = 3
timeout = 90
reload = True
debug = True

# Selenium Config
environ.setdefault('SELENIUM_HOST', "http://127.0.0.1:4444/wd/hub")
environ.setdefault('CELERY_BROKER', "redis://localhost:6379/0")
environ.setdefault('CELERY_BACKEND', "redis://localhost:6379/0")
