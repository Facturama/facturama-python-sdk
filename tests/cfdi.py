import base64

from . import BaseEndpointTestCase


class CfdiEndpointTestCase(BaseEndpointTestCase):

    def test_cfdi_get(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        html_file = self.client.Cfdi.get_by_file('html', 'Issued', '7eo51BvzV-E16gBx3nnxfQ2')
        self.client.api_lite = False
        self.client.sandbox = False
        html_name = '{}.html'.format('original')
        with open(html_name, 'wb') as f:
            f.write(base64.urlsafe_b64decode(html_file['Content'].encode('utf-8')))

    def test_cfdi_create(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        self.client.api_lite = True
        tmp = self.client.Cfdi.create(self.cfdi_object.copy())
        assert tmp

    def test_cfdi_list(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        tmp = self.client.Cfdi.list('issued','Expresion en Software','all')
        assert tmp

    def test_cfdi_email(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        tmp = self.client.Cfdi.send_by_email('issued','GgQKVvV84IlgmFCMqJVraQ2','mail@mail.com')
        assert tmp

    def test_cfdi_saveAsPdf(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        self.client.sandbox = True
        self.client.api_lite = False
        file = self.client.Cfdi.saveAsPdf('7eo51BvzV-E16gBx3nnxfQ2','nombre.pdf')
        assert file

    def test_cfdi_saveAsHtml(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        self.client.sandbox = True
        self.client.api_lite = False
        file = self.client.Cfdi.saveAsHtml('7eo51BvzV-E16gBx3nnxfQ2','nombre.html') #OwMgofF7ZDEM60gerUXudw2
        assert file

    def test_cfdi_complemento(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        self.client.sandbox = True
        self.client.api_lite = False
        tmp = self.client.Cfdi.create(self.cfdi_object_complemento_pago.copy())
        assert tmp

    def test_cfdi_complemento_cuentas_terceros(self):
        self.client._credentials = ('sdkpruebas', 'pruebas2022')
        self.client.sandbox = True
        self.client.api_lite = False
        tmp = self.client.Cfdi.create(self.cfdi_object_complemento_terceros.copy())
        assert tmp