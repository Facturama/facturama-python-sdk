from . import BaseEndpointTestCase


class CSDSMultiEndpointTestCase(BaseEndpointTestCase):
    def test_csds(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        self.client.sandbox = True
        csd = self.client.csdsMultiEmisor.get_by_rfc('UN-RFC')
        assert csd.status

    def getCurrentCsds(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        self.client.sandbox = True
        currentCsds = self.client.csdsMultiEmisor.get()
        assert currentCsds