from . import BaseEndpointTestCase


class CustomerEndpointTestCase(BaseEndpointTestCase):
    def test_customer_create(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')

        customer = self.client.Client.create(self.customer_object.copy())
        assert customer.Id

    def test_customer_get(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        customer = self.client.Client.retrieve('98DY-y6qSikkykW2nhp9kw2')
        assert customer.Id

    def test_customer_get_all(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        customer = self.client.Client.all()
        assert customer
