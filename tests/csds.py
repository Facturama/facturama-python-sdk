from . import BaseEndpointTestCase


class CSDSEndpointTestCase(BaseEndpointTestCase):
    def test_csds(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        self.client.api_lite = True
        self.client.sandbox = True
        self.client.csds.upload('rfc', 'csds.key', 'csds.cer', 'pass', v=2)
        csd = self.client.csds.get_by_rfc('rfc', v=2)
        assert csd.status
