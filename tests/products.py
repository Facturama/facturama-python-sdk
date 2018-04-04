from . import BaseEndpointTestCase


class ProductEndpointTestCase(BaseEndpointTestCase):

    def test_product_create(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        product = self.client.Product.create(self.product_object.copy())
        assert product.Name == 'Sitio Web CMS'
        assert product.IdentificationNumber == 'WEB003'

    def test_product_get(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        product = self.client.Product.all()
        assert product
