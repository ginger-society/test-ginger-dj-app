"""
Admin module for the app src
"""

from ginger.contrib import admin

from .models import Tenant2

admin.site.register(Tenant2)
