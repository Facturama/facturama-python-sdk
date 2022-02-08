import facturama
import json

def test_create_cfdi_multi():
    print ("=== Create CFDI Multi ===")
    facturama._credentials = ('pruebasapi', 'pruebas2011')

    cfdi_object = {
        "Folio": "100",
        "Serie": "R",
        "Currency": "MXN",
        "ExpeditionPlace": "78116",
        "PaymentConditions": "CREDITO A SIETE DIAS",
        "CfdiType": "I",
        "PaymentForm": "03",
        "PaymentMethod": "PUE",
        "Issuer": {
            "FiscalRegime": "601",
            "Rfc": "EKU9003173C9",
            "Name": "SinDelantal Mexico"
        },
        "Receiver": {
            "Rfc": "XAXX010101000",
            "Name": "Publico en general",
            "CfdiUse": "P01"
        },
        "Items": [
            {
                "ProductCode": "10101504",
                "IdentificationNumber": "EDL",
                "Description": "Estudios de viabilidad",
                "Unit": "NO APLICA",
                "UnitCode": "MTS",
                "UnitPrice": 50.0,
                "Quantity": 2.0,
                "Subtotal": 100.0,
                "Taxes": [
                    {
                        "Total": 16.0,
                        "Name": "IVA",
                        "Base": 100.0,
                        "Rate": 0.16,
                        "IsRetention": False
                    }
                ],
                "Total": 116.0
            },
            {
                "ProductCode": "10101504",
                "IdentificationNumber": "001",
                "Description": "SERVICIO DE COLOCACION",
                "Unit": "NO APLICA",
                "UnitCode": "E49",
                "UnitPrice": 100.0,
                "Quantity": 15.0,
                "Subtotal": 1500.0,
                "Discount": 0.0,
                "Taxes": [
                    {
                        "Total": 240.0,
                        "Name": "IVA",
                        "Base": 1500.0,
                        "Rate": 0.16,
                        "IsRetention": False
                    }
                ],
                "Total": 1740.0
            }
        ]
    }

    facturama.api_lite = True    # Multi Issuer Mode
    facturama.sandbox = True       # Sandbox environment

    cfdiCreated = facturama.CfdiMultiEmisor.create(cfdi_object)
    print ("------ cfdiCreated ------")
    print (cfdiCreated)

    print ("------ Id to Retrieve ------")
    print(cfdiCreated['Id'])

    print ("------ cfdiRetrieved ------")
    cfdiRetrived = facturama.CfdiMultiEmisor.retrieve(cfdiCreated['Id'])
    print (cfdiRetrived)

    #delete(IDcfdi,type,motive,uuidReplacement)
    #motive=(01 or 02 or 03 or 04)
    #uuidReplacement=(UUID or None)
    print("------ Cancel CFDI Multiemisor------")
    cfdiRetrived = facturama.CfdiMultiEmisor.delete(cfdiCreated['Id'], '01', '50AD4DD3-8BA1-4A28-BC1B-F7CD61A8F93D')
    print (cfdiRetrived)





def test_update_csd():
    facturama._credentials = ('pruebasapi', 'pruebas2011')
    facturama.api_lite = True
    facturama.sandbox = True
    facturama.csdsMultiEmisor.update('EKU9003173C9', 'key.key', 'cert.cer', '12345678a')
    csd = facturama.csdsMultiEmisor.get_by_rfc('EKU9003173C9')
    print (csd.Rfc)

    facturama.csdsMultiEmisor.delete('EKU9003173C9')


if __name__ == "__main__":
    print ("### Test Facturama API ###")
    print("")

    test_create_cfdi_multi()
    #test_update_csd()
