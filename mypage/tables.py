from .models import Software
import itertools
import django_tables2 as tables

class SoftwareTable(tables.Table):
    class Meta:
        model = Software
        template_name = "django_tables2/bootstrap.html"
        title = tables.Column("title")
        desc = tables.Column("desc")
        urls = tables.Column("urls")