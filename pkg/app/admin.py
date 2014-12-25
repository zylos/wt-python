from django.contrib import admin
from app.models import Tag, Group, License, Resource, DataSet
from app.models import DataSetResource, DataSetExtra, DataSetRating

class DataSetExtraInline(admin.TabularInline):
    model = DataSetExtra
    extra = 3

class DataSetRatingInline(admin.TabularInline):
    model = DataSetRating
    extra = 3

class DataSetResourceInline(admin.TabularInline):
    model = DataSetResource
    extra = 1

class DataSetAdmin(admin.ModelAdmin):
    list_display = ('title', 'version')
    list_filter = ('set_type', 'activity_state', 'tags')
    search_fields = ('title', 'url_name', 'notes')
    inlines = [ DataSetExtraInline, 
                DataSetRatingInline, 
                DataSetResourceInline ]

class TagAdmin(admin.ModelAdmin):
    search_fields = ('name', )

class LicenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'license_type')

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_size', 'file_type')
    list_filter = ('group', 'file_type')

# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Group)
admin.site.register(License, LicenseAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(DataSet, DataSetAdmin)
