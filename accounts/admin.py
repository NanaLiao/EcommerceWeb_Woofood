from django.contrib import admin
from accounts.models import UserProfile

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','city','phone','website','user_info')
#
#     def user_info(self,obj):
#         return obj.description
#
#     user_info.short_description = 'INFO'
#
#     def get_queryset(self,request):  #we inherit from admin.ModelAdmin, we can override the method
#         queryset = super(UserProfileAdmin,self).get_queryset(request)
#         queryset = queryset.order_by('phone') # we can have many arguments here, for examle, if the table has 2 same phone number, then we can add one more filter like user: queryset.order_by('phone','user')
#         return queryset



admin.site.register(UserProfile)
