from datetime import datetime, UTC
from mongoengine import Document, DateTimeField, StringField


class Company(Document):
    name = StringField(required=True)
    domain = StringField()
    industry = StringField()
    logo_url = StringField()
    location = StringField()
    state = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(UTC))
    updated_at = DateTimeField(default=lambda: datetime.now(UTC))

    meta = {"collection": "Company", "indexes": [{"fields": ["name"], "unique": True}]}

    def clean(self):
        self.name = self.name.lower() if self.name else None
        self.domain = self.domain.lower() if self.domain else None
        self.industry = self.industry.lower() if self.industry else None
        self.location = self.location.lower() if self.location else None
        self.state = self.state.lower() if self.state else None

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now(UTC)
        self.updated_at = datetime.now(UTC)
        return super(Company, self).save(*args, **kwargs)
