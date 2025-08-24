from datetime import datetime, timezone
from mongoengine import (
    Document,
    StringField,
    EmailField,
    ReferenceField,
    BooleanField,
    DateTimeField,
    CASCADE,
    NULLIFY,
)


class Employee(Document):
    first_name = StringField(required=True)
    last_name = StringField()
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    company = ReferenceField("Company", reverse_delete_rule=CASCADE)
    role = StringField()
    manager = ReferenceField("Employee", reverse_delete_rule=NULLIFY)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    meta = {
        "collection": "Employee",
        "indexes": [{"fields": ["company", "email"], "unique": True}],
    }

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
        return super(Employee, self).save(*args, **kwargs)
