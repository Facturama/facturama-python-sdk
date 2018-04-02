import base64

from . import BaseEndpointTestCase


class CfdiEndpointTestCase(BaseEndpointTestCase):

    def test_cfdi_create(self):
        self.client._credentials = ('pruebas', 'pruebas2011')
        html_file = self.client.Cfdi.get_by_file('html', 'IssuedLite', '3Dy9HrTLw2RF_R2H15kELQ2')
        self.client.api_lite = True
        html_name = '{}.html'.format('original')
        with open(html_name, 'wb') as f:
            f.write(base64.urlsafe_b64decode(html_file['Content'].encode('utf-8')))
