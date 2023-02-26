from django.db import models
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
import uuid
from datetime import datetime

# Create your models here.


class Employees(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    first_name = columns.Text(required=True)
    last_name = columns.Text()
    department = columns.Text(required=True)
    salary = columns.Integer(default=0)
    bonus = columns.Integer(default=0)
    role = columns.Text(required=True)
    phone = columns.BigInt(default=0)
    hire_date = columns.DateTime(default=datetime.now)
