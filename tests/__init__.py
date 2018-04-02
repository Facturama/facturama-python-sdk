import unittest
import random
import facturama


class BaseEndpointTestCase(unittest.TestCase):
    random.seed()

    client = facturama

    customer_object = {
        "Id": "1111000",
        "Email": "test@test.com",
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
        "Rfc": "GARR900630G98",
        "Name": "Pollitux"
    }

    product_object = {
        "Id": "0001",
        "Unit": "PZA",
        "IdentificationNumber": "0001",
        "Name": "Product test1",
        "Description": "Product test 1",
        "Price": 6.0
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

    cfdi_object = {
        "CfdiType": "ingreso",
        "IdBranchOffice": "KI2C2GeiviBPKVZRxX6GLg2",
        "IdClient": "MdkB7dsxLN8XmQGjKHHF4g2",
        "PaymentMethod": "TRANSFERENCIA ELECTRONICA DE FONDOS",
        "PaymentAccountNumber": "5143",
        "Currency": "MXN",
        "Subtotal": 950.66,
        "Discount": 0.0,
        "Total": 1102.76,
        "Items": [
            {
                "IdProduct": "0WV1zSDPmulwL3OGEIbbPw2",
                "Quantity": 2.0,
                "Total": 7.2,
                "TaxPercentage": 0.0,
                "Subtotal": 5.0
            }
        ],
        "Taxes": [
            {
                "Total": 152.1,
                "Name": "IVA",
                "Rate": 16.0,
                "Type": 1
            }
        ]
    }
