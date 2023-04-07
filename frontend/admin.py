from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from frontend.mail_template import mail_template
from .models import User
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view

# Register your models here.

class UserAdmin(ImportExportModelAdmin,ExtraButtonsMixin,admin.ModelAdmin):
    @button(html_attrs={'style': 'background-color:#DC6C6C;color:black'})
    def send_mails(self, request):
        def _action(request):
                users = User.objects.all()
                print(mail_template)
                for usr in users:
                    file = open("emails/{}".format(usr.email), "w")
                    file.write(mail_template.replace("<lien>","http://localhost:8000/user/{}".format(usr.token)))
                    file.close()

        return confirm_action(self, request, _action, "Confirm action",
                          "Successfully executed", )
    list_display = ['email','link_opened','compromised','token']
    

admin.site.register(User,UserAdmin)