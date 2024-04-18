# coding: utf-8

"""
    Machship API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CarrierInvoiceInformation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'carrier': 'CarrierLite',
        'company': 'CompanyLite',
        'file_name': 'str',
        'invoice_id': 'str',
        'invoice_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'carrier': 'carrier',
        'company': 'company',
        'file_name': 'fileName',
        'invoice_id': 'invoiceId',
        'invoice_date': 'invoiceDate'
    }

    def __init__(self, id=None, carrier=None, company=None, file_name=None, invoice_id=None, invoice_date=None):  # noqa: E501
        """CarrierInvoiceInformation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._carrier = None
        self._company = None
        self._file_name = None
        self._invoice_id = None
        self._invoice_date = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if carrier is not None:
            self.carrier = carrier
        if company is not None:
            self.company = company
        if file_name is not None:
            self.file_name = file_name
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if invoice_date is not None:
            self.invoice_date = invoice_date

    @property
    def id(self):
        """Gets the id of this CarrierInvoiceInformation.  # noqa: E501


        :return: The id of this CarrierInvoiceInformation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CarrierInvoiceInformation.


        :param id: The id of this CarrierInvoiceInformation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def carrier(self):
        """Gets the carrier of this CarrierInvoiceInformation.  # noqa: E501


        :return: The carrier of this CarrierInvoiceInformation.  # noqa: E501
        :rtype: CarrierLite
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this CarrierInvoiceInformation.


        :param carrier: The carrier of this CarrierInvoiceInformation.  # noqa: E501
        :type: CarrierLite
        """

        self._carrier = carrier

    @property
    def company(self):
        """Gets the company of this CarrierInvoiceInformation.  # noqa: E501


        :return: The company of this CarrierInvoiceInformation.  # noqa: E501
        :rtype: CompanyLite
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this CarrierInvoiceInformation.


        :param company: The company of this CarrierInvoiceInformation.  # noqa: E501
        :type: CompanyLite
        """

        self._company = company

    @property
    def file_name(self):
        """Gets the file_name of this CarrierInvoiceInformation.  # noqa: E501


        :return: The file_name of this CarrierInvoiceInformation.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CarrierInvoiceInformation.


        :param file_name: The file_name of this CarrierInvoiceInformation.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def invoice_id(self):
        """Gets the invoice_id of this CarrierInvoiceInformation.  # noqa: E501


        :return: The invoice_id of this CarrierInvoiceInformation.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this CarrierInvoiceInformation.


        :param invoice_id: The invoice_id of this CarrierInvoiceInformation.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def invoice_date(self):
        """Gets the invoice_date of this CarrierInvoiceInformation.  # noqa: E501


        :return: The invoice_date of this CarrierInvoiceInformation.  # noqa: E501
        :rtype: datetime
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this CarrierInvoiceInformation.


        :param invoice_date: The invoice_date of this CarrierInvoiceInformation.  # noqa: E501
        :type: datetime
        """

        self._invoice_date = invoice_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CarrierInvoiceInformation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CarrierInvoiceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
