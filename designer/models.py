from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.utils.translation import ugettext_lazy as _
# from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
# 	JOB_CHOICES = (
# 		('Исполнитель', 'Исполнитель'),
# 		)
	# user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
	# first_name = models.CharField(max_length=20, verbose_name='Имя')
	# last_name = models.CharField(max_length=20, verbose_name='Фамиля')
	# number = models.CharField(max_length=20, verbose_name='Номер телефона')
	# email = models.EmailField(max_length=50, verbose_name='Почта')
	# quantity_of_workers = models.IntegerField(
	# 	verbose_name='Количество работников', default=0)
	# job = models.CharField(verbose_name='Профессия', max_length=20, choices=JOB_CHOICES)
	# city = models.CharField(verbose_name='Город', max_length=30, blank=True)
	# login = models.CharField(verbose_name='Логин', max_length=50)
	# passwd = models.CharField(verbose_name='Пароль', max_length=100)
	#
	# def __str__(self):
	# 	return self.number
	#
	# class Meta:
	# 	verbose_name = 'Пользователь'
	# 	verbose_name_plural = 'Пользователи'


# class UserManager(BaseUserManager):
# 	"""Define a model manager for User model with no username field."""
#
# 	use_in_migrations = True
#
# 	def _create_user(self, email, password, **extra_fields):
# 		"""Create and save a User with the given email and password."""
# 		if not email:
# 			raise ValueError('The given email must be set')
# 		email = self.normalize_email(email)
# 		user = self.model(email=email, **extra_fields)
# 		user.set_password(password)
# 		user.save(using=self._db)
# 		return user
#
# 	def create_user(self, email, password=None, **extra_fields):
# 		"""Create and save a regular User with the given email and password."""
# 		extra_fields.setdefault('is_staff', False)
# 		extra_fields.setdefault('is_superuser', False)
# 		return self._create_user(email, password, **extra_fields)
#
# 	def create_superuser(self, email, password, **extra_fields):
# 		"""Create and save a SuperUser with the given email and password."""
# 		extra_fields.setdefault('is_staff', True)
# 		extra_fields.setdefault('is_superuser', True)
#
# 		if extra_fields.get('is_staff') is not True:
# 			raise ValueError('Superuser must have is_staff=True.')
# 		if extra_fields.get('is_superuser') is not True:
# 			raise ValueError('Superuser must have is_superuser=True.')
#
# 		return self._create_user(email, password, **extra_fields)


# class User(AbstractUser):
# 	"""User model."""
#
# 	username = None
# 	email = models.EmailField(_('email address'), unique=True)
# 	# date_joined = models.DateTimeField(auto_now_add=True)
# 	# is_active = models.BooleanField(default=True)
# 	# is_superuser = models.BooleanField(default=False)
#
# 	USERNAME_FIELD = 'email'
# 	REQUIRED_FIELDS = []
#
# 	objects = UserManager()


class Project(models.Model):
	user = models.ForeignKey(User, verbose_name='Исполнитель', on_delete=models.CASCADE)
	name = models.CharField(verbose_name='Название проекта', max_length=100)
	# location = models.CharField(verbose_name='Адрес', max_length=100)
	# name_of_customer = models.CharField(verbose_name='Имя заказчика', max_length=100)
	# email_of_customer = models.EmailField(verbose_name='Почта заказчика', max_length=100)
	# number_of_customer = models.CharField(verbose_name='Номер заказчика', max_length=100)
	# price_of_project = models.IntegerField(verbose_name='Цена проекта')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'


class Statement(models.Model):
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
	# product_type = models.CharField(max_length=50, verbose_name='Тип продукта', default='', blank=True)
	# application_room = models.CharField(
	# 	max_length=25, choices=APPLICATION_CHOICES+ROOM_CHOICES,
	# 	verbose_name='Комнаты', default='')
	link = models.URLField(max_length=1000, verbose_name='Ссылка на товар', default='', blank=True)
	# model = models.CharField(max_length=20, verbose_name='Модель/Артикул', default='', blank=True)
	unit = models.CharField(max_length=100, verbose_name='Единица измерения', default='', blank=True)
	retail_price = models.IntegerField(verbose_name='Цена постащика(БЕЗ СКИДКИ!)', default=0)
	# client_discount = models.IntegerField(verbose_name='Скидка для клиента', default=0)
	# designer_discount = models.IntegerField(default=0, verbose_name='Скидка для дизайнера')
	qty = models.IntegerField(default=0, verbose_name='Количество')
	total_client_price = models.IntegerField(default=0, verbose_name='Общая сумма позиции')
	# supplier = models.CharField(max_length=50, default='', blank=True)
	# aviability_of_stock = models.CharField(max_length=25, choices=AVIABILITY_OF_STOK, default='')
	file_3dmax = models.FileField(upload_to='statement/files', default='', blank=True)
	file_revit = models.FileField(upload_to='statement/files', default='', blank=True)
	file_technical_instruction = models.FileField(upload_to='statement/files', default='', blank=True)
	# client_approved	= models.CharField(max_length=3, choices=CLIENT_APPROVED_CHOICES, default='')

	def __str__(self):
		return self.product_name

	class Meta:
		verbose_name = 'Ведомость'
		verbose_name_plural = 'Ведомости'