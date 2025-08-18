from datetime import datetime, timezone
from mongoengine import Document, DateTimeField, StringField


class Company(Document):
    name = StringField(required=True)
    domain = StringField()
    industry = StringField()
    logo_url = StringField()
    location = StringField()
    state = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    meta = {"collection": "Company", "indexes": [{"fields": ["name"], "unique": True}]}

    def clean(self):
        def _normalize(val):
            if isinstance(val, list):
                return val[0] if val else None
            return val

        self.name = _normalize(self.name).lower() if _normalize(self.name) else None
        self.domain = (
            _normalize(self.domain).lower() if _normalize(self.domain) else None
        )
        self.industry = (
            _normalize(self.industry).lower() if _normalize(self.industry) else None
        )
        self.location = (
            _normalize(self.location).lower() if _normalize(self.location) else None
        )
        self.state = _normalize(self.state).lower() if _normalize(self.state) else None
        self.logo_url = _normalize(self.logo_url)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
        return super(Company, self).save(*args, **kwargs)
