from django.contrib import admin

from .models import User, ReportedCases

admin.site.register(User)
admin.site.register(ReportedCases)
