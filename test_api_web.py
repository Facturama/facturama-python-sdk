import facturama
import json


# Test CFDI 3.3
def test_create_cfdi_api_web():
    print("=== Create CFDI API Web ===")
    facturama._credentials = ('pruebas', 'pruebas2011')

    cfdi_object = {
        "Folio": "100",
        "ExpeditionPlace": "78140",
        "PaymentConditions": "CREDITO A SIETE DIAS",
        "CfdiType": "I",
        "PaymentForm": "03",
        "PaymentMethod": "PUE",
        "Receiver": {
            "Rfc": "URE180429TM6",
            "Name": "UNIVERSIDAD ROBOTICA ESPAÑOLA",
            "CfdiUse": "G03",
            "FiscalRegime": "601",
            "TaxZipCode": "65000"
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
                "TaxObject": "02",
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
                "TaxObject": "02",
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

    facturama.api_lite = False  # API Web Mode
    facturama.sandbox = True  # Sandbox environment

    cfdiCreated = facturama.Cfdi.create(cfdi_object)
    # print ("------ cfdiCreated ------")
    # print (cfdiCreated)

    print("------ Id to Retrieve ------")
    print(cfdiCreated['Id'])

    # print ("------ cfdiRetrieved ------")
    # cfdiRetrived = facturama.Cfdi.retrieve(cfdiCreated['Id'])
    # print (cfdiRetrived)

    # print ("------ xmlFile ------")
    # facturama.Cfdi.saveAsXML(cfdiCreated['Id'], cfdiCreated['Id'] + ".xml")

    # delete(IDcfdi,type,motive,uuidReplacement)
    # type=(issued or payroll)
    # motive=(01 or 02 or 03 or 04)
    # uuidReplacement=(UUID or None)
    print("------ Cancel CFDI ------")
    cfdiRetrived = facturama.Cfdi.delete(cfdiCreated['Id'], 'issued', '02', '50AD4DD3-8BA1-4A28-BC1B-F7CD61A8F93D')
    print(cfdiRetrived)


# Test CFDI 4.0
def test_create_cfdi4_api_web():
    print("=== Create CFDI 4.0 API Web ===")
    facturama._credentials = ('pruebas', 'pruebas2011')

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
            "CfdiUse": "G03",
            "FiscalRegime": "603",
            "TaxZipCode": "26015"
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
                "TaxObject": "02",
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

    facturama.api_lite = False  # API Web Mode
    facturama.sandbox = True  # Sandbox environment

    cfdiCreated = facturama.Cfdi.create3(cfdi4_object)  # para probar CFDI 4.0 se usa metodo create3()
    print("------ cfdiCreated ------")
    # print (cfdiCreated)

    # Imprime ID del CFDI
    print("------ Id to Retrieve ------")
    print(cfdiCreated['Id'])

    # Imprime CFDi creado
    # print ("------ cfdiRetrieved ------")
    # cfdiRetrived = facturama.Cfdi.retrieve(cfdiCreated['Id'])
    # print (cfdiRetrived)

    # Descarga Archivo XML
    # print ("------ xmlFile ------")
    # facturama.Cfdi.saveAsXML(cfdiCreated['Id'], cfdiCreated['Id'] + ".xml")

    # Descarga Archivo PDF
    # print ("------ pdfFile ------")
    # facturama.Cfdi.saveAsPdf(cfdiCreated['Id'], cfdiCreated['Id'] + ".pdf")

    # Enviar cfdi por correo
    # print ("------ SendByEmail ------")
    # facturama.Cfdi.send_by_email("Issued",cfdiCreated['Id'],"rafael@facturama.mx")

    # delete(IDcfdi,type,motive,uuidReplacement)
    # type=(issued or payroll)
    # motive=(01 or 02 or 03 or 04)
    # uuidReplacement=(UUID or None)
    # print("------ Cancel CFDI ------")
    # cfdiRetrived = facturama.Cfdi.delete(cfdiCreated['Id'], 'issued', '02', '50AD4DD3-8BA1-4A28-BC1B-F7CD61A8F93D')
    # print (cfdiRetrived)


def test_catalog():
    print("=== Test Catalog ===")
    facturama._credentials = ('pruebas', 'pruebas2011')

    facturama.api_lite = False  # Multi Issuer Mode
    facturama.sandbox = True  # Sandbox environment

    # lst_client=facturama.Client.all()
    # print(lst_client[99])

    # ListarProductosPaginado
    # lst_product=facturama.Product.list(0,100,"")
    # Total de registros
    # print(lst_product["recordsTotal"])
    # Total de registros filtrados
    # print(lst_product["recordsFiltered"])
    # Muestra el contenido del registro '0'
    # print(lst_product["data"][1])
    # muestra el ID del del registro '0'
    # print(lst_product["data"][0]['Id'])

    # ListarClientesPaginado
    # lst_clients=facturama.Client.list(0,100,"")
    # Total de registros
    # print(lst_clients["recordsTotal"])
    # Total de registros filtrados
    # print(lst_clients["recordsFiltered"])
    # Muestra el contenido del registro '0'
    # print(lst_clients["data"][0])
    # muestra el ID del del registro '0'
    # print(lst_clients["data"][0]['Id'])

    # Codigos postales
    # cfdiPostalCode=facturama.PostalCodesCatalog.query({'keyword':'78140'})
    # print(cfdiPostalCode)

    # ContractTypes
    # lst_payment=facturama.ContractTypes.query()
    # print(lst_payment)

    # RegimenTypes
    # lst_regimentypes=facturama.RegimenTypes.query()
    # print(lst_regimentypes)

    # TypesOfJourney
    # lst_typesofjourney=facturama.TypesOfJourney.query()
    # print(lst_typesofjourney)

    # PositionRisks
    # lst_positionrisks=facturama.PositionRisks.query()
    # print(lst_positionrisks)

    # paymentfrequencies
    # lst_paymentfrequencies=facturama.PaymentFrequencies.query()
    # print(lst_paymentfrequencies)

    # Banks
    # lst_Banks=facturama.Banks.query()
    # print(lst_Banks)

    # Countri
    # lst_Countri=facturama.CountriesCatalog.query()
    # print(lst_Countri)

    # Catalogo Incapacidades
    # lst_Incapacities=facturama.IncapacitiesCatalog.query()
    # print(lst_Incapacities)

    # Perceptions
    # lst_Perceptions=facturama.Perceptions.query()
    # print(lst_Perceptions)

    # Deductions
    # lst_Deductions=facturama.Deductions.query()
    # print(lst_Deductions)

    # OtherPayments
    # lst_OtherPayments=facturama.OtherPayments.query()
    # print(lst_OtherPayments)

    # Originsources Catalog
    # lst_Originsources=facturama.OriginSourcesCatalog.query()
    # print(lst_Originsources)

    # ExtraHours
    # lst_ExtraHours=facturama.ExtraHours.query()
    # print(lst_ExtraHours)

    # Incapacities
    # lst_Incapacities=facturama.Incapacities.query()
    # print(lst_Incapacities)

    # Deductions Catalog
    # lst_Deductions=facturama.DeductionsCatalog.query()
    # print(lst_Deductions)


def test_list():
    print("=== Test List Cfdis ===")
    facturama._credentials = ('pruebas', 'pruebas2011')
    facturama.api_lite = False  # Multi Issuer Mode
    facturama.sandbox = True  # Sandbox environment
    #print(facturama.Cfdi.listByRfc('received', 'all', 'OÑO120726RX3'))
    print(facturama.Cfdi.listAll('issuedLite', None, None, '', '', '', 'all', '', '0'))
    #print(facturama.Cfdi.listById('ejS5fM9j8Yv6U0dfEctY2g2','issued'))

def test_validar():
    print("Validar Cliente")
    facturama._credentials = ('pruebas', 'pruebas2011')
    facturama.api_lite = False  # Multi Issuer Mode
    facturama.sandbox = True  # Sandbox environment    
    params={
        "Rfc": "EKU9003173C9",
        "Name": "ESCUELA KEMPER URGATE",
        "ZipCode":"26015",
        "FiscalRegime": "601"      
    }
    print(facturama.Customers.validate(params))

if __name__ == "__main__":
    print("### Test Facturama API Web ###")
    print("")
    # test_create_cfdi_api_web()# CFDI 3.3
    # test_create_cfdi4_api_web()# CFDI 4.0 test
    # test_catalog()
    #test_list()
    #test_validar()
