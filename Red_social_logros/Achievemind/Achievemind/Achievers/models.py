from django.db import models
from django.contrib.auth.models import User

class Achiever(models.Model):
	Vinculation = models.OneToOneField(User, on_delete=models.CASCADE)
	Names = models.CharField(max_length=35)
	Surnames = models.CharField(max_length=35)
	BirthDay = models.DateField()
	Description = models.CharField(max_length=200)
	EMail = models.CharField(max_length=140)
	Profile_Pictures = models.ImageField(upload_to='ProfilePictures')
	FK_Level = models.ForeignKey('Level', on_delete=models.CASCADE)
	FK_Following = models.ForeignKey('Relation', on_delete=models.CASCADE)

	
	
	
class Achievement(models.Model):
	Achievements = models.CharField(max_length=250)
	FK_Achiever = models.ForeignKey('Achiever', on_delete=models.CASCADE)
	
	
	
class Comment(models.Model):
	Comments = models.CharField(max_length=300)
	FK_Achievement = models.ForeignKey('Achievement', on_delete=models.CASCADE)
	FK_Achiever = models.ForeignKey('Achiever', on_delete=models.CASCADE)
	
	
	
class Level(models.Model):
	Names = models.CharField(max_length=300)
	Unlocked = models.CharField(max_length=300)
	FK_Achiever = models.ForeignKey('Achiever', on_delete=models.CASCADE)
	
	
	
	
class Relation(models.Model):
	FK_Achiever = models.ForeignKey('Achiever', related_name='Achiever', on_delete=models.CASCADE)
	FK_Following = models.ForeignKey('Achiever', related_name='Following', on_delete=models.CASCADE)
	FK_Follower = models.ForeignKey('Achiever', related_name='Follower', on_delete=models.CASCADE)
