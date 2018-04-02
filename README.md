# Facturama
Facturama python wrapper https://www.api.facturama.com.mx/

Install
```sh
pip install -e git://github.com/tingsystems/facturama.git@master#egg=facturama
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
    "Name": "Pollitux"
 }
customer = facturama.Client.create(customer_object)
```


Create new Product

```python
import facturama

facturama._credentials = ('username', 'password')


product_object = {
    "Id": "0001",
    "Unit": "PZA",
    "IdentificationNumber": "0001",
    "Name": "Product test1",
    "Description": "Product test 1",
    "Price": 6.0
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

The wrapper support the version cfids 

0 api default\
1 api and cfdi 2\
2 api-lite\
3 api-lite and cfdi 2\

You can see https://api.facturama.com.mx/Help for more information
 
```python
import facturama 

facturama._credentials = ('username', 'password')

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

cfdi = facturama.Cfdi.create(cfdi_object) # create cfdi version 0
cfdi = facturama.Cfdi.create(cfdi_object, v=3) # create cfdi version 2 and api-lite 

```

## Library Development and Testing

You can test the facturama library with nose from the facturama library root:

```sh
$ nosetests
```


## Contributing:
[tingsystems](https://github.com/tingsystems)
