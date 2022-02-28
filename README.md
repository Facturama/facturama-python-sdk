# Facturama Python SDK

> [NOTE] This document is also available in [English]
>
> Librería para consumir la API Web y API Multiemisor de [Facturama](https://api.facturama.mx/).
>
> Puedes consultar la guía completa de la [API](https://apisandbox.facturama.mx/guias).

## Crear cuenta de usuario

- Crear una cuenta de usuario en el ambiente de prueba [Sandbox](https://dev.facturama.mx/api/login) 

- Para API Web, realiza la configuración básica usando RFC de pruebas **"EKU9003173C9"**, más información [aquí](https://apisandbox.facturama.mx/guias/perfil-fiscal)

- Sellos digitales de prueba (CSD), [aquí](https://github.com/rafa-dx/facturama-CSD-prueba). 

## Inicio Rápido

### Instalación
```sh
pip install -e git://github.com/Facturama/facturama-python-sdk.git@master#egg=facturama
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

### Operaciones API Web
- Crear, Consultar Cancelar CFDI así como descargar XML, PDF y envió de estos por mail.
- Consultar Perfil y Suscripción actual
- Carga de Logo y Certificados Digitales
- CRUD de Productos, Clientes, Sucursales y Series.

Ejemplos: [aquí](https://github.com/Facturama/facturama-python-sdk/wiki/API-Web)

*Todas las operaciones son reflejadas en la plataforma web.*


## API Multiemisor

> Creacion de CFDI con multiples emisores

### Operaciones API Multiemisor

- Crear, Consultar, Cancelar descarga de XML
- CRUD de CSD (Certificados de los Sellos Digitales).

Ejemplos: [aquí](https://github.com/Facturama/facturama-python-sdk/wiki/API-Multiemisor)

*Las operaciones no se reflejan en la plataforma web.*


### Library Development and Testing

Test de libreria con nose http://nose.readthedocs.io/en/latest/

```sh
$ nosetests
```


## Contributing:
[tingsystems](https://github.com/tingsystems)

[English]: ./README-en.md
