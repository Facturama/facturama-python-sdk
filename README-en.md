# Facturama SDK Python

[NOTA] Este documento esta disponble en [Español]

Facturama python wrapper https://api.facturama.mx/

## Check the Facturama guide here.

[Guide](https://apisandbox.facturama.mx/guias)


## How do I install it?

```sh
pip install -e git://github.com/Facturama/facturama-python-sdk.git@master#egg=facturama
```




## Web API operations

- Create, get, cancel CFDIs; download XMLs and PDFs and send them by email;
- Check profile and current subscription;
- Logo and digital certificates uploading;
- CRUDs for Product, Customer, Branch office and series.

*All operations will be reflected on Facturama's web app.*

Some examples: [here](https://github.com/Facturama/facturama-python-sdk/wiki/API-Web)

## Mult-issuer API operations

- Create, get, cancel CFDIs; download XMLs and PDFs;
- CRUD for digital sign certificates ("CSD", "Certificados de los Sellos Digitales").

*These operations will not be reflected on Facturama's web app.*

Some examples: [here](https://github.com/Facturama/facturama-python-sdk/wiki/API-Multiemisor)


## Library Development and Testing

Use nose to test http://nose.readthedocs.io/en/latest/

```sh
$ nosetests
```

## I want to contribute!
That is great! Just fork the project in GitHub, create a topic branch, write some code, and add some tests for your new code.

Thanks for helping!


## Contributing:
[tingsystems](https://github.com/tingsystems)

[Español]: ./README.md
