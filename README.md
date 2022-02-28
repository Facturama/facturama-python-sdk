# Facturama Python SDK

[NOTE] This document is also available in [English]

Libreria para consumir la API Web y API Multiemisor de [Facturama](https://api.facturama.mx/).

## Instalación
```sh
pip install -e git://github.com/Facturama/facturama-python-sdk.git@master#egg=facturama
```

## Operaciones Web API
- Crear, Consultar Cancelar CFDI así como descargar XML, PDF y envió de estos por mail.
- Consultar Perfil y Suscripción actual
- Carga de Logo y Certificados Digitales
- CRUD de Productos, Clientes, Sucursales y Series.

Ejemplos:[aquí](https://github.com/Facturama/facturama-python-sdk/wiki/API-Web)


## Operaciones API Multiemisor

- Crear, Consultar, Cancelar descarga de XML
- CRUD de CSD (Certificados de los Sellos Digitales).

*Las operaciones no se reflejan en la plataforma web.*

Ejemplos:[aquí](https://github.com/Facturama/facturama-python-sdk/wiki/API-Multiemisor)

## Library Development and Testing

Test de libreria con nose http://nose.readthedocs.io/en/latest/

```sh
$ nosetests
```


## Contributing:
[tingsystems](https://github.com/tingsystems)

[English]: ./README-en.md
