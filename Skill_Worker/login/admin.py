from django.contrib import admin
from login.models import Worker
from work.models import City,Community,Skill_cat,Education,Evaluation,Governorate

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Governorate)
class GovernorateAdmin(admin.ModelAdmin):
    pass

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill_cat)
class Skill_catAdmin(admin.ModelAdmin):
    pass

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    pass