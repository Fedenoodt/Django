from django.contrib import admin
from .models import Achiever, Achievement, Comment, Level, Relation



class AchieverAdm(admin.ModelAdmin):
	list_display = ('Vinculation', 'Names', 'Surnames', 'Description', 'Profile_Pictures', 'FK_Level', 'FK_Following')
	search_fields = ('Names', 'Surnames', 'Description', 'Profile_Pictures', 'FK_Level', 'FK_Following')
	
	
admin.site.register(Achiever, AchieverAdm)
	
	
class AchieveAdm(admin.ModelAdmin):
	list_display = ('Achievements', 'FK_Achiever')
	search_fields = ('Achievements', 'FK_Achiever')
	
	
admin.site.register(Achievement, AchieveAdm)
	
	
class CommentAdm(admin.ModelAdmin):
	list_display = ('Comments', 'FK_Achiever', 'FK_Achievement')
	search_fields = ('Comments', 'FK_Achiever', 'FK_Achievement')
	
	
admin.site.register(Comment, CommentAdm)
	
	
class LevelAdm(admin.ModelAdmin):
	list_display = ('Names', 'Unlocked', 'FK_Achiever')
	search_fields = ('Names', 'Unlocked', 'FK_Achiever')
	
	
admin.site.register(Level, LevelAdm)



class RelationAdm(admin.ModelAdmin):
	list_display = ('FK_Achiever', 'FK_Follower', 'FK_Following')
	
	
admin.site.register(Relation, RelationAdm)
