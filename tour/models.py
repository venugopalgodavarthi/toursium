from django.db import models

# Create your models here.


class countrymodel(models.Model):
    couid = models.CharField(primary_key=True, max_length=30)
    cname = models.CharField(max_length=30,)
    cimg = models.ImageField(upload_to='country/',)

    def __str__(self):
        return self.cname


class statemodel(models.Model):
    stateid = models.CharField(primary_key=True, max_length=30)
    sname = models.CharField(max_length=30)
    simg = models.ImageField(upload_to='state/')
    couid = models.ForeignKey(countrymodel, on_delete=models.CASCADE)

    def __str__(self):
        return self.sname


class citymodel(models.Model):
    cityid = models.CharField(primary_key=True, max_length=30)
    ciname = models.CharField(max_length=30)
    cimg = models.ImageField(upload_to='state/')
    desc = models.TextField()
    stateid = models.ForeignKey(statemodel, on_delete=models.CASCADE)

    def __str__(self):
        return self.ciname


class citydetails(models.Model):
    cityid = models.ForeignKey(citymodel, on_delete=models.CASCADE)
    citydesc = models.TextField()
    citywikipedia = models.URLField()
    cityyoutube = models.URLField()

    def __str__(self):
        return str(self.cityid)


class citygallary(models.Model):
    gid = models.BigAutoField(primary_key=True)
    citydetails = models.ForeignKey(citydetails, on_delete=models.CASCADE)
    gimg = models.ImageField(upload_to='citygallary/')
