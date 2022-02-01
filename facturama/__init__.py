#!/usr/bin/python
# coding: utf-8
# (c) 2017 Raul Granados <@pollitux>

import base64
from requests import request


try:
    import json
except ImportError:
    import simplejson as json

__version__ = '3.0.2'
__author__ = 'Raul Granados'

api_lite = False
sandbox = False
url_base = ''

_credentials = ('', '')


class FacturamaError(Exception):
    def __init__(self, error_json):
        super(FacturamaError, self).__init__(error_json)
        self.error_json = error_json


class MalformedRequestError(FacturamaError):
    pass


class AuthenticationError(FacturamaError):
    pass


class ProcessingError(FacturamaError):
    pass


class ResourceNotFoundError(FacturamaError):
    pass


class ParameterValidationError(FacturamaError):
    pass


class ApiError(FacturamaError):
    pass


class Facturama:
    """
    Build request facturama API
    """

    _headers = None

    @classmethod
    def aut_api(cls):
        _username, _password = _credentials
        cls._headers = {
            'Authorization': 'Basic %s' % (base64.b64encode(
                ('{}:{}'.format(_username, _password)).encode('utf-8'))).decode('ascii'),
            'content-type': 'application/json'
        }

    @classmethod
    def build_http_request(cls, method, path, payload=None, params=None, version=0):
        """

        :param method: get, post, patch, put
        :param path: resource in the Facturama API
        :param payload: request body
        :param params: query params by url
        :param version: cfdi version 0 api, 1 api and cfdi 3.3, 2 api-lite, 3 api-lite and cfdi 3.3
        :return:
        """
        # urls base of facturama api

        """
        http://api.facturama.mx/2/ - opción 1 api and cfdi 3.3
        http://api.facturama.mx/api-lite/2/ - opción 3 api-lite and cfdi 2
        """

        if url_base:
            host = url_base
        else:
            host = 'https://apisandbox.facturama.mx' if sandbox else 'https://api.facturama.mx'

        uris = [
            '{}/api/'.format(host),
            '{}/api/2/'.format(host),
            '{}/api-lite/'.format(host),
            '{}/api-lite/2/'.format(host),
            '{}/retenciones/'.format(host),
        ]
        api_base = uris[version]
        cls.aut_api()
        method = str(method).lower()
        body = request(
            method, '{}{}'.format(api_base, path), data=json.dumps(payload), params=params, headers=cls._headers
        )

        if body.status_code == 200 or body.status_code == 201 or body.status_code == 204:
            response_body = {'status': True}
            try:
                response_body = body.json()
            except Exception:
                pass
            return response_body

        if body.status_code == 400:
            raise MalformedRequestError(body.json())
        elif body.status_code == 401:
            raise AuthenticationError(body.json())
        elif body.status_code == 402:
            raise ProcessingError(body.json())
        elif body.status_code == 404:
            raise ResourceNotFoundError(body.json())
        elif body.status_code == 422:
            raise ParameterValidationError(body.json())
        elif body.status_code == 500:
            raise ApiError(body.json())
        else:
            raise FacturamaError(body.json())

    @classmethod
    def to_object(cls, response):
        for key, value in response.items():
            setattr(cls, key, value)
        return cls

    @classmethod
    def create(cls, data):
        """

        :param data: dict with data for create object
        :return: object with data from response
        """
        return cls.build_http_request('post', cls.__name__, data)

    @classmethod
    def retrieve(cls, oid, params=None):
        """

        :params oid: id of object retrieve
        :return: object with data from response
        """
        params = {'type':'issued'}
        return cls.build_http_request('get', '{}/{}'.format(cls.__name__, oid), None , params=params)

    @classmethod
    def all(cls, params=None):
        """
        :type params: extra params for build request
        :return: list of objects from response facturama api
        """
        return cls.build_http_request('get', cls.__name__, params=params)

    @classmethod
    def query(cls, params=None):
        """
        :type params: extra params for build request
        :return: list of objects from response facturama api
        """
        return cls.build_http_request('get', cls.__name__, params=params)

    @classmethod
    def update(cls, data, oid):
        """
        :param oid: id object
        :type data: data
        :return: object with data from response
        """
        return cls.build_http_request('put', '{}/{}'.format(cls.__name__, oid), data)

    @classmethod
    def delete(cls, oid):
        """
        :param oid: id object
        :return: None
        """
        return cls.build_http_request('delete', '{}/{}'.format(cls.__name__, oid))


class Client(Facturama):
    """
    Opr with Clients of Facturama API
    """


class Product(Facturama):
    """
    Opr with Products of Facturama API
    """


