######### IMPORTS ########
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from frontend.mail_template import *
from .models import User
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from django.db.models.functions import TruncDay
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json

######### Main Class ##########

class UserAdmin(ImportExportModelAdmin,ExtraButtonsMixin,admin.ModelAdmin):
    # Create the send mail buttons for the 3 different websites
    @button(html_attrs={'style': 'background-color:#DC6C6C;color:black'})
    def send_netflix_emails(self, request):
        def _action(request):
                users = User.objects.all()
                for usr in users:
                    file = open("emails/{}".format(usr.token), "w")
                    file.write(mail_template_netflix.replace("<lien>","http://localhost:8000/app/netflix/{}".format(usr.token)))
                    file.close()

        return confirm_action(self, request, _action, "Confirm action",
                          "Successfully executed", )
    # Amazon
    @button(html_attrs={'style': 'background-color:#886A6C;color:black'})
    def send_amazon_emails(self, request):
        def _action(request):
                users = User.objects.all()
                for usr in users:
                    file = open("emails/{}".format(usr.token), "w")
                    file.write(mail_template_amazon.replace("<lien>","http://localhost:8000/app/amazon/{}".format(usr.token)))
                    file.close()

        return confirm_action(self, request, _action, "Confirm action",
                          "Successfully executed", )
    # GitHub
    @button(html_attrs={'style': 'background-color:#886A10;color:black'})
    def send_github_emails(self, request):
        def _action(request):
                users = User.objects.all()
                for usr in users:
                    file = open("emails/{}".format(usr.token), "w")
                    file.write(mail_template_github.replace("<lien>","http://localhost:8000/app/github/{}".format(usr.token)))
                    file.close()

        return confirm_action(self, request, _action, "Confirm action",
                          "Successfully executed", )

     # Creating the report charts
    def changelist_view(self, request, extra_context=None):
        #Getting the values
        link_opened = (
            User.objects.filter(link_opened=True).count()
        )
        
        compromised = (
            User.objects.filter(compromised=True).count()
        )

        reported = (
            User.objects.filter(has_reported=True).count()
        )

        total_users = (
            User.objects.all().count()
        )
        # Serialize and attach the chart data to the template context
        as_json = json.dumps([link_opened,compromised,reported], cls=DjangoJSONEncoder)
        as_json2 = json.dumps(total_users, cls=DjangoJSONEncoder)
        extra_context = extra_context or {"stats_data": as_json,"total_users": total_users}
        
        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
    
    # Display the list of users from db
    list_display = ['email','link_opened','compromised','has_reported']
    
# Register the models
admin.site.register(User,UserAdmin)