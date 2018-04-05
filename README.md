# Facturama
Facturama python wrapper https://api.facturama.mx/

Install
```sh
pip install -e git://github.com/Facturama/facturama-python-sdk.git@master#egg=facturama
```

NOTE: The Wrapper by default use api base of Facturama


Crete new Client


```python
import facturama

facturama._credentials = ('username', 'password')

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
    "Name": "Pollitux",
    "CfdiUse": "P01",
    "TaxResidence": "",
    "NumRegIdTrib": ""
 }
customer = facturama.Client.create(customer_object)
```


Create new Product

```python
import facturama

facturama._credentials = ('username', 'password')


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

product = facturama.Product.create(product_object)

```
 
Create new Branch Office
  
```python
import facturama 

facturama._credentials = ('username', 'password')

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

branch = facturama.BranchOffice.create(branch_office_object)

```

Create new Cfdi

You can see https://api.facturama.mx/Docs for more information
 
```python
import facturama 

facturama._credentials = ('username', 'password')

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
            "Rfc": "ESO1202108R2",
            "Name": "SinDelantal Mexico"
        },
        "Receiver": {
            "Rfc": "XAXX010101000",
            "Name": "RADIAL SOFTWARE SOLUTIONS",
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


cfdi = facturama.Cfdi.create(cfdi_object) # create cfdi version 3.3 and api-lite

```

## Library Development and Testing

You can test the facturama library with nose from the facturama library root:

```sh
$ nosetests
```


## Contributing:
[tingsystems](https://github.com/tingsystems)
