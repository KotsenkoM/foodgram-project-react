from django.contrib import admin

from .models import Tag, Recipe, Ingredient, Cart, Favorite


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')


admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Cart)
admin.site.register(Favorite)
