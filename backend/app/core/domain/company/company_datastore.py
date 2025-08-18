from ...models.company import Company
from .beans_factory import CompanyBeanFactory
from .beans import CompanyBean


class CompanyDataStore:
    @staticmethod
    def create_company(data: dict) -> CompanyBean:
        company = Company(**data).save()
        return CompanyBeanFactory.to_bean(company)

    @staticmethod
    def get_company_by_id(company_id: str) -> CompanyBean:
        company = Company.objects.get(id=company_id)
        return CompanyBeanFactory.to_bean(company)

    @staticmethod
    def update_company(company_id: str, data: dict) -> CompanyBean:
        company = Company.objects.get(id=company_id)
        for field, value in data.items():
            setattr(company, field, value)
        company.save()
        return CompanyBeanFactory.to_bean(company)

    @staticmethod
    def delete_company(company_id: str) -> None:
        company = Company.objects.get(id=company_id)
        company.delete()

    @staticmethod
    def list_companies() -> list[CompanyBean]:
        return [CompanyBeanFactory.to_bean(c) for c in Company.objects.all()]
