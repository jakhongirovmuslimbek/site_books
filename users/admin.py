from django.contrib import admin
from .models import UsersModel, ApiUserModel

admin.site.register(UsersModel)
admin.site.register(ApiUserModel)
