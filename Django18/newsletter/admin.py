from django.contrib import admin
from .models import SignUp


# Register your models here.


class SignupModel(admin.ModelAdmin):
    list_display = ["__str__", "fullname", "timestamp", "updated"]
    list_filter = ["updated"]

    class Meta:
        model = SignUp


admin.site.register(SignUp, SignupModel)
