from django.contrib import admin
from .models import User, Achievement, Comment, Level, Relation

class UserAdm(admin.ModelAdmin):
	list_display = ('Names', 'Surnames', 'Description', 'Profile_Pictures', 'FK_Level', 'FK_Following')
	search_fields = ('Names', 'Surnames', 'Description', 'Profile_Pictures', 'FK_Level', 'FK_Following')
	
	
admin.site.register(User, UserAdm)
	
	
class AchieveAdm(admin.ModelAdmin):
	list_display = ('Achievements', 'FK_User')
	search_fields = ('Achievements', 'FK_User')
	
	
admin.site.register(Achievement, AchieveAdm)
	
	
class CommentAdm(admin.ModelAdmin):
	list_display = ('Comments', 'FK_User', 'FK_Achievement')
	search_fields = ('Comments', 'FK_User', 'FK_Achievement')
	
	
admin.site.register(Comment, CommentAdm)
	
	
class LevelAdm(admin.ModelAdmin):
	list_display = ('Names', 'Unlocked', 'FK_User')
	search_fields = ('Names', 'Unlocked', 'FK_User')
	
	
admin.site.register(Level, LevelAdm)



class RelationAdm(admin.ModelAdmin):
	list_display = ('FK_User', 'FK_Follower', 'FK_Following')
	
	
admin.site.register(Relation, RelationAdm)
