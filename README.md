# Facturama Python SDK

> [NOTE] This document is also available in [English].
>
> Librería para consumir la API Web y API Multiemisor de [Facturama](https://api.facturama.mx/).
>
> Puedes consultar la guía completa de la [API](https://apisandbox.facturama.mx/guias).
## Crear cuenta de usuario

> Crear una cuenta de usuario en el ambiente de prueba [Sandbox](https://dev.facturama.mx/api/login) 
>
> Para API Web, realiza la configuración básica usando RFC de pruebas **"EKU9003173C9"**, más información [aquí](https://apisandbox.facturama.mx/guias/perfil-fiscal).
>
> Sellos digitales de prueba (CSD), [aquí](https://github.com/rafa-dx/facturama-CSD-prueba). 
## Inicio Rápido

### Instalación
```sh
pip install -e git+https://github.com/Facturama/facturama-python-sdk.git@master#egg=facturama
```

### Incluir librería

```sh
import facturama
```

### Credenciales de usuario

```sh
facturama._credentials = ('username', 'password')
```

## API Web

> Creación de CFDIs con un único emisor, (el propietario de la cuenta, cuyo perfil fiscal se tiene configurado)
> 
> *Todas las operaciones son reflejadas en la plataforma web.*
### Operaciones API Web
- Crear, Consultar Cancelar CFDI así como descargar XML, PDF y envió de estos por mail.
- Consultar Perfil y Suscripción actual.
- CRUD de Productos, Clientes, Sucursales y Series.

Nota: Se recomienda incluir el folio y la fecha de expedición para todas las facturas.

## API Multiemisor

> Creacion de CFDIs con multiples emisores.
>
> *Las operaciones NO se reflejan en la plataforma web.*
### Operaciones API Multiemisor

- Crear, Consultar, Cancelar descarga de XML.
- CRUD de CSD (Certificados de los Sellos Digitales).



# Clientes
## Crear nuevo cliente
```
customer_object = {
        "Id": "1111000",
        "Email": "test@test.com",
        "Address": {
            "Street": "Fenix One",
            "ExteriorNumber": "1",
            "InteriorNumber": "0",
            "Neighborhood": "Call me",
            "ZipCode": "29950",
            "Locality": "Xiquilpan",
            "Municipality": "Jiquilpan",
            "State": "MICHOACAN",
            "Country": "MX"
        },
        "Rfc": "KAHO641101B39",
        "Name": "OSCAR KALA HAAK",
        "CfdiUse": "S01",
        "TaxZipCode": "29950",
        "FiscalRegime": "605",

    }

cliente = facturama.Client.create(customer_object)
```

## Mostrar clientes

### Mostrar todos
```
customers = facturama.Client.all()
for x in customers:
    print(x)
```
    
### Mostrar cliente por ID
```
print(facturama.Client.retrieve("HN10gA7YPgrCgjKfSnNn0g2")) #Para obtener el ID de un cliente, es necesario mostrar todos los clientes y buscarlo manualmente para recuperar el valor.
```

### Lista paginada de clientes
```
lst_clients = facturama.Client.list(0, 100, "")
#Total de registros
print(lst_clients["recordsTotal"])
#Total de registros filtrados
print(lst_clients["recordsFiltered"])
#Muestra el contenido del registro '0'
print(lst_clients["data"][0])
#Muestra el ID del del registro '0'
print(lst_clients["data"][0]['Id'])
```

## Editar cliente
```
customer_object = {
        "Id": "1111000",
        "Email": "testUpdate@test.com",
        "Address": {
            "Street": "Fenix One",
            "ExteriorNumber": "1",
            "InteriorNumber": "0",
            "Neighborhood": "Call me, but not today",
            "ZipCode": "29950",
            "Locality": "Xiquilpan",
            "Municipality": "Jiquilpan",
            "State": "MICHOACAN",
            "Country": "MX"
        },
        "Rfc": "KAHO641101B39",
        "Name": "OSCAR KALA HAAK",
        "CfdiUse": "S01",
        "TaxZipCode": "29950",
        "FiscalRegime": "605",

}

updateCostumer = facturama.Client.update(customer_object,"DF0734DccXct6-LvsmgOJg2") #Recibe el ID del cliente a modificar como segundo argumento.
```

## Eliminar cliente
```
#facturama.Client.delete("DF0734DccXct6-LvsmgOJg2") #Se debe de eliminar el cliente con su ID.
```


# Productos

## Agregar producto
```
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

## Mostrar productos

### Mostrar todos
```
products = facturama.Product.all()
for x in products:
    print(f"\n", x)
```

### Mostrar por ID
```
print(facturama.Product.retrieve("FkoyDzFYagNiB15uTrVX4Q2")) #Para obtener el ID de un producto, es necesario mostrar todos los productos y buscarlo manualmente para recuperar el valor.
```

### Lista paginada de productos
```
lst_product = facturama.Product.list(0, 100, "")
#Total de registros
print(lst_product["recordsTotal"])
#Total de registros filtrados
print(lst_product["recordsFiltered"])
#Muestra el contenido del registro '0'
print(lst_product["data"][1])
#muestra el ID del del registro '0'
print(lst_product["data"][0]['Id'])
```

## Editar producto
```
product_object = {
"Unit": "Servicio",
      "UnitCode": "E48",
      "IdentificationNumber": "WEB003",
      "Name": "Sitio Web Destilación",
      "Description": "Sitio web para venta de productos destilados",
      "Price": 9000,
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

updateProduct = facturama.Product.update(product_object, "0PS3VO1l0qUpfEs3wJDHRw2") #Recibe el ID del producto a modificar como segundo argumento.
```

## Eliminar un producto
```
facturama.Product.delete("SfJ9YoW4Z-fo91shQqgVRA2")
```

# Sucursales (Branch Offices)

## Crear nueva sucursal
```
branch_office_object = {
    "Name": "Capsule Corp",
    "Description": "Secret Capsule Corp HQ",
    "Address": {
        "Street": "Namek",
        "ExteriorNumber": "1",
        "InteriorNumber": "0",
        "Neighborhood": "Rock 3",
        "ZipCode": "59510",
        "Locality": "Xiquilpan",
        "Municipality": "Jiquilpan",
        "State": "MICHOACAN",
        "Country": "MX"
    },
}

branch = facturama.BranchOffice.create(branch_office_object)
```

## Mostrar sucursales

### Mostrar todas
```
sucursales = facturama.BranchOffice.all()

for x in sucursales:
    print(x)
```

### Mostrar sucursal por ID
```
print(facturama.BranchOffice.retrieve('NvLlLjpITbl1pMrGlo45mA2')) #Para obtener el ID de una sucursal, es necesario mostrar todas las sucursales y buscar una manualmente para recuperar el valor.
```

## Actualizar sucursal
```
branch_office_object = {
    "Id": "J0in7OLXwv4NddnqfwUjOA2",
    "Name": "Red Patrol INC",
    "Description": "We are not evil",
    "Address": {
        "Street": "Secret",
        "ExteriorNumber": "1",
        "InteriorNumber": "0",
        "Neighborhood": "None",
        "ZipCode": "59510",
        "Locality": "Secret",
        "Municipality": "Jiquilpan",
        "State": "MICHOACAN",
        "Country": "MX"
    },
}

facturama.BranchOffice.update(branch_office_object, "J0in7OLXwv4NddnqfwUjOA2") #Recibe el ID de la sucursal a modificar como segundo argumento.
```

## Eliminar sucursal
```
facturama.BranchOffice.delete("OTU0ichKzs4A35vGYN6yqw2")
```

# Series

## Crear serie
```
serie_object = {
    "IdBranchOffice": "A6A2ECMzMMuij5aFI4_jpA2",
    "Name": "ADB",
    "Description": "Para el control de inventarios 2",
    "Folio": 207
}

facturama.BranchOffice.Serie.newSerie("A6A2ECMzMMuij5aFI4_jpA2", serie_object)
```

## Mostrar series de una sucursal
```
print(facturama.BranchOffice.Serie.retrieve("A6A2ECMzMMuij5aFI4_jpA2")) #Recibe el ID de la sucursal
```

## Eliminar serie
```
facturama.BranchOffice.Serie.delete("A6A2ECMzMMuij5aFI4_jpA2/ADB")
```

# CFDI 4.0
## Crear factura de ingreso
```
crear_factura = {
    "Folio": "10",
    "Date": "2023-05-09T10:00",
    "Currency": "MXN",
    "ExpeditionPlace": "65000",
    "CfdiType": "I",
    "PaymentForm": "03",
    "PaymentMethod": "PUE",
    "TaxZipCode": "26015",
    "Receiver": {
        "Rfc": "ZUÑ920208KL4",
        "Name": "ZAPATERIA URTADO ÑERI",
        "CfdiUse": "G03",
        "FiscalRegime": "601",
        "TaxZipCode": "77060"
    },
    "Items": [
        {
            "ProductCode": "10101504",
            "IdentificationNumber": "EDL",
            "Description": "Estudios de viabilidad",
            "Unit": "NO APLICA",
            "UnitCode": "MTS",
            "UnitPrice": 70.0,
            "Quantity": 2.0,
            "Subtotal": 140.0,
            "TaxObject": "02",  # Nuevos elementos para CFDi 4.0
        "Taxes": [
                {
                    "Total": 22.4,
                    "Name": "IVA",
                    "Base": 140.0,
                    "Rate": 0.16,
                    "IsRetention": False
                }
            ],
            "Total": 162.4
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
            "TaxObject": "01",
            "Total": 1500.0
        }
    ]
}
cfdi = facturama.Cfdi.create3(crear_factura)
```

## Crear factura de egreso
```
f_egreso = {
    "Folio": "11",
    "Date": "2023-05-09T10:25",
    "Currency": "MXN",
    "ExpeditionPlace": "65000",
    "CfdiType": "E",
    "PaymentForm": "99",
    "PaymentMethod": "PPD",
    "Receiver": {
        'Rfc': 'CACX7605101P8',
        'CfdiUse': 'CP01',
        'Name': 'XOCHILT CASAS CHAVEZ',
        'FiscalRegime': '605',
        'TaxZipCode': '10740'
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
            "TaxObject": "02",  # Nuevos elementos para CFDi 4.0
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
            "TaxObject": "01",
            "Total": 1500.0
        }
    ]
}
cfdi = facturama.Cfdi.create3(f_egreso)
```
## Crear factura con pago en parcialidades
```
f_ppd = {
    "Folio": "501",
    'Date': '2023-05-08T10:27',
    'PaymentForm': '99',
    'PaymentConditions': 'CREDITO A SIETE DIAS',
    'Currency': 'MXN',
    'CfdiType': 'I',
    'PaymentMethod': 'PPD',
    'ExpeditionPlace': '65000',
    'Receiver':
    {
        'Rfc': 'CACX7605101P8',
        'CfdiUse': 'CP01',
        'Name': 'XOCHILT CASAS CHAVEZ',
        'FiscalRegime': '605',
        'TaxZipCode': '10740',
        'Address':
        {
            'Street': 'Guadalcazar del receptor',
            'ExteriorNumber': '300',
            'InteriorNumber': 'A',
            'Neighborhood' : 'Las lomas',
            'ZipCode': '65000',
            'Municipality': 'San Luis Potosi',
            'State': 'San Luis Potosi',
            'Country': 'México'
        }
    },
    'Items': [
       {
            'ProductCode': '10101504',
            'IdentificationNumber': 'EDL',
            'Description': 'Estudios de viabilidad',
            'Unit': 'NO APLICA',
            'UnitCode': 'MTS',
            'UnitPrice': 50.0,
            'Quantity': 2.0,
            'Subtotal': 100.0,
            "TaxObject": "02",
            'Taxes': [
               {
                   'Total': 16.0,
                   'Name': 'IVA',
                   'Base': 100.0,
                   'Rate': 0.16,
                   'IsRetention': False,
               }
            ],
            'Total': 116.0,
       }
    ]
}
cfdi = facturama.Cfdi.create3(f_ppd)
```

## Crear factura de comercio exterior
```
f_comext = {
        "Receiver": {
            "Name": " JOSE ALBERTO  LOPEZ CAMARILLO",
            "CfdiUse": "S01",
            "Rfc": "XEXX010101000",
            "FiscalRegime": "616",
            "TaxRegistrationNumber": "123456789",
            "TaxResidence": "USA",
            "TaxZipCode": "78116"
         },
        "CfdiType": "I",
        "NameId": "26",
        "ExpeditionPlace": "78116",
        "Folio": "102",
        "Date": "2023-05-08T09:14",
        "PaymentForm": "01",
        "PaymentMethod": "PUE",
        "Exportation": "02",
        "Items": [{
            "IdentificationNumber": "CX-000988",
      	    "Quantity": "1",
      	    "ProductCode": "44121706",
      	    "UnitCode": "DPC",
            "Unit": "PIEZA",
            "TaxObject": "02",
            "Description": "Es un lapiz",
            "UnitPrice": "100",
            "Subtotal": "100.00",
            "Taxes": [{
                "Name": "IVA",
                "Rate": "0.16",
                "Total": "16",
                "Base": "100",
                "IsRetention": "false"
            }],
            "Total": "116.00"
        }],
        "Complemento": {
            "ForeignTrade": {
                "Issuer": {
                    "Address": {
                        "Street": "Cañada de Gomez",
                        "ExteriorNumber": "110",
                        "InteriorNumber": "A",
                        "Reference": "-",
                        "Municipality": "028",
                        "State": "SLP",
                        "Country": "MEX",
                        "ZipCode": "78216"
                    }
                },
                "Receiver": {
                    "Address": {
                        "Street": "Thompson Drive",
                        "ExteriorNumber": "3994",
                        "InteriorNumber": "A",
                        "Neighborhood": None,
                        "Locality": "Oakland",
                        "Municipality": "028",
                        "State": "CA",
                        "Country": "USA",
                        "ZipCode": "94612"
                    }
                },
                "Commodity": [{
                    "SpecificDescriptions": [{
                        "Brand": "Volkswagen",
                         "Model": "Polo",
                         "SubModel": "GTI",
                         "SerialNumber": "4556789542156"
                    }],
                    "IdentificationNumber": "CX-000988",
                    "TariffFraction": "9609100100",
                    "CustomsQuantity": "1",
                    "CustomsUnit": "06",
                    "CustomsUnitValue": "10.60"
                }],
                "OperationType": "2",
                "RequestCode": "A1",
                "OriginCertificate": "true",
                "Incoterm": "CFR",
                "Subdivision": 1,
                "ExchangeRateUSD": "17.9975", #Este valor cambia diariamente, precio del dólar.
                "TotalUSD": "1",
                "OriginCertificateNumber": "20001000000300022817",
                "ReliableExporterNumber": None,
                "Observations": "sample string 8"
            }
        }
    }
cfdi = facturama.Cfdi.create3(f_comext)
```

## Crear factura de donativos
```
donativo = {
    "Currency": "MXN",
    "ExpeditionPlace": "65000",
    "CfdiType": "I",
    "PaymentForm": "03",
    "PaymentMethod": "PUE",
    "TaxZipCode": "26015",
    "Folio": "20"
    "Date" : "2023-05-01T13:46:00",
    "Receiver":
    {
        "Rfc": "ZUÑ920208KL4",
        "Name": "ZAPATERIA URTADO ÑERI",
        "CfdiUse": "G03",
        "FiscalRegime": "601",
        "TaxZipCode": "77060"
    },
    "Complemento": {
        "Donation": {
            "AuthorizationDate": "1/05/2023",
            "AuthorizationNumber": "B400-05-08-2014-005",
            "Legend": "El comprobante es un donativo"
        }
    },
    "Items":
    [{
        "ProductCode": "60121535",
        "Description": "Es una goma",
        "Unit": "NO APLICA",
        "UnitCode": "H87",
        "UnitPrice": 10.0,
        "Quantity": 200000.0,
        "Subtotal": 2000000.0,
        "TaxObject": "01",
        "Total": 2000000.0
    }]
}

cfdi = facturama.Cfdi.create3(donativo)
```

## Crear factura para IEDU (Instituciones educativas)
```
iedu = {
    "CfdiType": "I",
    "Currency": "MXN",
    "Folio": "33"
    "Date": "2023-05-03T10:00",
    "ExpeditionPlace": "65000",
    "NameId": "1",
    "PaymentForm": "01",
    "PaymentMethod": "PUE",
    "Receiver": {
        "Rfc": "ZUÑ920208KL4",
        "Name": "ZAPATERIA URTADO ÑERI",
        "CfdiUse": "G03",
        "FiscalRegime": "601",
        "TaxZipCode": "77060"
    },
    "Items": [
        {
            "Complement": {
                "EducationalInstitution": {
                    "AutRvoe" : "234",
                    "Curp": "ROAJ850914HSPMLS08",
                    "EducationLevel": "Profesional técnico",
                    "StudentsName": "Pruebas Complementos"
                }
            },
            "Taxes": [
                {

                    "Base": "100",
                    "IsRetention": "false",
                    "Name": "IVA",
                    "Rate": "0.16",
                    "Total": "16"
                }
            ],
            "Description": "producto prueba complemento IEDU",
            "IdProduct": "lLro-ivFuvcTbH32gFSQ7w2",
            "TaxObject": "02",
            "ProductCode": "86121503",
            "Quantity": "1",
            "Subtotal": "100.00",
            "Total": "116.00",
            "Unit": "Unidad de servicio",
            "UnitCode": "E48",
            "UnitPrice": "100.00"
        }
    ]
}

cfdi = facturama.Cfdi.create3(iedu)
```

## Crear factura de terceros
```
terceros = {
  "Currency": "MXN",
  "ExpeditionPlace": "65000",
  "PaymentConditions": "CREDITO A SIETE DIAS",
  "Folio": "18",
  "Date": "2023-05-03T09:08",
  "CfdiType": "I",
  "PaymentForm": "01",
  "PaymentMethod": "PUE",
  "Observations":"Elemento Observaciones solo visible en PDF",
  "Receiver":
    {
        'Rfc': 'CACX7605101P8',
        'CfdiUse': 'CP01',
        'Name': 'XOCHILT CASAS CHAVEZ',
        'FiscalRegime': '605',
        'TaxZipCode': '10740',
    },
  "Items": [
    {
      "ProductCode": "10101504",
      "IdentificationNumber": "EDL",
      "Description": "Estudios de laboratorio",
      "Unit": "NO APLICA",
      "UnitCode": "MTS",
      "UnitPrice": 50,
      "Quantity": 2.0,
      "Subtotal": 100,
      "TaxObject":"02",
      "Taxes": [
        {
          "Total": 16,
          "Name": "IVA",
          "Base": 100,
          "Rate": 0.16,
          "IsRetention": False
        }
      ],
      "Total": 116,
      "ThirdPartyAccount":{
            "Rfc":"CACX7605101P8",
            "Name":"XOCHILT CASAS CHAVEZ",
            "FiscalRegime":"616",
            "TaxZipCode":"10740"
        }
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

cfdi = facturama.Cfdi.create3(terceros)
```

## Crear factura para kits
```
kit = {
    "CfdiType": "I",
    "PaymentForm": "03",
    "PaymentMethod": "PUE",
    "Folio": "25",
    "Date": "2023-05-05T09:47",
    "ExpeditionPlace": "65000",
    "Receiver": {
        "Rfc": "CACX7605101P8",
        "CfdiUse": "CP01",
        "Name": "XOCHILT CASAS CHAVEZ",
        "FiscalRegime": "605",
        "TaxZipCode": "10740",
    },
    "Items": [
        {
            "TaxObject": "02",
            "ProductCode": "60131517",
            "Description": "Estuche para guitarra",
            "UnitCode": "H87",
            "Quantity": 1,
            "UnitPrice": 4877,
            "Subtotal": 4877,
            "Taxes": [
                {
                    "Total": 780.32,
                    "Name": "IVA",
                    "Base": 4877,
                    "Rate": 0.16,
                    "IsRetention": False
                }
            ],
            "Parts": [
                {
                    "Quantity": 1,
                    "UnitCode": "H87",
                    "ProductCode": "60131303",
                    "Description": "Guitarra acústica",
                    "UnitPrice": 3800
                }
            ],
            "Total": 5657.32
        }
    ]
}

cfdi = facturama.Cfdi.create3(kit)
```

## Crear complemento de pago
```
complemento = {
    "CfdiType": "P",
    "NameId": "14",
    "Date": "2023-05-07T09:08",
    "Folio": "93",
    "ExpeditionPlace": "65000",
  'Receiver': {
      'Rfc': 'CACX7605101P8',
      'CfdiUse': 'CP01',
      'Name': 'XOCHILT CASAS CHAVEZ',
      'FiscalRegime': '605',
      'TaxZipCode': '10740'
    },
    "Complemento": {
        "Payments": [
            {
                "Date": "2023-05-01T00:00:00.000Z",
                "Currency": "MXN",
                "Amount": "100",
                "PaymentForm": "01",
                "RelatedDocuments": [
                    {
                        "Uuid": "a7c9ed1e-865a-4433-93d6-13bfeecae0af", #ID de la factura relacionada
                        "Currency": "MXN",
                        "PaymentMethod": "PUE",
                        "PartialityNumber": "1",
                        "PreviousBalanceAmount": "116",
                        "AmountPaid": "100",
                        "TaxObject": "01"
                    }
                ]
            }
        ]
    }
}

cfdi = facturama.Cfdi.create3(complemento)
```

## Carta porte 2.0
```
c_porte2 = {
    "Folio": "77",
    "Date": "2023-05-03T11:50",
    "ExpeditionPlace": "65000",
    "NameId": 33,
    "CfdiType": "T",
    "Currency": "MXN",
    "Receiver": {
        "Rfc": "EKU9003173C9",
        "Name": "ESCUELA KEMPER URGATE",
        "CfdiUse": "S01",
        "FiscalRegime": "601",
        "TaxZipCode": "26015"
    },
    "Items": [
        {
            "ProductCode": "78101800",
            "Description": "Transporte de carga por carretera",
            "UnitCode": "E48",
            "UnitPrice": 0,
            "Quantity": 1,
            "Subtotal": 0,
            "TaxObject":"01",
            "Total": 0
        }
    ],
    "Complemento": {
        "CartaPorte20": {
            "TranspInternac": "No",
            "Ubicaciones": [
                {
                    "TipoUbicacion": "Origen",
                    "RFCRemitenteDestinatario": "EKU9003173C9",
                    "FechaHoraSalidaLlegada": "25/11/2021",
                    "DistanciaRecorrida": 1,
                    "Domicilio": {
                        "Calle": "Puebla No.1 ",
                        "CodigoPostal": "28239",
                        "Colonia": "0342",
                        "Estado": "COL",
                        "Municipio": "007",
                        "Localidad": "02",
                        "Pais": "MEX"
                    }
                },
                {
                    "TipoUbicacion": "Destino",
                    "RFCRemitenteDestinatario": "EKU9003173C9",
                    "FechaHoraSalidaLlegada": "25/11/2021",
                    "DistanciaRecorrida": 1,
                    "Domicilio": {
                        "Calle": "Morelos No.1 ",
                        "CodigoPostal": "28219",
                        "Colonia": "0575",
                        "Estado": "COL",
                        "Municipio": "007",
                        "Localidad": "02",
                        "Pais": "MEX"
                    }
                }
            ],
            "Mercancias": {
                "UnidadPeso": "KGM",
                "Mercancia": [
                    {
                        "Cantidad": "1",
                        "BienesTransp": "10101500",
                        "Descripcion": "Animales vivos de granja",
                        "ClaveUnidad": "KGM",
                        "PesoEnKg": "1"
                    }
                ],
                "Autotransporte": {
                    "PermSCT": "TPAF01",
                    "NumPermisoSCT": "123abc",
                    "Seguros": {
                        "AseguraRespCivil": "Seguros SA",
                        "PolizaRespCivil": "123123"
                    },
                    "IdentificacionVehicular": {
                        "AnioModeloVM": "1990",
                        "ConfigVehicular": "C2R3",
                        "PlacaVM": "XXX000"
                    },
                    "Remolques": [
                        {
                            "SubTipoRem": "CTR001",
                            "Placa": "21132h"
                        }
                    ]
                }
            },
            "FiguraTransporte": [
                {
                    "TipoFigura": "01",
                    "RFCFigura": "GARH990725QI7",
                    "NombreFigura": "Hegar",
                    "NumLicencia": "000001"
                },
                {
                    "TipoFigura": "02",
                    "RFCFigura": "GARH990725QI7",
                    "NombreFigura": "Hegar Jose",
                    "PartesTransporte": [{
                        "ParteTransporte": "PT01"
                    }],
                        "Domicilio": {
                        "Calle": "Morelos No.1 ",
                        "CodigoPostal": "28219",
                        "Colonia": "0575",
                        "Estado": "COL",
                        "Municipio": "007",
                        "Localidad": "02",
                        "Pais": "MEX"
                    }
                }
            ]
        }
    }
}

cfdi = facturama.Cfdi.create3(c_porte2)
```
## Crear factura para público en general
```
f_general = {
    "Currency": "MXN",
    "Folio": "68",
    "CfdiType": "I",
    "PaymentForm": "03",
    "PaymentMethod": "PUE",
    "OrderNumber": "TEST-001",
    "ExpeditionPlace": "65000",
    "Date": "2023-05-09T12:55",
    "PaymentConditions": "VENDA DE MOSTRADOR",
    "Observations": "Elemento Observaciones solo visible en PDF",
    "Exportation": "01",
    "Receiver": {
        "Rfc": "XAXX010101000",
        "Name": "PÚBLICO EN GENERAL",
        "CfdiUse": "S01",
        "TaxZipCode": "65000",
        "FiscalRegime": "616"
    },
    "Items": [
        {
            "ProductCode": "10101504",
            "IdentificationNumber": "EDL",
            "Description": "Estudios de laboratorio",
            "Unit": "NO APLICA",
            "UnitCode": "MTS",
            "UnitPrice": 50,
            "Quantity": 2.0,
            "Subtotal": 100,
            "TaxObject": "02",
            "Taxes": [
                {
                    "Total": 16,
                    "Name": "IVA",
                    "Base": 100,
                    "Rate": 0.16,
                    "IsRetention": False
                }
            ],
            "Total": 116
        }
    ]
}

cfdi = facturama.Cfdi.create3(f_general)
```

## Nómina
```
nomina = {
    "NameId": 1,
    "ExpeditionPlace": "78000",
    "CfdiType": "N",
    "Folio": "47",
    "PaymentMethod": "PUE",
    "Receiver": {
        "Rfc": "CACX7605101P8",
        "Name": "XOCHILT CASAS CHAVEZ",
        "CfdiUse": "CN01",
        "FiscalRegime": "605",
        "TaxZipCode": "10740"
    },
    "Complemento": {
        "Payroll": {
            "Type": "O",
            "PaymentDate": "2023-05-10T13:43:59.4011985-06:00",
            "InitialPaymentDate": "2023-05-10T13:43:59.4011985-06:00",
            "FinalPaymentDate": "2023-05-10T13:43:59.4011985-06:00",
            "DaysPaid": 5,
            "Issuer": {
                "EmployerRegistration": "B5510768108"
            },
            "Employee": {
                "Curp": "AAAA110313HCMLNS09",
                "SocialSecurityNumber": "1234567890",
                "StartDateLaborRelations": "2019-01-15T13:43:59.3952019-06:00",
                "ContractType": "01",
                "RegimeType": "02",
                "Unionized": True,
                "TypeOfJourney": "01",
                "EmployeeNumber": "012345672ST",
                "Department": "Software and Deployments",
                "Position": "Developer",
                "PositionRisk": "1",
                "FrequencyPayment": "01",
                "Bank": "SANTANDER",
                "BankAccount": "1234567890",
                "BaseSalary": 1,
                "DailySalary": 1,
                "FederalEntityKey": "SLP"
            },
            "Perceptions": {
                "Details": [
                    {
                        "PerceptionType": "001",
                        "Code": "00500",
                        "Description": "Salario Diario",
                        "TaxedAmount": 4,
                        "ExemptAmount": 5
                    }
                ]
            },
            "Deductions": {
                "Details": [
                    {
                        "DeduccionType": "001",
                        "Code": "IMSS",
                        "Description": "Seguridad Social",
                        "Amount": 4
                    },
                    {
                        "DeduccionType": "002",
                        "Code": "ISR",
                        "Description": "Impuesto Sobre la Renta",
                        "Amount": 2
                    },
                    {
                        "DeduccionType": "003",
                        "Code": "RETIRO",
                        "Description": "Aportacion a retiro",
                        "Amount": 1
                    }
                ]
            },
            "OtherPayments": [
                {
                    "OtherPaymentType": "002",
                    "Code": "00101",
                    "Description": "otro pago",
                    "Amount": 110,
                    "EmploymentSubsidy": {
                        "Amount": 110
                    }
                }
            ]
        }
    }
}

cfdi = facturama.Cfdi.create3(nomina)
```

## Proceso para anticipo

Al utilizar una nota de crédito deberás emitir tres comprobantes fiscales y los pasos a seguir son los siguientes:

1. Se elabora Factura de venta (CFDI de Ingreso) por el valor del anticipo recibido. (Anticipo)
2. Se realiza la venta o prestación de servicio y se expide la correspondiente Factura de venta (CFDI de Ingreso) por el valor total de la operación. (Total_Operación)
3. Se crea una Nota de crédito (CFDI de Egreso) para aplicar el anticipo al saldo remanente del total de la operación. (Nota de Crédito)
Adjunto ejemplos para anticipos y venta al público en general.

### Anticipo
```
anticipo = {
    "NameId": "1",
    "Currency": "MXN",
    "Folio": "407",
    "CfdiType": "I",
    "PaymentForm": "03",
    "PaymentMethod": "PUE",
    "OrderNumber": "TEST-001",
    "ExpeditionPlace": "78000",
    "Date": "2023-05-09T12:55:02-06:00",
    "PaymentConditions": "Anticipo",
    "Observations": "Elemento Observaciones solo visible en PDF",
    "Exportation": "01",
    "Receiver": {
        "Rfc": "URE180429TM6",
        "CfdiUse": "G03",
        "Name": "UNIVERSIDAD ROBOTICA ESPAÑOLA",
        "FiscalRegime": "601",
        "TaxZipCode": "65000"
    },
    "Items": [
        {
            "ProductCode": "84111506",
            "IdentificationNumber": None,
            "Description": "Anticipo del bien o servicio ",
            "Unit": "NO APLICA",
            "UnitCode": "ACT",
            "UnitPrice": 100,
            "Quantity": 1.0,
            "Subtotal": 100,
            "TaxObject": "02",
            "Taxes": [
                {
                    "Total": 16,
                    "Name": "IVA",
                    "Base": 100,
                    "Rate": 0.16,
                    "IsRetention": False
                }
            ],
            "Total": 116
        }
    ]
}

cfdi = facturama.Cfdi.create3(anticipo)
```

### Total de operación
```
total ={
    "NameId": "1",
    "Currency": "MXN",
    "Folio": "359",
    "CfdiType": "I",
    "PaymentForm": "03",
    "PaymentMethod": "PUE",
    "OrderNumber": "TEST-001",
    "ExpeditionPlace": "78000",
    "Date": "2023-05-09T13:02:08-06:00",
    "PaymentConditions": "venta",
    "Observations": "Elemento Observaciones solo visible en PDF",
    "Exportation": "01",
    "Relations": {
        "Type": "07",
        "Cfdis": [
            {
                "Uuid": "72184cc7-cf48-4846-a4fb-a9ebd5101797"
            }
        ]
    },
    "Receiver": {
        "Rfc": "URE180429TM6",
        "CfdiUse": "G03",
        "Name": "UNIVERSIDAD ROBOTICA ESPAÑOLA",
        "FiscalRegime": "601",
        "TaxZipCode": "65000"
    },
    "Items": [
        {
            "ProductCode": "10101504",
            "IdentificationNumber": "EDL",
            "Description": "Estudios de laboratorio",
            "Unit": "NO APLICA",
            "UnitCode": "MTS",
            "UnitPrice": 300,
            "Quantity": 1.0,
            "Subtotal": 300,
            "TaxObject": "02",
            "Taxes": [
                {
                    "Total": 48,
                    "Name": "IVA",
                    "Base": 300,
                    "Rate": 0.16,
                    "IsRetention": False
                }
            ],
            "Total": 348
        }
    ]
}

cfdi = facturama.Cfdi.create3(total)
```

### Nota de crédito
```
credit_bill = {
    "NameId": "2",
    "Folio": "247",
    "CfdiType": "E",
    "Currency": "MXN",
    "PaymentForm": "30",
    "PaymentMethod": "PUE",
    "OrderNumber": "TEST-001",
    "ExpeditionPlace": "78000",
    "Date": "2023-05-09T13:07:04-06:00",
    "Observations": "Ejemplo de nota de credito",
    "PaymentConditions": "Anticipo",
    "Exportation": "01",
    "Relations": {
        "Type": "07",
        "Cfdis": [
            {
                "Uuid": "72184cc7-cf48-4846-a4fb-a9ebd5101797"
            }
        ]
    },
    "Receiver": {
        "Rfc": "URE180429TM6",
        "CfdiUse": "G03",
        "Name": "UNIVERSIDAD ROBOTICA ESPAÑOLA",
        "FiscalRegime": "601",
        "TaxZipCode": "65000"
    },
    "Items": [
        {
            "ProductCode": "84111506",
            "IdentificationNumber": None,
            "Description": "Anticipo del bien o servicio ",
            "Unit": "NO APLICA",
            "UnitCode": "ACT",
            "UnitPrice": 100,
            "Quantity": 1.0,
            "Subtotal": 100,
            "TaxObject": "02",
            "Taxes": [
                {
                    "Total": 16,
                    "Name": "IVA",
                    "Base": 100,
                    "Rate": 0.16,
                    "IsRetention": False
                }
            ],
            "Total": 116
        }
    ]
}

cfdi = facturama.Cfdi.create3(credit_bill)
```

## Mostrar facturas
### Mostrar todas las facturas
```
facturas = facturama.Cfdi.listAll()
```

### Mostrar facturas por estado y receptor
```
facturas = facturama.Cfdi.list('issued','XOCHILT CASAS CHAVEZ','all')

for x in facturas:
     print(x)
```

## Descargar facturas
### Descargar XML
```
xml = facturama.Cfdi.saveAsXML("x9-38Z-Gl66oWWX9uetbcQ2", "EjemploFact.xml")
```
### Descargar HTML
```
html = facturama.Cfdi.saveAsHtml("x9-38Z-Gl66oWWX9uetbcQ2", "EjemploFact.html")
```

### Descargar PDF
```
pdf = facturama.Cfdi.saveAsPdf("x9-38Z-Gl66oWWX9uetbcQ2", "EjemploFact.pdf")
```

## Mandar factura por correo electrónico
```
facturama.Cfdi.send_by_email('issued', "x9-38Z-Gl66oWWX9uetbcQ2", 'ejemplo@freshbooks.com')
```

## Eliminar facturas
```
facturama.Cfdi.delete('rY0ZgPPdcYlmJepd6k-jgw2','issued', '02', '69615e85-4cc9-4830-8c41-9d6dcaad58d3') #Recibe el ID de la factura como primer argumento y el UUID de la factura como último argumento
```

# Multiemisor

## CFDI 4.0
```
{
    "NameId": null,
    "LogoUrl": "https://m.media-amazon.com/images/I/51zLZbEVSTL._AC_SX569_.jpg",
    "Date": "2023-05-15 12:48",
    "Serie": null,
    "PaymentAccountNumber": null,
    "CurrencyExchangeRate": null,
    "Currency": "MXN",
    "ExpeditionPlace": "78000",
    "PaymentConditions": null,
    "Relations": null,
    "Folio": "20",
    "CfdiType": "I",
    "PaymentForm": "28",
    "PaymentMethod": "PUE",
    "Issuer": {
        "FiscalRegime": "601",
        "Rfc": "EKU9003173C9",
        "Name": "ESCUELA KEMPER URGATE",
        "Address": null
    },
    "Receiver": {
        "Id": null,
        "Rfc": "IAÑL750210963",
        "Name": "LUIS IAN ÑUZCO",
        "CfdiUse": "CP01",
        "FiscalRegime": "605",
        "TaxZipCode": "30230",
        "TaxRegistrationNumber": null,
        "Address": null
    },
    "Items": [
        {
            "IdProduct": null,
            "ProductCode": "81112501",
            "IdentificationNumber": null,
            "SKU": null,
            "Description": "Licencia Mensual Parrot Connect: Ríos Ceviches Mamalones (MTY)",
            "Unit": "Unidad de servicio.",
            "UnitCode": "E48",
            "UnitPrice": 1200.0,
            "Quantity": 1,
            "Subtotal": 1200.0,
            "Discount": null,
            "TaxObject": "02",
            "Taxes": [
                {
                    "Total": 192.0,
                    "Name": "IVA",
                    "Base": 1200.0,
                    "Rate": 0.16,
                    "IsRetention": false,
                    "IsQuota": null
                }
            ],
            "CuentaPredial": null,
            "NumerosPedimento": null,
            "Parts": null,
            "Total": 1392.0,
            "Complement": null
        }
    ],
    "Complemento": null,
    "Observations": null,
    "OrderNumber": null,
    "PaymentBankName": null
}

cfdi = facturama.CfdiMultiEmisor.create3(facturamulti)
```

# Cuenta
## Subir CSD
```
Rfc = "aaa010101aaa"
Certificate = "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"
PrivateKey = "MIIFDjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQIAgEAAoIBAQACAggAMBQGCCqGSIb3DQMHBAgwggS+AgEAMASCBMh4EHl7aNSCaMDA1VlRoXCZ5UUmqErAbuck7ujDnmKxSaOGzJzn1hAlfBWJNtr1rgiCXRHB5/2qJ/CnTOkCcgutvs1xl3vxHgY1+N9I60iZUG+yjfEd+ungL4alXXMtKgZ8CkQXaeYIeQXFdyZ5jUU07Cy+LjMrIOAh1m/VnL6U/qW3dY+oJmII6gCG0SKcfCojeCpBVL2ispK2CBTpMDO4hd7vnbFhafl9/wUkAncmz5SHLjXPMKgmK7HvBiUSMRYFCjcNEBvMshI7E1//nG8pi0Xrmbq4MfT1B+SF8vbA39hCqKP32m+QFlOduHlaFSnW96UkMBT5hF1qImwU3HTbtKfAumo3BLzYJ9XP7Y6eVOFFSSsXudrAt94mH7CojUjazGHBsqagsUY85Q7Cz0TTvnnvWFNFAj/xbQm6nT1VL8FkdJm8hEb5YLaOqQZ8y1AEv8sCq/M51aHglexuzGFIIUTF+/XQGeYDBITlS6z2TryoHp8n1+6LpClL51WrIfaSxyMEtG2fmAHN82iNujOP6MBR7aMZ6dfxJctFRAaWlmi89wa5VhyeaoDzkx1roJznF3MLxVKROmYLDYk142IwRtTgWrex4Wnidpo4unrfL+uj6VwTUDk0cizaYvamRhlZ/LXdwyB1syb/GQGu94gSzB1zAzb5/IIbtyofK+/tVTv08OMpCqHfBye1QJQg+vxQHMkbhZH6sEgORSEjuidW13DTKi8xyryQsD5WccMh8WDxMuAVFUldrwWdGilFKg0G99S/XJWLwKB74Nv0v/Ygdp6/d9T0fFD3FXpb9RznErCgfVSMtrPv1svGg3QFwh+qmkzjh+NBwUrmmqEjNshji+9SB4fnJNYlKVvu4WAzMKliixUkRcCID1QYwLtiyWuwZDYxKTnk7Y1LXmRGqqhNbh4kdnTNUdkxEjqp+UVtBdaxswa6s4qrLbNeD7VN+1KJEMN6/zZ6+2Uj2KBMzaDA0zwAHMB1gyPkgX0v47e61iffaVAUQzDGYGbDERG2vT8234NSDdgqzOpsf7il2Pv+uF0oab+db62JiRvOEjNefXG5p8KRudYyaVO8N7iTdRRj/A/yDwjmSq9dDCZEZE0cD6BEaAgmjvqwF5IvGgJGnWYKhrOGBPv+VL6zGOXo/L9zenxYwKNTHzNYlvug/t4gXQmArroqA2YKBGpYb8/FY/q3t3k+u1bXWvNLOzWi81InvxFSCTu6l9GBCthyWwekWdoL6ssSzOmzPr/d2klSRST3ByJmAJzLGJFsj6AL01BaUVWERH0s+GmnSWOU8ZIQVGF7aOEWWbtD0vyjJRxQnxPxn+Tt3oT9Nob10QGwG/2tNZtZuhAMf1yt+cF8jl0hC/LI0FtMqmLAkxaEOiXHmFuKXbAjFxIjdIwgWsAZe1cTLzR44jIKwlB64jvh1LXmJ5jCszLd/fuCEB0XZUWLDRCZVb82MqcZl7U/gaFazSqm71NNafCDzWjWO4ukWN1lcTDJE05KgeRqoYIEcpU8jXy/CAEaoseA1bWDnfnLJk2axVXzmrtYnojyKjTjDz3In41Kjsx3nNOegqtH7O2gl9YBzJfgwZmF0ldk+udcotc0JwIXYWk7b5HmRgXWa+WvDHSwyLzMrbw="
PrivateKeyPassword = "12345678a"

facturama.csdsMultiEmisor.upload(Rfc, PrivateKey, Certificate, PrivateKeyPassword, True)
```

## Borrar CSD
```
facturama.csdsMultiEmisor.delete("FUNK671228PH6")
```

## Recuperar información de la cuenta mediante RFC
```
print(facturama.TaxEntity.retrieve("EKU9003173C9"))
print(facturama.TaxEntity.SuscriptionPlan.retrieve("EKU9003173C9"))
```





