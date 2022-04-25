from django.contrib import admin
from .models import Document, Faculty, Specialization, Type

admin.site.register(Faculty)
admin.site.register(Type)
admin.site.register(Specialization)
admin.site.register(Document)

# admin.site.register(Kinterms)
