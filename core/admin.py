from django.contrib import admin
from .models import Service,Consultant,Serv,Praise,New,Slickbox,Plan,Sponsor,Contact

# homeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
@admin.register(Serv)
class ServAdmin(admin.ModelAdmin):
    list_display=('title','description')

@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display=('name','title','description')

@admin.register(Praise)
class PraisesAdmin(admin.ModelAdmin):
    list_display=('name_lastname','title','description')

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display=('name_lastname','title','category','history')

# homeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

# HOME222222222222222222222222222222222222222222222222222
@admin.register(Slickbox)
class SlickboxAdmin(admin.ModelAdmin):
    list_display=('title','description')

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display=('name','price_monthly','price_yearly','my_list')


# HOME222222222222222222222222222222222222222222222222222


@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display=('name','last_name','occupation')



#    SERVICEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display=('logo',)

#    SERVICEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE


# CONTACTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','tel1','mail1','adress1')


# CONTACTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT