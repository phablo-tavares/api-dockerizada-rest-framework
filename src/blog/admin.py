from django.contrib import admin
from .models import Autor,Post,Comentario

# Register your models here.
admin.site.register(Autor)
admin.site.register(Post)
admin.site.register(Comentario)