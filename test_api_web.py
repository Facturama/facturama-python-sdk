import facturama
import json

#Test CFDI 3.3
def test_create_cfdi_api_web():
    print ("=== Create CFDI API Web ===")
    facturama._credentials = ('pruebasapi', 'pruebas2011')

    cfdi_object = {
        "Folio": "100",
        "ExpeditionPlace": "78140",
        "PaymentConditions": "CREDITO A SIETE DIAS",
        "CfdiType": "I",
        "PaymentForm": "03",
        "PaymentMethod": "PUE",
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

    facturama.api_lite = False    # API Web Mode
    facturama.sandbox = True       # Sandbox environment

    cfdiCreated = facturama.Cfdi.create(cfdi_object)
    print ("------ cfdiCreated ------")
    print (cfdiCreated)

    print ("------ Id to Retrieve ------")
    print(cfdiCreated['Id'])

    print ("------ cfdiRetrieved ------")
    cfdiRetrived = facturama.Cfdi.retrieve(cfdiCreated['Id'])
    print (cfdiRetrived)

    print ("------ xmlFile ------")
    facturama.Cfdi.saveAsXML(cfdiCreated['Id'], cfdiCreated['Id'] + ".xml")

    #delete(IDcfdi,type,motive,uuidReplacement)
    #type=(issued or payroll)
    #motive=(01 or 02 or 03 or 04)
    #uuidReplacement=(UUID or None)
    print("------ Cancel CFDI ------")
    cfdiRetrived = facturama.Cfdi.delete(cfdiCreated['Id'], 'issued', '02', '50AD4DD3-8BA1-4A28-BC1B-F7CD61A8F93D')
    print (cfdiRetrived)

# Test CFDI 4.0
def test_create_cfdi4_api_web():
    print ("=== Create CFDI 4.0 API Web ===")
    facturama._credentials = ('pruebasapi', 'pruebas2011')

    cfdi4_object = {
        "Folio": "100",
        "ExpeditionPlace": "78140",
        "PaymentConditions": "CREDITO A SIETE DIAS",
        "CfdiType": "I",
        "PaymentForm": "03",
        "PaymentMethod": "PUE",
        "Receiver": {
            "Rfc": "EKU9003173C9",
            "Name": "ESCUELA KEMPER URGATE",
            "CfdiUse": "P01",
            "FiscalRegime":"603",
            "TaxZipCode":"26015"
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
                "ObjetoImp":"02",
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
            }
        ]
    }

    facturama.api_lite = False    # API Web Mode
    facturama.sandbox = True       # Sandbox environment

    cfdiCreated = facturama.Cfdi.create3(cfdi4_object) #para probar CFDI 4.0 se usa metodo create3()
    print ("------ cfdiCreated ------")
    #print (cfdiCreated)

    #Imprime ID del CFDI
    print ("------ Id to Retrieve ------")
    print(cfdiCreated['Id'])

    #Imprime CFDi creado
    #print ("------ cfdiRetrieved ------")
    #cfdiRetrived = facturama.Cfdi.retrieve(cfdiCreated['Id'])
    #print (cfdiRetrived)

    #Descarga Archivo XML
    #print ("------ xmlFile ------")
    #facturama.Cfdi.saveAsXML(cfdiCreated['Id'], cfdiCreated['Id'] + ".xml")
    
    #Descarga Archivo PDF
    #print ("------ pdfFile ------")
    #facturama.Cfdi.saveAsPdf(cfdiCreated['Id'], cfdiCreated['Id'] + ".pdf")

    #Enviar cfdi por correo
    #print ("------ SendByEmail ------")
    #facturama.Cfdi.send_by_email("Issued",cfdiCreated['Id'],"rafael@facturama.mx")


    #delete(IDcfdi,type,motive,uuidReplacement)
    #type=(issued or payroll)
    #motive=(01 or 02 or 03 or 04)
    #uuidReplacement=(UUID or None)
    #print("------ Cancel CFDI ------")
    #cfdiRetrived = facturama.Cfdi.delete(cfdiCreated['Id'], 'issued', '02', '50AD4DD3-8BA1-4A28-BC1B-F7CD61A8F93D')
    #print (cfdiRetrived)





if __name__ == "__main__":
    print ("### Test Facturama API Web ###")
    print("")

    #test_create_cfdi_api_web()# CFDI 3.3
    test_create_cfdi4_api_web()# CFDI 4.0 test
