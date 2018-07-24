from django.contrib import admin
from .models import Person, Doc, Venda, Produto

admin.site.register(Person)
admin.site.register(Doc)
admin.site.register(Venda)
admin.site.register(Produto)