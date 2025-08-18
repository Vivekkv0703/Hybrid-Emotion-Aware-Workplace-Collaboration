from .beans import CompanyBean
from ...models.company import Company


class CompanyBeanFactory:
    @staticmethod
    def to_bean(company: Company) -> CompanyBean:
        return CompanyBean(
            id=str(company.id),
            name=company.name,
            domain=company.domain,
            industry=company.industry,
            logo_url=company.logo_url,
            location=company.location,
            state=company.state,
            created_at=company.created_at,
            updated_at=company.updated_at,
        )
