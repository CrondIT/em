from django.db import models

class TimeStamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Events(TimeStamp):
    title = models.CharField('Название', max_length=200, default='Новое мероприятие')
    print_title = models.TextField('Название для печати')
    description = models.TextField('Описание') 
    from_date = models.DateField('Дата начала')
    to_date = models.DateField('Дата окончания')
    
    
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
