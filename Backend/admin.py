from django.contrib import admin
from .models import *
# Register your models here.

# class MyModelAdmin(admin.ModelAdmin):
    # def get_queryset(self, request):
        #     qs = super(MyModelAdmin, self).get_queryset(request)
        #     if request.user.is_superuser():
        #         return qs
        #     return qs.filter(author=request.user)

class AnimalAdmin(admin.ModelAdmin):
    readonly_fields = ['author']
    # exclude = ['author']
    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if not request.user.is_superuser or not form.cleaned_data['author']:
                obj.author = request.user
                obj.save()
            elif form.cleaned_data['author']:
                obj.author = form.cleaned_data['author']
                obj.save()
        # obj.author = request.user
        # obj.save()
        # print (obj)
        # print (obj.__dict__)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(Animal, AnimalAdmin)