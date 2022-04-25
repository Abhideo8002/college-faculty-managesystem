
# from msilib.schema import Media
from django.db import models

class Type (models.Model):
 

    title= models.CharField(
        max_length = 20,
        default = '1'
        )

    def __str__(self):
       return "%s" %(self.title)
   
class Specialization (models.Model):
    special= models.CharField(
        max_length = 20,
        
        default = '1'
        )

    def __str__(self):
       return "%s" %(self.special)
        

class Document (models.Model):
    # document= models.FileField(default='')
    document = models.FileField(upload_to='Media/')

    discription= models.CharField(max_length=200, default='')

    # def __str__(self):
    #    return "%s %s" %(self.document, self.discription)

class Faculty (models.Model):
    name= models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    special=models.CharField(max_length=10)
    document=models.FileField(max_length=100)
    type = models.ForeignKey(Type , on_delete= models.CASCADE ,null = True ,blank= True)
    specialization  = models.ManyToManyField(Specialization ,null= True ,blank= True) 
    

    def __str__(self):
        return "%s %s %s" %(self.name, self.phone, self.document)
   




