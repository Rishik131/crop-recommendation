from django.db import models
class snippet(models.Model):
    district = models.CharField(max_length=30)
    village = models.CharField(max_length=30,null=True)
    pH = models.CharField(max_length=30)
    moisture = models.CharField(max_length=30)
    nitrogen = models.CharField(max_length=30,null=True)
    phosphorus = models.CharField(max_length=30,null=True)
    zinc = models.CharField(max_length=30,null=True)
    potassium = models.CharField(max_length=30,null=True)
    iron = models.CharField(max_length=30,null=True)
    copper = models.CharField(max_length=30,null=True)
    def _str_(self):
        return self.district