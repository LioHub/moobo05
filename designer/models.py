from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	JOB_CHOICES = (
		('Исполнитель', 'Исполнитель'),
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
	# first_name = models.CharField(max_length=20, verbose_name='Имя')
	# last_name = models.CharField(max_length=20, verbose_name='Фамиля')
	number = models.CharField(max_length=20, verbose_name='Номер телефона')
	# email = models.EmailField(max_length=50, verbose_name='Почта')
	quantity_of_workers = models.IntegerField(
    	verbose_name='Количество работников', default=0)
	job = models.CharField(verbose_name='Профессия', max_length=20, choices=JOB_CHOICES)
	city = models.CharField(verbose_name='Город', max_length=30, blank=True)
	# login = models.CharField(verbose_name='Логин', max_length=50)
	# passwd = models.CharField(verbose_name='Пароль', max_length=100)

	def __str__(self):
		return self.user

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Project(models.Model):
	user = models.ForeignKey(User, verbose_name='Исполнитель', on_delete=models.CASCADE)
	name = models.CharField(verbose_name='Название проекта', max_length=100)
	location = models.CharField(verbose_name='Адрес', max_length=100)
	name_of_customer = models.CharField(verbose_name='Имя заказчика', max_length=100)
	email_of_customer = models.EmailField(verbose_name='Почта заказчика', max_length=100)
	number_of_customer = models.CharField(verbose_name='Номер заказчика', max_length=100)
	price_of_project = models.IntegerField(verbose_name='Цена проекта')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'


class Statement(models.Model):
	# main
	ROOM_CHOICES = (
		('Зал', 'Зал'),
		('Гостинная', 'Гостинная'),
		('Прихожая', 'Прихожая'),
		('Ванная', 'Ванная'),
		('Санузел', 'Санузел'),
		('Гостевой санузел', 'Гостевой санузел'),
		('Гостеванная ванная', 'Гостеванная ванная'),
		('Главная ванная', 'Главная ванная'),
		('Гардероб', 'Гардероб'),
		('Спальня', 'Спальня'),
		('Главная спальня', 'Главная спальня'),
		('Детская', 'Детская'),
		('Балкон', 'Балкон'),
		('Лоджия', 'Лоджия'),
		('Кабинет', 'Кабинет'),
		('Кухня', 'Кухня'),
		('Летняя кухня', 'Летняя кухня'),
		('Котельная', 'Котельная'),
		('Хозяйственной помещение', 'Хозяйственной помещение'),
		('Прачечная', 'Прачечная'),
	)
	APPLICATION_CHOICES = (
		('Все комнаты', 'Все комнаты'),
	)

	CLIENT_APPROVED_CHOICES = (
		('Да', 'Да'),
		('Нет', 'Нет'),
		)

	AVIABILITY_OF_STOK = (
		('На складе', 'На складе'),
		('Под заказ', 'Под заказ'),
		('Ожидается поступление', 'Ожидается поступление'),
		)

	project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE)
	room = models.CharField(max_length=25, choices=ROOM_CHOICES, 
		verbose_name='Название комнаты', default='')
	images = models.ImageField('Фото', upload_to='statement/photos', default='', blank=True)
	product_name = models.CharField(max_length=250, verbose_name='Имя продукта', default='', blank=True)
	product_type = models.CharField(max_length=50, verbose_name='Тип продукта', default='', blank=True)
	application_room = models.CharField(
		max_length=25, choices=APPLICATION_CHOICES+ROOM_CHOICES, 
		verbose_name='Комнаты', default='')
	link = models.URLField(max_length=100, verbose_name='Ссылка на товар', default='', blank=True)
	model = models.CharField(max_length=20, verbose_name='Модель/Артикул', default='', blank=True)
	retail_price = models.IntegerField(verbose_name='Цена постащика(БЕЗ СКИДКИ!)', default=0)
	client_discount = models.IntegerField(verbose_name='Скидка для клиента', default=0)
	designer_discount = models.IntegerField(default=0, verbose_name='Скидка для дизайнера')
	qty = models.IntegerField(default=0, verbose_name='Количество')
	total_client_price = models.IntegerField(default=0, verbose_name='Общая сумма позиции')
	supplier = models.CharField(max_length=50, default='', blank=True)
	aviability_of_stock = models.CharField(max_length=25, choices=AVIABILITY_OF_STOK, default='')
	file_3dmax = models.FileField(upload_to='statement/files', default='', blank=True)
	file_revit = models.FileField(upload_to='statement/files', default='', blank=True)
	file_technical_instruction = models.FileField(upload_to='statement/files', default='', blank=True)
	client_approved	= models.CharField(max_length=3, choices=CLIENT_APPROVED_CHOICES, default='')

	def __str__(self):
		return self.product_name

	class Meta:
		verbose_name = 'Ведомость'
		verbose_name_plural = 'Ведомости'

	# family = models.CharField()
	# images = models.ImageField()
	# product_type = models.CharField()
	# product_name = models.CharField()
	# rooms = models.CharField()
	# link = models.URLField()
	# model =  models.CharField()
	# description = models.TextField()
	# retail_price = models.IntegerField()
	# client_price = models.IntegerField()
	# trade_price = models.IntegerField()
	# qty = models.IntegerField()
	# total_client_price = models.IntegerField()
	# supplier = models.CharField()
	# aviability_of_stock = models.BooleanField() (???)
	# # order_lead_tyme (???)
	# # finish/Color (???)
	# docs_revit = models.FileField()
	# docs_3dmax = models.FileField()
