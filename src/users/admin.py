from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from default.admin import admin
from users.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    pass
