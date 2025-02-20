from . import BaseEndpointTestCase


class CatalogEndpointTestCase(BaseEndpointTestCase):
    def test_prod_srv_get(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        self.client.sandbox = True
        prod_or_srv = self.client.ProductsServicesCatalog.query({'keyword': 'Caballos'})
        assert prod_or_srv

    def test_tariff_fractions_catalog(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        self.client.sandbox = True
        tariff_fractions = self.client.TariffFractionsCatalog.query({'keyword': 'aceite'})
        assert tariff_fractions

    def test_customs_units_catalog(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        self.client.sandbox = True
        customs_units = self.client.CustomsUnitsCatalog.query({'keyword': 'litro'})
        assert customs_units