# 22 + 32 = 54
	#non main
	# Co_family = models.()
	# Manufacturer = models.()
	# Supplier_proposal = models.()
	# Assignee = models.()
	# Options = models.()
	# Designer_Approved = models.()
	# Project_mamager_Approval = models.()
	# Dimentions = models.()
	# Spec_Type = models.()
	# Construction_Scope = models.()
	# Purchase order_#/_Status = models.()
	# Invoice_#/_Status = models.()
	# PO_Issue_date = models.()
	# PO_Terms = models.()
	# PO_Signet_Date = models.()
	# Dispatch_Date = models.()
 #    first_name
	# Est._Delivery = models.()
	# Actual_Delivery = models.()
	# Order_Received = models.()
	# Order_On_site = models.()
	# Order_Current_Location = models.()
	# Installation_date = models.()
	# Installation_Status = models.()
	# Notes = models.TextField()
	# Status = models.CharField()
	# Allowance/Budget = models.()
	# Murk_Up = models.()
	# Trade_Discount = models.()
	# Freight_Cost = models.()
	# Tax_Rate = models.()
	# Client_Total = models.()
	# Bugget_Cost = models.()

        # user
# id
# first_name
# last_name
# number
# email
# quantity_of_workers
# profession(job)
# city
# login
# passwd


        # project
# id
# id_user
# name
# location
# name_of_customer
# email_of_customer
# number_of_customer


# main
# id (auto)
# Room (???)
# Family (???)
# Images (img)
# Product_type (CharField)
# Product_name (CharField)
# Rooms (CharField)
# Link(URL) 
# Model # (CharField)
# Description (TextField)
# Retail_Price (int)
# Client_Price (int)
# Trade_Price (int)
# QTY (int)
# Total_Client_Price (int)
# Supplier (CharField)
# Aviability_of_stock  (???)
# Order_Lead_Tyme (???)
# Finish/Color (???)
# Docs_Revit (file)
# Docs_3Dmax (file)


# # not main
# Co_family 
# Manufacturer 
# Supplier_proposal 
# Assignee 
# Options 
# Designer_Approved 
# Project_mamager_Approval 
# Aviability_of_stock 
# Dimentions 
# Spec_Type 
# Construction_Scope
# Purchase order_#/_Status
# Invoice_#/_Status 
# PO_Issue_date 
# PO_Terms 
# PO_Signet_Date 
# Dispatch_Date 
# Est._Delivery 
# Actual_Delivery 
# Order_Received 
# Order_On_site 
# Order_Current_Location 
# Installation_date 
# Installation_Status 
# Notes 
# Status 
# Allowance/Budget 
# Murk_Up 
# Trade_Discount 
# Freight_Cost 
# Tax_Rate 
# Client_Total 
# Bugget_Cost