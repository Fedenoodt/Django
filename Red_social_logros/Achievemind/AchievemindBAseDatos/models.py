from django.db import models

class User(models.Model):
	Names = models.CharField(max_length=35)
	Surnames = models.CharField(max_length=35)
	Email = models.CharField(max_length=300)
	Password = models.CharField(max_length=80)
	Description = models.CharField(max_length=200)
	Profile_Pictures = models.ImageField(upload_to='ProfilePictures')
	FK_Level = models.ForeignKey('Level', on_delete=models.CASCADE)
	FK_Following = models.ForeignKey('Relation', on_delete=models.CASCADE)

	
	
	
class Achievement(models.Model):
	Achievements = models.CharField(max_length=250)
	FK_User = models.ForeignKey('User', on_delete=models.CASCADE)
	
	
	
class Comment(models.Model):
	Comments = models.CharField(max_length=300)
	FK_Achievement = models.ForeignKey('Achievement', on_delete=models.CASCADE)
	FK_User = models.ForeignKey('User', on_delete=models.CASCADE)
	
	
	
class Level(models.Model):
	Names = models.CharField(max_length=300)
	Unlocked = models.CharField(max_length=300)
	FK_User = models.ForeignKey('User', on_delete=models.CASCADE)
	
	
	
	
class Relation(models.Model):
	FK_User = models.ForeignKey('User', related_name='User', on_delete=models.CASCADE)
	FK_Following = models.ForeignKey('User', related_name='Following', on_delete=models.CASCADE)
	FK_Follower = models.ForeignKey('User', related_name='Follower', on_delete=models.CASCADE)