class BranchOffice(Facturama):
    """
    Opr with Branch Offices of Facturama API
    """


class Cfdi(Facturama):
    """
    Opr with Cfdi of Facturama API
    """

    @classmethod
    def create(cls, data, v=1):
        """

        :param v: cfdi version 0 api, 1 api and cfdi 3.3, 2 api-lite, 3 api-lite and cfdi 3.3
        :param data: dict with data for create object
        :return: object with data from response
        """

        return cls.build_http_request('post', 'cfdis' , data, version=v)

    @classmethod
    def get_by_file(cls, f, t, oid):
        """
        :return: get cfdi file by format and type
        """
        return cls.build_http_request('get', '{}/{}/{}/{}'.format(cls.__name__, f, t, oid))

    @classmethod
    def saveAsPdf(cls, oid, fileName):
        """
        :return: get cfdi file by format and type
        """
        issued = 'issuedLite' if api_lite else 'issued'
        html_file = cls.get_by_file('pdf', issued, oid)
        with open(fileName, 'wb') as f:
            f.write(base64.urlsafe_b64decode(html_file['Content'].encode('utf-8')))
        return f

    @classmethod
    def saveAsHtml(cls, oid, fileName):
        """
        :return: get cfdi file by format and type
        """
        issued = 'issuedLite' if api_lite else 'issued'
        html_file = cls.get_by_file('html', issued, oid)
        with open(fileName, 'wb') as f:
            f.write(base64.urlsafe_b64decode(html_file['Content'].encode('utf-8')))
        return f

    @classmethod
    def saveAsXML(cls, oid, fileName):
        """
        :return: get cfdi file by format and type
        """
        issued = 'issuedLite' if api_lite else 'issued'
        xml_file = cls.get_by_file('xml', issued, oid)

        with open(fileName, 'wb') as f:
            f.write(base64.urlsafe_b64decode(xml_file['Content'].encode('utf-8')))
        return f

    @classmethod
    def send_by_email(cls, t, oid, email):
        """
        :return: send Cfdi by email
        """
        return cls.build_http_request('post', '{}?cfdiType={}&cfdiId={}&email={}'.format(cls.__name__, t, oid, email))

    @classmethod
    def delete(cls, oid, _type, _motive, _uuidReplacement=None):
        """
        :param oid: id object
        :return: None
        """
        params = {'type':_type, 'motive':_motive, 'uuidReplacement':_uuidReplacement }
        v = 2 if api_lite else 0
        return cls.build_http_request('delete', '{}/{}'.format(cls.__name__ if not api_lite else 'cfdis', oid),params=params, version=v)

    @classmethod
    def list(cls, tipo, keyword, status):
        """
        :param oid: id object
        :return: None
        """
        v = 0
        return cls.build_http_request(
            'get', '{}?type={}&keyword={}&status={}'.format(cls.__name__ , tipo, keyword, status), version=v
        )

class csds(Facturama):
    """
    Opr with csds of Facturama API
    """

    @classmethod
    def get_by_rfc(cls, rfc, v=0):
        """
        get csds by rfc
        :return: object with data from response
        """
        return cls.build_http_request('get', '{}/{}'.format(cls.__name__, rfc), version=v)

    @classmethod
    def create(cls, data):
        raise NotImplemented('Method not implemented')

    @classmethod
    def upload(cls, rfc, path_key, path_cer, password, encode=False, v=0):
        """

        :param encode:
        :param rfc:
        :param path_key:
        :param path_cer:
        :param password:
        :param v:
        :return: object with data from response
        """
        file_key, file_cer = path_key, path_cer
        if not encode:
            with open(path_key, 'rb') as f:
                file_key = base64.b64encode(f.read()).decode('utf-8')

            with open(path_cer, 'rb') as f:
                file_cer = base64.b64encode(f.read()).decode('utf-8')

        data = {
            'Rfc': str(rfc).upper(), 'Certificate': file_cer, 'PrivateKey': file_key, 'PrivateKeyPassword': password
        }
        return cls.build_http_request('post', cls.__name__, data, version=v)


class Catalogs(Facturama):
    catalog = None
    prefix = 'Catalogs'

    @classmethod
    def query(cls, params=None):
        """
        :type params: extra params for build request
        :return: list of objects from response facturama api
        """
        return cls.build_http_request('get', '{}/{}'.format(cls.prefix, cls.catalog), params=params)


class ProductsServicesCatalog(Catalogs):
    """
    Opr with Product or Services catalog of Facturama API
    """

    catalog = 'ProductsOrServices'


class PostalCodesCatalog(Catalogs):
    """
    Opr with PostalCodes catalog of Facturama API
    """

    catalog = 'PostalCodes'


