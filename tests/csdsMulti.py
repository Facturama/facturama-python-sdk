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

    def test_csds_full(self){
        self.client._credentials = ('pruebas', 'pruebas2011')

        self.client.api_lite = True
        self.client.sandbox = True    

        # carga  un nuevo certificado para el RFC
        self.client.csdsMultiEmisor.upload('UN-RFC', 'key.key', 'cert.cer', '12345678a')

        #Edita el certificado para el RFC
        self.client.csdsMultiEmisor.update('UN-RFC', 'key.key', 'cert.cer', '12345678a')

        #Obtiene el certificado asociado al RFC
        csd = self.client.csdsMultiEmisor.get_by_rfc('UN-RFC')    
        print csd.Rfc    

        # Elimina el certificado del RFC
        self.client.csdsMultiEmisor.delete('UN-RFC')
    }