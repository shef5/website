from django.contrib import admin

# Register your models here.
from .forms import URLform
from .models import URL

class Inputurl(admin.ModelAdmin):
	list_display = ["__str__", "timestamp", "updated"]
	class Meta:
		model = URL

admin.site.register(URL, Inputurl)