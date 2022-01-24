from django.contrib import admin
from .models import Category, NoteBook, CPU, RAM, Memory, Motherboard, VideoCart, ModelNoteBook

admin.site.register(Category)
admin.site.register(NoteBook)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(Memory)
admin.site.register(Motherboard)
admin.site.register(VideoCart)
# admin.site.register(CategorySearch)

admin.site.register(ModelNoteBook)
