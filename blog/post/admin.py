from django.contrib import admin
from.models import Post, Contact

class PostAdmin(admin.ModelAdmin):
    list_display=('Title','Date','Image','Content')

class ContactAdmin(admin.ModelAdmin):
    list_display=('Your_Name','Email_Address','Phone','Subject','Your_Message')

admin.site.register(Post,PostAdmin)
admin.site.register(Contact, ContactAdmin)