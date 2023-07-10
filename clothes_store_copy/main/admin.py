from django.contrib import admin
from .models import Season, Clothes, Size, Availability, Review, User

# Register your models here.

admin.site.register(Season)
admin.site.register(Clothes)
admin.site.register(Size)
admin.site.register(Availability)
admin.site.register(Review)
admin.site.register(User)