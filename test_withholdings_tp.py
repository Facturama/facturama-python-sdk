# Example for  technology platforms withholdings - "retenciones para plataformas tecnológicas"
# Documentation in https://apisandbox.facturama.mx/guias/complementos/servicios-plataformas-tecnologicas

import facturama
import json

def test_create_retention():
    print ("=== Create technology platforms withholdings ===")     
    facturama._credentials = ('pruebasapi', 'pruebas2011')

    cfdi_object = {
        "FolioInt": "216647",
        "FechaExp": "2021-05-27T08:08:01-06:00",
        "CveRetenc": "26",
        "Emisor": {
            "RFCEmisor": "EKU9003173C9",
            "NomDenRazSocE": "Xenon_Industrial_Articles"
        },
        "Receptor": {
            "Nacionalidad": "Nacional",
            "Nacional": {
                "RFCRecep": "MISC491214B86",
                "NomDenRazSocR": "string"
            }
        },
        "Periodo": {
            "MesIni": "01",
            "MesFin": "01",
            "Ejerc": "2021"
        },
        "Totales": {
            "montoTotOperacion": "1681.06",
            "montoTotGrav": "1681.06",
            "montoTotExent": "0.00",
            "montoTotRet": "151.2906",
            "ImpRetenidos": [
                {
                    "BaseRet": "1681.06",
                    "Impuesto": "01",
                    "MontoRet": "16.8106",
                    "TipoPagoRet": "Pago definitivo"
                },
                {
                    "BaseRet": "268.96",
                    "Impuesto": "02",
                    "MontoRet": "134.48",
                    "TipoPagoRet": "Pago definitivo"
                }
            ]
        },
        "Complemento": {
            "ServiciosPlataformasTecnologicas": {
                "Servicios": [
                    {
                        "ImpuestosTrasladadosdelServicio": {
                            "Base": "1681.06",
                            "Impuesto": "02",
                            "TasaCuota": "0.160000",
                            "Importe": "268.9696"
                        },
                        "ComisionDelServicio": {
                            "Base": "1681.06",
                            "Porcentaje": "",
                            "Importe": "14.66"
                        },
                        "FormaPagoServ": "02",
                        "TipoDeServ": "05",
                        "FechaServ": "2021-01-07T03:01:06+06:00",
                        "PrecioServSinIva": "1681.06"
                    }
                ],
                "Periodicidad": "02",
                "NumServ": 1,
                "MontToServSIva": "1681.06",
                "TotalIvaTrasladado": "268.969600",
                "TotalIvaRetenido": "134.48",
                "TotalIsrRetenido": "16.8106",
                "DifIvaEntregadoPrestServ": "134.489600",
                "MonTotalporUsoPlataforma": "14.66"
            }
        }
    }

    #facturama.api_lite = True    # Multi Issuer Mode  (API Lite or API Web don't apply, retentions are independient)
    facturama.sandbox = True       # Sandbox environment (Same meaning than CFDI context, True = sandbox mode, False = Productive mode)

    print ("------ Retention List ------")
    retentionsList = facturama.Retentions.list()
    print (retentionsList)

    # print ("------ Retention Cancel ------")
    # cancellationResponse = facturama.Retentions.delete('FQupz2o5G9n8cVH65HoixA2')
    # print (cancellationResponse)
    
    
    retentionCreated = facturama.Retentions.create(cfdi_object)
    print ("------ Retention Created ------")
    print (retentionCreated)

    print ("------ Id to Retrieve ------")
    print(retentionCreated['Id'])

    print ("------ Retention Retrieved ------")
    retentionRetrived = facturama.Retentions.retrieve(retentionCreated['Id'])
    print (retentionRetrived)

    print ("------ Retention Save as PDF ------")
    facturama.Retentions.saveAsPdf(retentionCreated['Id'], '{}.pdf'.format(retentionCreated['Id']))
    

    print ("------ Retention Save as XML ------")    
    facturama.Retentions.saveAsXML(retentionCreated['Id'], '{}.xml'.format(retentionCreated['Id']))

    print ("------ Retention Send By Mail ------")
    sendMailResponse = facturama.Retentions.sendByMail(retentionCreated['Id'], 'chucho@facturama.mx')    
    print(sendMailResponse)



if __name__ == "__main__":
    print ("### Test Facturama Technology Platforms Withholdings ###")
    print("")
    
    test_create_retention()    