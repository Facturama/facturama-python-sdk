from . import BaseEndpointTestCase


class CatalogEndpointTestCase(BaseEndpointTestCase):
    def test_prod_srv_get(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        prod_or_srv = self.client.ProductsServicesCatalog.query({'keyword': 'Caballos'})
        assert prod_or_srv