class UnitsCatalog(Catalogs):
    """
    Opr with Units catalog of Facturama API
    """

    catalog = 'Units'


class CurrenciesCatalog(Catalogs):
    """
    Opr with Currencies catalog of Facturama API
    """

    catalog = 'Currencies'


class CountriesCatalog(Catalogs):
    """
    Opr with Currencies catalog of Facturama API
    """
    prefix = 'catalogs'
    catalog = 'Countries'


class PaymentFormsCatalog(Catalogs):
    """
    Opr with PaymentForms catalog of Facturama API
    """
    prefix = 'catalogs'
    catalog = 'PaymentForms'


class PaymentMethodsCatalog(Catalogs):
    """
    Opr with PaymentMethods catalog of Facturama API
    """
    prefix = 'catalogs'
    catalog = 'PaymentMethods'


class FederalTaxesCatalog(Catalogs):
    """
    Opr with FederalTaxes catalog of Facturama API
    """
    prefix = 'catalogs'
    catalog = 'FederalTaxes'


class FiscalRegimensCatalog(Catalogs):
    """
    Opr with FiscalRegimens catalog of Facturama API
    """
    prefix = 'catalogs'
    catalog = 'FiscalRegimens'


class CfdiTypesCatalog(Catalogs):
    """
    Opr with CfdiTypes catalog of Facturama API
    """
    prefix = 'catalogs'
    catalog = 'CfdiTypes'


class RelationTypesCatalog(Catalogs):
    """
    Opr with RelationTypes catalog of Facturama API
    """
    prefix = 'catalogs'
    catalog = 'RelationTypes'


class CfdiUsesCatalog(Catalogs):
    """
    Opr with CfdiUses catalog of Facturama API
    """
    prefix = 'catalogs'
    catalog = 'CfdiUses'

class CfdiMultiEmisor(Facturama):
    """
    Opr with Cfdi of Facturama API
    """

    @classmethod
    def create(cls, data, v=3):
        """

        :param v: cfdi version 0 api, 1 api and cfdi 3.3, 2 api-lite, 3 api-lite and cfdi 3.3
        :param data: dict with data for create object
        :return: object with data from response
        """
        return cls.build_http_request('post', cls.__name__ if not api_lite else 'cfdis', data, version=v)

    @classmethod
    def retrieve(cls, oid, params=None):
        """

        :params oid: id of object
        :return: object with data from response
        """
        return cls.build_http_request('get', '{}/{}'.format('cfdis', oid), params=params, version=2)
        #return cls.build_http_request('get', '{}/{}'.format('cfdis', oid), version=3)

    @classmethod
    def get_by_file(cls, f, t, oid):
        """
        :return: get cfdi file by format and type
        """
        return cls.build_http_request('get', '{}/{}/{}/{}'.format('Cfdi', f, t, oid))

    @classmethod
    def saveAsPdf(cls, oid, fileName):
        """
        :return: get cfdi file by format and type
        """
        html_file = cls.get_by_file('pdf', 'IssuedLite',oid)
        cls.api_lite = True
        with open(fileName, 'wb') as f:
            f.write(base64.urlsafe_b64decode(html_file['Content'].encode('utf-8')))
        return f

    @classmethod
    def saveAsHtml(cls, oid, fileName):
        """
        :return: get cfdi file by format and type
        """
        html_file = cls.get_by_file('html', 'IssuedLite', oid)
        cls.api_lite = True
        with open(fileName, 'wb') as f:
            f.write(base64.urlsafe_b64decode(html_file['Content'].encode('utf-8')))
        return f

    @classmethod
    def saveAsXML(cls, oid, fileName):
        """
        :return: get cfdi file by format and type
        """
        xml_file = cls.get_by_file('xml', 'IssuedLite', oid)
        cls.api_lite = True
        with open(fileName, 'wb') as f:
            f.write(base64.urlsafe_b64decode(xml_file['Content'].encode('utf-8')))
        return f

    @classmethod
    def delete(cls, oid, _motive, _uuidReplacement=None):
        """
        :param oid: id object
        :return: None
        """
        params = {'motive':_motive, 'uuidReplacement':_uuidReplacement }
        return cls.build_http_request('delete', '{}/{}'.format('cfdis', oid),params=params, version=2)

    @classmethod
    def list(cls, filters):
        """
        :param filters: dict filters
        :return: None
        """
        return cls.build_http_request('get','cfdis', params=filters, version=2)


    @classmethod
    def detail(cls, oid):
        """
        :param oid: id object
        :return: None
        """
        return cls.build_http_request('get', '{}/{}'.format('cfdis', oid), version=2)


