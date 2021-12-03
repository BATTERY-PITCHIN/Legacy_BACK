from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Founder)
admin.site.register(FactoryOwner)
admin.site.register(ContactUsers)
admin.site.register(FounderEstimate)
admin.site.register(FactoryInformation)
admin.site.register(KeywordList)