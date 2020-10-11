from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from app.admin import admin
from users.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    pass
