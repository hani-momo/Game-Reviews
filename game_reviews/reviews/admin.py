from django.contrib import admin

# Register your models here.
from .models import Game, UserProfile

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date')
    search_fields = ('title', 'genre')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

admin.site.register(Game, GameAdmin)
admin.site.register(UserProfile, UserProfileAdmin)