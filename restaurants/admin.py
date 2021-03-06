from django.contrib import admin
from restaurants.models import Restaurant, Food, Comment

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('is_spicy', 'price')
    fields = ('price', 'restaurant', )
    search_fields = ('name', 'price', )
    ordering = ('-price',)

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Comment)

