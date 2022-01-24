from django.db import models
wifi_choices = {
    ('PL', 'wifi есть')
}


class Category(models.Model):
    category = models.CharField('Категория', max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category


class ModelNoteBook(models.Model):
    model_notebook = models.CharField('Модель ноутбука(Категории сайт)', max_length=200)

    class Meta:
        verbose_name = 'Категория сайта'
        verbose_name_plural = 'Категории сайта'

    def __str__(self):
        return self.model_notebook


class CPU(models.Model):
    cpu = models.CharField('Процессор', max_length=100)
    cpu_core = models.SmallIntegerField('Кол-во ядер')
    frequency = models.FloatField('Частота', max_length=60)
    graphics_cpu = models.CharField('Графический процессор', max_length=130)
    cpu_socket = models.CharField('Сокет', max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'

    def __str__(self):
        return self.cpu


class RAM(models.Model):
    name_ram = models.CharField('Производитель', max_length=50)
    memory_ram = models.SmallIntegerField('Объем установленный ГБ')
    type_socket = models.CharField('Тип DDR', max_length=5)
    frequency = models.FloatField('Частота', max_length=60)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'ОЗУ'
        verbose_name_plural = 'ОЗУ'

    def __str__(self):
        return self.name_ram


class Memory(models.Model):
    # TO DO Сделать имя для SSD или HARD
    ssd = models.BooleanField('ssd')
    hard_disk = models.BooleanField('HardDisk')
    memory_ssd = models.SmallIntegerField('Объем ssd ГБ')
    memory_hard = models.SmallIntegerField('Объем жесткого диска ГБ')
    name_ssd = models.CharField('Название ssd', max_length=40)
    name_hard = models.CharField('Название hard', max_length=40)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Память'
        verbose_name_plural = 'Память'

    def __str__(self):
        return self.name_ssd


class VideoCart(models.Model):
    name = models.CharField('Название', max_length=200)
    memory = models.SmallIntegerField('Память ГБ')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ВидеоКарта'
        verbose_name_plural = 'ВидеоКарты'


class Motherboard(models.Model):
    name = models.CharField('Название', max_length=200)
    number_slots_ram = models.SmallIntegerField('Кол-во слотов для ОЗУ')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнскае платы'


class NoteBook(models.Model):

    name_company = models.CharField('Производитель', max_length=20, unique=True)
    image_1 = models.ImageField('Фото 1', upload_to='media',
                                default='test.jpg')
    image_2 = models.ImageField('Фото 2', upload_to='media',
                                default='test.jpg')

    series = models.CharField('Серия/Номер модели', max_length=255, unique=True)
    diagonal = models.FloatField('Диагональ экрана', max_length=60)
    size_screen = models.CharField('Разрешение экрана', max_length=20)
    type_matrix = models.CharField('Тип матрицы экрана', max_length=30)
    surface_screen = models.CharField('Поверхность экрана', max_length=30)
    wifi = models.CharField('wifi', choices=wifi_choices, max_length=20)

    key_cpu = models.ForeignKey(CPU, on_delete=models.PROTECT)
    type_connect_cpu = models.BooleanField('Интегрированный?')

    key_ram = models.ForeignKey(RAM, on_delete=models.PROTECT)
    type_connect_ram = models.BooleanField('Есть интергрированный слот?')

    key_memory = models.ForeignKey(Memory, on_delete=models.PROTECT)
    type_connect_memory = models.BooleanField('Есть интергрированный слот?')

    key_video_cart = models.ForeignKey(VideoCart, on_delete=models.PROTECT)
    type_connect_video = models.BooleanField('Интергрированная?')

    key_motherboard = models.ForeignKey(Motherboard, on_delete=models.PROTECT)

    category_site = models.ForeignKey(ModelNoteBook, on_delete=models.PROTECT)

    availability = models.BooleanField('Наличие', default=False)
    usb_ports = models.SmallIntegerField('USB портов')
    hdmi_port = models.BooleanField('HDMI')
    lan = models.BooleanField('LAN порт')
    bluetooth_5 = models.BooleanField('Bluetooth 5')
    bluetooth_4 = models.BooleanField('Bluetooth 4')
    headphone = models.CharField('Наушники', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    price = models.FloatField()

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

    def __str__(self):
        return self.name_company


class InfoTmp(models.Model):

    name = models.CharField('Марка', max_length=25)
    number_series = models.CharField('Модель\Серия', max_length=40)
    text = models.TextField('Описание', max_length=10_000)

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

    def __str__(self):
        return self.name
