from django.db import models

# Create your models here.
class Person(models.Model):
	FirstName = models.CharField(max_length=64)
	LastName = models.CharField(max_length=64)
	PhoneNo = models.CharField(max_length=10)
	Address = models.CharField(max_length=100)
	FileName = models.CharField(max_length=100, default=None)
	URL = models.CharField(max_length = 100, default=None)
	# def __str__(self):
	# 	return f"{self.FirstName} {self.LastName}, living in {self.Address}, Contact No :  {self.PhoneNo}"

class AddPerson(models.Model):
	ExtendedAddress = models.CharField(max_length=100)
	AddID = models.ForeignKey(Person, on_delete=models.CASCADE)
	
	# def __str__(self):
	# 	return f"Extended Addres: {self.ExtendedAddress}, Add ID : {self.AddID_id}"

