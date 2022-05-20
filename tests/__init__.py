import unittest
import random
import facturama



class BaseEndpointTestCase(unittest.TestCase):
    random.seed()

    client = facturama

    customer_object = {
        "Id": "1111000",
        "Email": "test@test.com",
        "EmailOp1": "",
        "EmailOp2": "",
        "Rfc": "CACX7605101P8",
        "Name": "RXOCHILT CASAS CHAVEZ",
        "CfdiUse": "P01",
        "TaxResidence": "10740",
        "FiscalRegime":"605",
        "NumRegIdTrib": "",
        "Address": {
            "Street": "Calle de pruebas",
            "ExteriorNumber": "123",
            "InteriorNumber": "456",
            "Neighborhood": "Santa Teresa",
            "ZipCode": "10740",
            "Locality": "Ciudad de México",
            "Municipality": "La Magdalena Contreras",
            "State": "Distrito Federal",
            "Country": "Mex"
        }
    }

    product_object = {
      "Unit": "Servicio",
      "UnitCode": "E48",
      "IdentificationNumber": "WEB003",
      "Name": "Sitio Web CMS",
      "Description": "Desarrollo de sitio web empleando un CMS",
      "Price": 6500,
      "CodeProdServ": "43232408",
      "CuentaPredial": "123",
      "Taxes": [
        {
          "Name": "IVA",
          "Rate": 0.16,
          "IsRetention": False,
          "IsFederalTax": True
        },
        {
          "Name": "ISR",
          "IsRetention": True,
          "IsFederalTax": True,
          "Total": 0.10
        },
        {
          "Name": "IVA",
          "IsRetention": True,
          "IsFederalTax": True,
          "Total": 0.106667
        }
      ]
    }
    
    branch_office_object = {
        "Name": "Corp Inc",
        "Description": "Desc corp",
        "Address": {
            "Street": "Fenix One",
            "ExteriorNumber": "1",
            "InteriorNumber": "0",
            "Neighborhood": "Call me",
            "ZipCode": "59510",
            "Locality": "Xiquilpan",
            "Municipality": "Jiquilpan",
            "State": "MICHOACAN DE OCAMPO",
            "Country": "MX"
        },
    }

    cfdi_object ={
        "Folio": "100",
        "Serie": "B",
        "Currency": "MXN",
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
                "TaxObject":"02",
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
                "TaxObject":"02",
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

    cfdi_object_40 ={
        "Folio": "100",
        "Serie": "B",
        "Currency": "MXN",
        "ExpeditionPlace": "78140",
        "PaymentConditions": "CREDITO A SIETE DIAS",
        "CfdiType": "I",
        "PaymentForm": "03",
        "PaymentMethod": "PUE",
        "Receiver": {
            "Rfc": "URE180429TM6",
            "Name": "UNIVERSIDAD ROBOTICA ESPAÑOLA",
            "CfdiUse": "CP01",
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
                "TaxObject":"02",
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
                "TaxObject":"02",
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

    cfdi_object_40_mult ={
        "Folio": "100",
        "Serie": "B",
        "Currency": "MXN",
        "ExpeditionPlace": "78140",
        "PaymentConditions": "CREDITO A SIETE DIAS",
        "CfdiType": "I",
        "PaymentForm": "03",
        "PaymentMethod": "PUE",
        "Issuer": {
            "Rfc":"EKU9003173C9",
            "Name":"ESCUELA KEMPER URGATE",
            "CfdiUse":"G03",
            "FiscalRegime":"601"
        },
        "Receiver": {
            "Rfc": "URE180429TM6",
            "Name": "UNIVERSIDAD ROBOTICA ESPAÑOLA",
            "CfdiUse": "CP01",
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
                "TaxObject":"02",
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
                "TaxObject":"02",
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
  
    cfdi_object_FacturaGlobal ={
        "Folio": "100",
        "Serie": "B",
        "Currency": "MXN",
        "ExpeditionPlace": "78140",
        "PaymentConditions": "CFDI 4.0 de prueba ",
        "CfdiType": "I",
        "PaymentForm": "03",
        "PaymentMethod": "PUE",
        "Exportation":"01",
        "GlobalInformation":{ 
            "Periodicity":"04",
            "Months":"04",
            "Year":"2022"
        },
        "Receiver": {
            "Rfc": "XAXX010101000",
            "Name": "PUBLICO EN GENERAL",
            "CfdiUse": "S01",
            "TaxZipCode": "78140",
            "FiscalRegime":"616"
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
                "TaxObject":"02",
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

    cfdi_object_FacturaGlobal_mult ={
        "Folio": "100",
        "Serie": "B",
        "Currency": "MXN",
        "ExpeditionPlace": "78140",
        "PaymentConditions": "CFDI 4.0 de prueba ",
        "CfdiType": "I",
        "PaymentForm": "03",
        "PaymentMethod": "PUE",
        "Exportation":"01",
        "GlobalInformation":{ 
            "Periodicity":"04",
            "Months":"04",
            "Year":"2022"
        },
        "Issuer": {
            "Rfc": "EKU9003173C9",
            "Name": "ESCUELA KEMPER URGATE",
            "FiscalRegime": "601"
        },
        "Receiver": {
            "Rfc": "XAXX010101000",
            "Name": "PUBLICO EN GENERAL",
            "CfdiUse": "S01",
            "TaxZipCode": "78140",
            "FiscalRegime":"616"
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
                "TaxObject":"02",
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
                "TaxObject":"02",
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

    cfdi_object_complemento_pago = {
        "Receiver": {
            "Name": "SERVICIOS ADMINISTRATIVOS AXKAN DEL BAJIO S.C",
            "CfdiUse": "P01",
            "Rfc": "XEXX010101000"
        },
        "CfdiType": "P",
        "NameId": "1",
        "Folio": "93",
        "ExpeditionPlace": "51873",
        "Complemento": {
            "Payments": [{
                "Date": "2018-10-04",
                "PaymentForm": "03",
                "Amount": "11142.21",
                "RelatedDocuments": [{
                    "Uuid": "C94C8AF3-C774-4D4C-802E-781411934A6E",
                    "Serie": "BQ",
                    "Folio": "2205",
                    "Currency": "USD",
                    "ExchangeRate": "19.2107",
                    "PaymentMethod": "PUE",
                    "PartialityNumber": "1",
                    "PreviousBalanceAmount": "1160.00",
                    "AmountPaid": "580.00",
                    "ImpSaldoInsoluto": "580.00"
                }]
            }]
        }
    }

    cfdi_object_complemento_terceros={
        "Receiver": {
            "Name": "Jose de Jesus Romero Alvarado",
            "CfdiUse": "G03",
            "Rfc": "ROAJ850914837"
        },
        "CfdiType": "I",
        "NameId": "01",
        "ExpeditionPlace": "45037",
        "PaymentForm": "01",
        "PaymentMethod": "PUE",
        "Decimals": "2",
        "Currency": "MXN",
        "Date": "2019-06-19T12:45:29",
        "Items": [{
            "Quantity": "1",
            "ProductCode": "10121806",
            "UnitCode": "58",
            "Unit": " kilogramo neto",
            "Description": "consumo",
            "IdentificationNumber": "-",
            "UnitPrice": "1000",
            "Subtotal": "1000.00",
            "Taxes": [{
                "Name": "IVA",
                "Rate": "0.16",
                "Total": "160",
                "Base": "1000",
                "IsRetention": "false",
                "IsFederalTax": "true"
            }],
            "Total": "1160.00",
            "Complement": {
                "ThirdPartyAccount": {
                    "Rfc": "ESO1202108R2",
                    "Name": "Expresion en Software",
                    "Taxes": [{
                        "Name": "IVA",
                        "Rate": "0.16",
                        "Amount": "1000"
                    }]
                }
            }
        }]
    }

    cfdi_object_multi_complemento_pago = {
        "Issuer": {
            "FiscalRegime": "601",
            "Rfc": "AAA010101AAA",
            "Name": "EXPRESION EN SOFTWARE"
        },
        "Receiver": {
            "Name": "SERVICIOS ADMINISTRATIVOS AXKAN DEL BAJIO S.C",
            "CfdiUse": "P01",
            "Rfc": "SAA1609301X7"
        },
        "CfdiType": "P",
        "NameId": "1",
        "Folio": "93",
        "ExpeditionPlace": "76140",
        "Complemento": {
            "Payments": [{
                "Date": "2018-10-04",
                "PaymentForm": "03",
                "Amount": "11142.21",
                "RelatedDocuments": [{
                    "Uuid": "C94C8AF3-C774-4D4C-802E-781411934A6E",
                    "Serie": "BQ",
                    "Folio": "2205",
                    "Currency": "USD",
                    "ExchangeRate": "19.2107",
                    "PaymentMethod": "PUE",
                    "PartialityNumber": "1",
                    "PreviousBalanceAmount": "1160.00",
                    "AmountPaid": "580.00",
                    "ImpSaldoInsoluto": "580.00"
                }]
            }]
        }
    }

    cfdi_object_multi_complemento_donativos= {
        "CfdiType": "I",
        "Currency": "MXN",
        "Date": "2019-06-19T13:45:00",
        "ExpeditionPlace": "51873",
        "NameId": "9",
        "Folio": "94",
        "PaymentForm": "12",
        "PaymentMethod": "PUE",
        "Serie": "Nueva",
        "Complemento": {
            "Donation": {
                "AuthorizationDate": "30/01/2019",
                "AuthorizationNumber": "B400-05-08-2014-005",
                "Legend": "El comprobante es un donativo"
            }
        },
        "Items": [{
            "Description": "Cobija de lana y algodon",
            "IdProduct": "LNzPKg5ydGCdkPAr8W1v7Q2",
            "ProductCode": "20102000",
            "IdentificationNumber": "FP114",
            "Quantity": "3",
            "Subtotal": "3000",
            "Total": "3000",
            "Unit": "NO APLICA",
            "UnitCode": "EA",
            "UnitPrice": "1000"
        }],
        "Issuer": {
            "FiscalRegime": "601",
            "Rfc": "AAA010101AAA",
            "Name": "EXPRESION EN SOFTWARE"
        },
        "Receiver": {
            "CfdiUse": "D04",
            "Name": "Abarrotes del centro",
            "Rfc": "XAXX010101000"
        }
    }

    cfdi_object_multi_complemento_terceros = {
        "Issuer": {
            "FiscalRegime": "601",
            "Rfc": "AAA010101AAA",
            "Name": "EXPRESION EN SOFTWARE"
        },
        "Receiver": {
            "Name": "Jose de Jesus Romero Alvarado",
            "CfdiUse": "G03",
            "Rfc": "ROAJ850914837"
        },
        "CfdiType": "I",
        "NameId": "01",
        "ExpeditionPlace": "45037",
        "PaymentForm": "01",
        "PaymentMethod": "PUE",
        "Folio": "95",
        "Currency": "MXN",
        "Date": "2019-06-19T12:45:29",
        "Items": [{
            "Quantity": "1",
            "ProductCode": "10121806",
            "UnitCode": "58",
            "Unit": " kilogramo neto",
            "Description": "consumo",
            "IdentificationNumber": "-",
            "UnitPrice": "1000",
            "Subtotal": "1000.00",
            "Taxes": [{
                "Name": "IVA",
                "Rate": "0.16",
                "Total": "160",
                "Base": "1000",
                "IsRetention": "false",
                "IsFederalTax": "true"
            }],
            "Total": "1160.00",
            "Complement": {
                "ThirdPartyAccount": {
                    "Rfc": "ESO1202108R2",
                    "Name": "Expresion en Software",
                    "Taxes": [{
                        "Name": "IVA",
                        "Rate": "0.16",
                        "Amount": "1000"
                    }]
                }
            }
        }]
    }