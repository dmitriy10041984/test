from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields

# const
SHORT_TEXT_LEN=1000
# Create your models here. Здесь можно создавать модели
class Article(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    user=models.ForeignKey(User)
    date=models. DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_short_text(self):
        # если длина текста больше 1000, то обрезаем, а если нет - возвращаем как есть
        if len(self.text)>SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text



# Create your models here.
class Client(models.Model):
    SEX_SELECT = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )

    surename=models.CharField(max_length=50,verbose_name="Фамилия")
    name=models.CharField(max_length=50,verbose_name="Имя")
    secondname=models.CharField(max_length=50,verbose_name="Отчество")
    sex = models.CharField(max_length=1, choices=SEX_SELECT,verbose_name="Пол")
    birthday=models.DateField(verbose_name="Дата рождения")

    class Meta:
        ordering = ['surename','name','secondname']
        db_tablespace='DEFAULT_TABLESPACE'
        unique_together=(("surename","name"))
        verbose_name_plural = "Данные о клиентах"


    def __str__(self):
        return self.surename

class Category(models.Model):
    title_cat=models.CharField(max_length=100,unique=True,verbose_name="Название категории")
    text_cat=models.TextField(verbose_name="Описание категории")

    class Meta:
        ordering=['title_cat']
        db_table = 'Category_of_Request'
        get_latest_by = "order_date"
        verbose_name_plural = "Категории"
        #
        managed=True
        required_db_features=['gis_enabled']
        required_db_vendor=['sqlite']
        select_on_save=False

    def __str__(self):
        return self.title_cat


class ClientRequests(models.Model):
    number_of_request=models.PositiveIntegerField(unique=True,verbose_name="Номер заявки")
    client=models.ForeignKey(Client, on_delete=models.CASCADE,verbose_name="Клиент")
    category=models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="Принадлежность заявки к категории")
    create_request=models.DateTimeField(auto_now_add=True,verbose_name="Время и дата создания заявки")
    modify_request=models.DateTimeField(verbose_name="Время и дата изменение заявки")
    delete_request=models.DateTimeField(verbose_name="Время и дата удаления заявки")

    class Meta:
        abstract=True
        order_with_respect_to = 'number_of_request'
        default_permissions=('add','change')
        required_db_vendor='sqlite'
        index_together=[
            ["number_of_request","client_name","category"]
        ]

    def __str__(self):
        return self.client_name


class Request_of_laboratory(ClientRequests):
    laboratory_title=models.CharField(max_length=100,verbose_name="Название лаборатории")

    class Meta:
        verbose_name_plural="Заявки лабораторий"

    def __str__(self):
        return self.laboratory_title

class Request_of_medcenter(ClientRequests):
    medcenter_title=models.CharField(max_length=100,verbose_name="Название медицинского центра")

    class Meta:
        verbose_name_plural = "Заявки медцентров"

    def __str__(self):
        return self.medcenter_title

class Delivery(Request_of_medcenter):
    DELIVERY_SELECT = (
        ('S', 'Самовывоз'),
        ('K', 'Курьер'),
        ('N', 'Неопределен'),
    )
    address=models.TextField(verbose_name="Адрес получателя")
    delivery_variant=models.CharField(max_length=1,choices=DELIVERY_SELECT,verbose_name="Вариант доставки")
    delivery_date=models.DateTimeField(verbose_name="Дата и время доставки")

    class Meta:
        verbose_name_plural = "Доставки"

    def __str__(self):
        return self.medcenter_title


class XMLClient(Client):
    class Meta:
        ordering=['surename']
        proxy=True

    def get_xml(self):
        return "Расширение класса"



class AllFieldMethod(models.Model):
    #field1=models.AutoField()
    field2=models.BigIntegerField()
    field3=models.BinaryField()
    field4=models.BooleanField()
    field5=models.CharField(max_length=100)
    field6=models.CommaSeparatedIntegerField(max_length=6)
    field7=models.DateField()
    field8=models.DateTimeField()
    field9=models.DecimalField(max_digits=6,decimal_places=6)
    field10=models.DurationField()
    field11=models.EmailField()
    field12=models.FileField()
    field13=models.FilePathField()
    field14=models.FloatField()
    field15=models.ImageField()
    field16=models.IntegerField()
    field17=models.GenericIPAddressField()
    field18=models.NullBooleanField()
    field19=models.PositiveIntegerField()
    field20=models.PositiveSmallIntegerField()
    field21=models.SlugField()
    field22=models.SmallIntegerField()
    field23=models.TextField()
    field24=models.TimeField()
    field25=models.URLField()
    field26=models.UUIDField()
    field27=models.ForeignKey(Client,on_delete=models.CASCADE)
    field28=models.ManyToManyField(Category)
    field29=models.OneToOneField(Article)


#for examples
class Blog1(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author1(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()


class Entry1(models.Model):
    blog1 = models.ForeignKey(Blog1)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    authors1 = models.ManyToManyField(Author1)


