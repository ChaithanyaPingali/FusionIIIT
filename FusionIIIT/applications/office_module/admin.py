from django.contrib import admin

from .models import vendor, stock, apply_for_purchase, quotations, purchase_commitee

admin.site.register(vendor),
admin.site.register(stock),
admin.site.register(apply_for_purchase),
admin.site.register(quotations),
admin.site.register(purchase_commitee),