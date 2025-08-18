from rest_framework.viewsets import ViewSet
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.response import Response
from ..domain.company.company_datastore import CompanyDataStore
from ..decorators.cloudinary import handle_logo_upload


class Company(ViewSet):
    def _bean_to_dict(self, company):
        return {
            "id": company.id,
            "name": company.name,
            "domain": company.domain,
            "industry": company.industry,
            "logo_url": company.logo_url,
            "location": company.location,
            "state": company.state,
            "created_at": company.created_at,
            "updated_at": company.updated_at,
        }

    def retrieve(self, request, company_id=None):
        company = CompanyDataStore.get_company_by_id(company_id)
        return Response(self._bean_to_dict(company), status=HTTP_200_OK)

    @handle_logo_upload
    def create(self, request):
        company = CompanyDataStore.create_company(request.data)
        return Response(self._bean_to_dict(company), status=HTTP_201_CREATED)

    def update(self, request, company_id=None):
        company = CompanyDataStore.update_company(company_id, request.data)
        return Response(self._bean_to_dict(company), status=HTTP_200_OK)

    def destroy(self, request, company_id=None):
        CompanyDataStore.delete_company(company_id)
        return Response(status=HTTP_204_NO_CONTENT)
