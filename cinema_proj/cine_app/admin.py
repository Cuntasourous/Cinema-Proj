from django.contrib import admin
from cine_app.models import Genre, Movie_list, timeslots, book3
from cine_app.models import UserProfileInfo
# Register your models here.

admin.site.register(Genre)
admin.site.register(Movie_list)
admin.site.register(book3)
admin.site.register(timeslots)
#admin.site.register(UserProfileInfo)