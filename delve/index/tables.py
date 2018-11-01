import django_tables2 as tables
from .models import Person

class PersonTable(tables.Table):
    commodity = tables.ManyToManyColumn()
    method = tables.ManyToManyColumn()
    class Meta:
        model = Person
        template_name = 'django_tables2/bootstrap.html'