from django.contrib import admin
from .models import NoteBook, CPU, RAM, Memory

admin.site.register(NoteBook)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(Memory)