class csdsMultiEmisor(Facturama):
    """
    Opr with csds of Facturama API
    """

    @classmethod
    def get_by_rfc(cls, rfc):
        """
        get csds by rfc
        :return: object with data from response
        """
        return cls.build_http_request('get', '{}/{}'.format('csds', rfc), version=2)

    @classmethod
    def create(cls, data):
        raise NotImplemented('Method not implemented')

    @classmethod
    def upload(cls, rfc, path_key, path_cer, password, encode=False):
        """

        :param encode:
        :param rfc:
        :param path_key:
        :param path_cer:
        :param password:
        :param v:
        :return: object with data from response
        """
        file_key, file_cer = path_key, path_cer
        if not encode:
            with open(path_key, 'rb') as f:
                file_key = base64.b64encode(f.read()).decode('utf-8')

            with open(path_cer, 'rb') as f:
                file_cer = base64.b64encode(f.read()).decode('utf-8')

        data = {
            'Rfc': str(rfc).upper(), 'Certificate': file_cer, 'PrivateKey': file_key, 'PrivateKeyPassword': password
        }
        return cls.build_http_request('post', 'csds', data, version=2)

    @classmethod
    def update(cls, rfc, path_key, path_cer, password, encode=False):
        """

        :param encode:
        :param rfc:
        :param path_key:
        :param path_cer:
        :param password:
        :param v:
        :return: object with data from response
        """
        file_key, file_cer = path_key, path_cer
        if not encode:
            with open(path_key, 'rb') as f:
                file_key = base64.b64encode(f.read()).decode('utf-8')

            with open(path_cer, 'rb') as f:
                file_cer = base64.b64encode(f.read()).decode('utf-8')

        data = {
            'Rfc': str(rfc).upper(), 'Certificate': file_cer, 'PrivateKey': file_key, 'PrivateKeyPassword': password
        }
        return cls.build_http_request('put', '{}/{}'.format('csds', rfc), data, version=2)


    @classmethod
    def delete(cls, rfc):
        """
        get csds by rfc
        :return: object with data from response
        """
        return cls.build_http_request('delete', '{}/{}'.format('csds', rfc), version=2)

    @classmethod
    def get(cls):
        """
        get csds by rfc
        :return: object with data from response
        """
        return cls.build_http_request('get', '{}'.format('csds'), version=2)


class Retentions(Facturama):
    """
    Opr with Cfdi of Facturama API
    """

    @classmethod
    def create(cls, data):
        """
        :param data: dict with data for create object
        :return: object with data from response
        """
        return cls.build_http_request('post', '', data, version=4)

    @classmethod
    def retrieve(cls, oid, params=None):
        """
        :params oid: id of object
        :return: object with data from response
        """
        return cls.build_http_request('get', oid, params=params, version=4)

    @classmethod
    def get_by_file(cls, format, oid):
        """
        :return: get cfdi file by format and type
        """
        return cls.build_http_request('get', '{}/{}'.format(oid, format), params=None, version=4)

    @classmethod
    def saveAsPdf(cls, oid, fileName):
        """
        :return: get cfdi file by format and type
        """
        html_file = cls.get_by_file('pdf', oid)
        cls.api_lite = True
        with open(fileName, 'wb') as f:
            f.write(base64.urlsafe_b64decode(html_file['Content'].encode('utf-8')))
        return f

    @classmethod
    def saveAsHtml(cls, oid, fileName):
        """
        :return: get cfdi file by format and type
        """
        html_file = cls.get_by_file('html', oid)
        cls.api_lite = True
        with open(fileName, 'wb') as f:
            f.write(base64.urlsafe_b64decode(html_file['Content'].encode('utf-8')))
        return f

    @classmethod
    def saveAsXML(cls, oid, fileName):
        """
        :return: get cfdi file by format and type
        """
        xml_file = cls.get_by_file('xml', oid)
        cls.api_lite = True
        with open(fileName, 'wb') as f:
            f.write(base64.urlsafe_b64decode(xml_file['Content'].encode('utf-8')))
        return f

    @classmethod
    def delete(cls, oid):
        """
        :param oid: id object
        :return: None
        """
        return cls.build_http_request(
            'delete', oid, version=4)

    @classmethod
    def list(cls, filters = None):
        """
        :param filters: dict filters
        :return: None
        """
        return cls.build_http_request('get','', params=filters, version=4)

    @classmethod
    def sendByMail(cls, oid, email):
        """
        :param filters: dict filters
        :return: None
        """
        return cls.build_http_request('post','envia?id={}&email={}'.format(oid, email), None, version=4)
