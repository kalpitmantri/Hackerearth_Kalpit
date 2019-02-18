from django.db import models

class Wines(models.Model):
	country = models.CharField(max_length=100,blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	designation = models.CharField(max_length=200,blank=True,null=True)
	points = models.IntegerField(blank=True,null=True)
	price = models.IntegerField(blank=True,null=True)
	province = models.CharField(max_length=100,blank=True,null=True)
	region_1 = models.CharField(max_length=100,blank=True,null=True)
	region_2 = models.CharField(max_length=100,blank=True,null=True)
	variety = models.CharField(max_length=150,blank=True,null=True)
	winery	= models.CharField(max_length=150,blank=True,null=True)

	def __str__(self):
		return str(self.id)		

	def snippet(self):
		return self.description[0:150] + '...'