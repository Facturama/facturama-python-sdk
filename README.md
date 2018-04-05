# Facturama
Facturama python wrapper https://api.facturama.mx/

## Instalación
```sh
pip install -e git://github.com/Facturama/facturama-python-sdk.git@master#egg=facturama
```




## Crear nuevo Cliente


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

## Listar Clientes:
```python
import facturama

facturama._credentials = ('username', 'password')
customers = facturama.Client.all()

```

## Obtener Detalles de un Cliente:

```python
import facturama

facturama._credentials = ('username', 'password')
customer = facturama.Client.retrieve('98DY-y6qSikkykW2nhp9kw2')

```

## Crear nuevo Producto

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

## Listar Productos:


```python
import facturama

facturama._credentials = ('username', 'password')
products = facturama.Product.all()

```

## Crear nueva Sucursal (Branch Office)
  
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

## Listar Sucursales:

```python
import facturama

facturama._credentials = ('username', 'password')
sucursales = facturama.BranchOffice.all()

```

## Crear nuevo CFDI 3.3

Documentación en https://api.facturama.mx/Docs
 
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


cfdi = facturama.Cfdi.create(cfdi_object)


```

## Descarga CFDI:


```python
import facturama

facturama._credentials = ('username', 'password')
html_file = facturama.Cfdi.get_by_file('html', 'IssuedLite', 'OwMgofF7ZDEM60gerUXudw2')
facturama.api_lite = True
html_name = '{}.html'.format('nombreDelHtml')
with open(html_name, 'wb') as f:
    f.write(base64.urlsafe_b64decode(html_file['Content'].encode('utf-8')))

```

## Cancelar CFDI:

```python
import facturama

facturama._credentials = ('username', 'password')
facturama.api_lite = True
facturama.Cfdi.delete('OwMgofF7ZDEM60gerUXudw1')
```

## Listar CFDI:
Por tipo, keyword, status  mas información en: https://api.facturama.mx/docs/api/GET-Cfdi_type_keyword_status

```python
import facturama

facturama._credentials = ('username', 'password')
lista = facturama.Cfdi.list('issued','Expresion en Software','all')

```

## Enviar CFDI por mail:

```python
import facturama

facturama._credentials = ('username', 'password')
facturama.Cfdi.send_by_email('issued','GgQKVvV84IlgmFCMqJVraQ2','mail@mail.com')

```

## Library Development and Testing

Test de libreria con nose http://nose.readthedocs.io/en/latest/

```sh
$ nosetests
```


## Contributing:
[tingsystems](https://github.com/tingsystems)
