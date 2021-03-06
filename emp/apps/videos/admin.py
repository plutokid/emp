from django.contrib import admin
from emp.apps.videos.models  import Video, VideoCategory, VideoPlaylist

class VideoAdmin(admin.ModelAdmin):
	list_display   = ('title', 'uploader', 'upload_datetime', 'length', 'views', 'codec', 'src_codec')
	list_filter    = ('upload_datetime', 'nsfw', 'codec', 'categories')
	search_fields  = ('title', 'categories',) # todo: implement proper tag search

	date_hierarchy = 'upload_datetime'

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoCategory)
admin.site.register(VideoPlaylist)