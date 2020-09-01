from django.contrib import admin
from reminderlist import models

# Register your models here.
admin.site.register([
    models.Todolist,
    models.Like,
    models.Comment,
])