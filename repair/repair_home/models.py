from django.db import models


class CPU(models.Model):
    cpu = models.CharField('Процессор', max_length=100)
    cpu_core = models.SmallIntegerField('Кол-во ядер')
    frequency = models.FloatField('Частота', max_length=60)
    type_connect = models.BooleanField('Интегрированный?')
    graphics_cpu = models.CharField('Графический процессор', max_length=130)

    def __str__(self):
        return self.cpu


class RAM(models.Model):
    name_ram = models.CharField('Производитель', max_length=50)
    memory_ram = models.SmallIntegerField('Объем установленный')
    type_socket = models.CharField('Тип DDR', max_length=5)
    frequency = models.FloatField('Частота', max_length=60)

    def __str__(self):
        return self.name_ram


class Memory(models.Model):
    ssd = models.BooleanField('ssd')
    hard_disk = models.BooleanField('HardDisk')
    memory_ssd = models.SmallIntegerField('Объем ssd')
    memory_hard = models.SmallIntegerField('Объем жесткого диска')


class NoteBook(models.Model):
    name_company = models.CharField('Производитель', max_length=20, unique=True)
    series = models.CharField('Серия/Номер модели', max_length=255, unique=True)
    diagonal = models.FloatField('Диагональ экрана', max_length=60)
    size_screen = models.CharField('Разрешение экрана', max_length=20)
    type_matrix = models.CharField('Тип матрицы экрана', max_length=30)
    surface_screen = models.CharField('Поверхность экрана', max_length=30)
    key_cpu = models.ForeignKey(CPU, on_delete=models.PROTECT)
    key_ram = models.ForeignKey(RAM, on_delete=models.PROTECT)
    key_memory = models.ForeignKey(Memory, on_delete=models.PROTECT)

    def __int__(self):
        return self.id
