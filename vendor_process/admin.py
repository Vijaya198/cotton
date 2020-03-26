

from django.contrib import admin

# Register your models here.
from .models import vendor_information, user_info, user_address, state
#from django.contrib.auth.models import User


admin.site.register(vendor_information)
admin.site.register(user_info)
admin.site.register(user_address)
admin.site.register(state)
#admin.site.register(User)
# Register your models here.




