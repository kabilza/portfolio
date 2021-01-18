from django.db import models
from datetime import datetime
import datetime as dt

myDate = datetime.now()
formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")

# Create your models here.

class Info(models.Model):
    """User's Info"""
    gender = models.CharField('Gender (F or M)', max_length=1)
    birthday = models.DateField(null=True, blank=True)
    brief_info = models.TextField('Background Infomation', default="NOT SET")
    phone_num = models.CharField('Phone Number', max_length=10, default="NOT SET")
    twitter = models.TextField('Twitter', default="NOT SET")

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        return int((dt.date.today() - self.birthday).days/365.25)

    def get_gender(self):
        return self.gender

    def get_brief_info(self):
        return self.brief_info

    def get_number(self):
        return self.phone_num

class Projects(models.Model):
    """User's past projects and works"""
    project_name = models.TextField('Project Name', default="NOT SET")
    project_info = models.TextField('Project Info', default="NOT SET")
    date_created = models.TextField('Date', default="NOT SET")

class ContactMe(models.Model):
    """Received Contact Info from the web"""
    email = models.TextField('Email', default="NOT SET")
    subject = models.TextField('Subject', default="NOT SET")
    message = models.TextField('Message', default="NOT SET")