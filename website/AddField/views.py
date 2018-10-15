# -*- coding: utf-8 -*-
from django.db import models
from .models import Person
from .models import AddPerson
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.files.storage import FileSystemStorage
from PIL import Image
import sys

# Create your views here.
def index(request):
	context = {
		"Person" : Person.objects.all(),
		"AddPerson" : AddPerson.objects.all()
	}
	return render(request,"AddField/index.html",context)

def editView(request,PID):
	person = Person.objects.filter(id=PID).all()
	context = {
	'Person' : person
	}
	boo = []
	addperson = AddPerson.objects.filter(AddID_id=PID).all()
	if addperson is not None:
		for addperson in addperson:
			html = "<input type='text'class='fieldname'id='ExtendedAddress'name='Array'value='%s'><input type='hidden'class='fieldname'id='AddID_id'name='Id'value='%s'>" %(addperson.ExtendedAddress,addperson.id)
			boo.append(html)
		context = {
		"list" : boo,
		'Person' : person,
		}    
		return render(request,"AddField/Edit.html", context)
	else:
		return render(request,"AddField/Edit.html",context)

def createPerson(request):
	if request.method == 'POST':
		if request.POST.get('PID'):
			person = Person.objects.filter(id =request.POST.get('PID')).all()
			for person in person: 
				person.FirstName= request.POST.get('FirstName')
				person.LastName= request.POST.get('LastName')
				person.PhoneNo= request.POST.get('PhoneNo')
				person.Address= request.POST.get('Address')
				person.save()
				addperson = AddPerson.objects.filter(AddID_id = request.POST.get('PID')).delete()
				a = request.POST.getlist('Array')
				for i in a:
					if i == '':
						pass
					else:
						addperson = AddPerson()
						addperson.ExtendedAddress = i
						addperson.AddID_id = person.id
						addperson.save()
			return render(request,"AddField/New.html")
		person = Person()
		if 'myfile' in request.FILES:
			myfile = request.FILES['myfile']
			img = Image.open(myfile)
			size = sys.getsizeof(img.tobytes())
			while size > 2000000:
				width, height = img.size
				img = img.resize((int(width/2),int(height/2)), Image.ANTIALIAS)
				size = sys.getsizeof(img.tobytes())
				myfile.seek(0)
				myfile.truncate()
				img.save(myfile)
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)
			str1 = request.POST.get('FirstName')
			str2 = request.POST.get('LastName') 
			person.FileName = "%s%s'sPicture.jpeg"%(str1,str2)
			person.URL = uploaded_file_url
		person.FirstName= request.POST.get('FirstName')
		person.LastName= request.POST.get('LastName')
		person.PhoneNo= request.POST.get('PhoneNo')
		person.Address= request.POST.get('Address')
		person.save()
		ID = person.id
		a = request.POST.getlist('Array')
		for i in a:
			if i == '':
				pass
			else:
				addperson = AddPerson()
				addperson.ExtendedAddress = i
				addperson.AddID_id = person.id
				addperson.save()
		return render(request,"AddField/New.html")
	else:
		return render(request,"AddField/New.html")

def delete_person(request, ID):
	Person.objects.get(id=ID).delete()
	context = {
	"Person" : Person.objects.all(),
	"AddPerson" : AddPerson.objects.all()
	}
	return render(request,"AddField/index.html",context)

def uploadView(request):
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    return render(request, 'AddField/Edit.html', {
        'uploaded_file_url': uploaded_file_url
    })


