import django_tables2 as tables
from .models import Statement

class PersonTable(tables.Table):
    class Meta:
        model = Statement
        template_name = "django_tables2/bootstrap.html"
        fields = ('project', 'room', 'images', 'product_name', 'product_type', 'application_room', 'link',
                  'model', 'retail_price', 'client_discount', 'designer_discount', 'qty', 'total_client_price',
                  'supplier', 'aviability_of_stock', 'file_3dmax', 'file_revit', 'file_technical_instruction',
                  'client_approved')