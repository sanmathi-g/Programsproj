from django.db import models

# Create your models here.

class ProgCategory(models.Model):
    Category_title = models.CharField(max_length=50)
    Category_summary = models.CharField(max_length=200)
    Category_slug = models.CharField(max_length=100)

    class Meta:
        verbose_name ="Categories"

    def __str__(self):
        return self.Category_title


class ProgSeries(models.Model):
    prog_series = models.CharField(max_length=50)
    Category_title = models.ForeignKey(ProgCategory,default = 1,verbose_name= "Category" , on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name ="Series"

    def __str__(self):
        return self.prog_series


class programs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField
    date = models.DateTimeField(auto_now_add=True)
    prog_series = models.ForeignKey(ProgSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    prog_slug = models.CharField(max_length=100, default=1)



    def __str__(self):
        return self.title

