from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class AdminAreaCongfig(AdminConfig):
    default_site = 'api.admin.AdminArea'


class ApiConfig(AppConfig):
    name = 'api'
