from django.contrib import admin
from .models import Subject, AcademicLevel, Axis, Post

from admin_auto_filters.filters import AutocompleteFilterFactory

# Model admins
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_per_page = 10
    search_fields = ['name']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id',)
        return ()

class AcedemicLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_per_page = 10
    search_fields = ['name']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id',)
        return ()

class AxisAdmin(admin.ModelAdmin):
    list_display = ('name', 'id','subject__name')
    list_per_page = 10
    search_fields = ['name']

    # Automcomplete select form
    autocomplete_fields = ['subject']

    list_filter = [
        # Filter select with search
        AutocompleteFilterFactory('Subject', 'subject'),
    ]

    def subject__name(self, obj):
        return obj.subject.name

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id',)
        return ()

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'academic_level', 'subject', 'axis', 'id')
    exclude = ('image',)
    list_per_page = 10

    search_fields = ['title']
    
    # Automcomplete select form
    autocomplete_fields = ['user', 'academic_level', 'axis']

    # Filters
    list_filter = [
        # Filter select with search
        AutocompleteFilterFactory('User', 'user'),
        AutocompleteFilterFactory('Academic level', 'academic_level'),
        AutocompleteFilterFactory('Axis', 'axis'),
        AutocompleteFilterFactory('Subject', 'axis__subject'),
    ]


    def subject(self, obj):
        return obj.axis.subject.name
    
    # def total_likes(self, obj):
    #     return obj.likes.count()
    
    # def total_views(self, obj):
    #     return obj.views.count()
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('id', 'created_at', 'updated_at', 'total_likes', 'total_views')
        return ()

# Register your models here.
admin.site.register(Subject, SubjectAdmin)
admin.site.register(AcademicLevel, AcedemicLevelAdmin)
admin.site.register(Axis, AxisAdmin)
admin.site.register(Post, PostAdmin)
