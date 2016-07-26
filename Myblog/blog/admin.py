from django.contrib import admin
# Register your models here.
from .models import Article, Client, Category, Request_of_laboratory, Request_of_medcenter, Delivery, AllFieldMethod, \
    Blog1, Author1, Entry1

admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Request_of_laboratory)
admin.site.register(Request_of_medcenter)
admin.site.register(Delivery)
admin.site.register(Article)
admin.site.register(AllFieldMethod)
admin.site.register(Blog1)
admin.site.register(Author1)
admin.site.register(Entry1)



