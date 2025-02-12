from django.contrib import admin
from .models import csdep_sem3
from .models import csdep_sem2
from .models import cs_dep
from .models import csdep_sem4
from.models import csdep_sem5
from.models import csdep_sem6
# Register your models here.
admin.site.register(cs_dep)
admin.site.register(csdep_sem2)
admin.site.register(csdep_sem3)
admin.site.register(csdep_sem4)
admin.site.register(csdep_sem5)
admin.site.register(csdep_sem6)