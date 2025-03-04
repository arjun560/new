from django.contrib import admin
from .models import Test
admin .site.register(Test)


from .models import Destination
admin.site.register(Destination)
# Register your models here.
