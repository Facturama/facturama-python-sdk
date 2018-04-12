import base64

from . import BaseEndpointTestCase


class CfdiMultiEndpointTestCase(BaseEndpointTestCase):

    def test_cfdi_get(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        html_file = self.client.CfdiMultiEmisor.get_by_file('html', 'IssuedLite', 'o9Vy0QfumyYEcOuu3S-7Cw2')
        self.client.api_lite = True
        html_name = '{}.html'.format('original')
        with open(html_name, 'wb') as f:
            f.write(base64.urlsafe_b64decode(html_file['Content'].encode('utf-8')))

    def test_cfdi_create(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        self.client.api_lite = True
        tmp = self.client.CfdiMultiEmisor.create(self.cfdi_object.copy())
        assert tmp

    def test_cfdi_list(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        filter = dict(rfc='XAXX010101000',
                      folioStart = 100,
                      folioEnd = 200
                )
        tmp = self.client.CfdiMultiEmisor.list(filter)
        assert tmp

    def test_cfdi_saveAsPdf(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        file = self.client.CfdiMultiEmisor.saveAsPdf('o9Vy0QfumyYEcOuu3S-7Cw2','nombre.pdf')
        assert file

    def test_cfdi_saveAsHtml(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        file = self.client.CfdiMultiEmisor.saveAsHtml('o9Vy0QfumyYEcOuu3S-7Cw2','nombre.html')
        assert file

    def test_cfdi_detail(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        detailInfo = self.client.CfdiMultiEmisor.detail('o9Vy0QfumyYEcOuu3S-7Cw2')
        assert detailInfo