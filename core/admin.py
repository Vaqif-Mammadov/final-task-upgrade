from django.contrib import admin
from .models import Social,Service,Consultant,Serv,Praise,New,Slickbox,Plan,Sponsor,Contact,Reply,User_contact,FAQQuestion,Answer,NewsletterMessage

# homeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display=('name','image','link','active')

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
    list_display=('name_lastname','title','category','category2','history')

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


# BLOGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
@admin.register(NewsletterMessage)
class NewsletterMessageAdmin(admin.ModelAdmin):
    list_display=('user','subject','message')

# BLOGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG


# PRICINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
@admin.register(User_contact)
class User_contactAdmin(admin.ModelAdmin):
    list_display=('name','phone')


@admin.register(FAQQuestion)
class FAQQuestionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'message','phone', 'count', 'created_at')
    search_fields = ('name', 'email','phone', 'message')
    list_filter = ('count',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_text', 'created_at')
    search_fields = ('question__name', 'answer_text')
    list_filter = ('created_at',)

# PRICINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG

# SİNGLEPOST111111111111111111111111111111111111111111111111111111111111111
@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display=('user','comment','created_at')





# SİNGLEPOST111111111111111111111111111111111111111111111111111111111111111