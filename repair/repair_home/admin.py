from django.contrib import admin
from .models import NoteBook, CPU, RAM, Memory, Motherboard, VideoCart

admin.site.register(NoteBook)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(Memory)
admin.site.register(Motherboard)
admin.site.register(VideoCart)
