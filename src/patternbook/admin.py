from django.contrib import admin

# Register your models here.
from .models import SignUp


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
        #fields = ('full_name', 'timestamp')
        list_display = ('__unicode__', 'full_name', 'timestamp',)
        model = SignUp


#admin.site.register(SignUp)