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

class CreateQuoteResponseV2(object):
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
        'consignment_number': 'str',
        'despatch_date_local': 'datetime',
        'despatch_date_utc': 'datetime',
        'eta_local': 'datetime',
        'eta_utc': 'datetime',
        'carrier': 'CarrierLite',
        'carrier_service': 'CarrierServiceLite',
        'company_carrier_account': 'CompanyCarrierAccountLite',
        'is_test': 'bool',
        'is_international': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'consignment_number': 'consignmentNumber',
        'despatch_date_local': 'despatchDateLocal',
        'despatch_date_utc': 'despatchDateUtc',
        'eta_local': 'etaLocal',
        'eta_utc': 'etaUtc',
        'carrier': 'carrier',
        'carrier_service': 'carrierService',
        'company_carrier_account': 'companyCarrierAccount',
        'is_test': 'isTest',
        'is_international': 'isInternational'
    }

    def __init__(self, id=None, consignment_number=None, despatch_date_local=None, despatch_date_utc=None, eta_local=None, eta_utc=None, carrier=None, carrier_service=None, company_carrier_account=None, is_test=None, is_international=None):  # noqa: E501
        """CreateQuoteResponseV2 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._consignment_number = None
        self._despatch_date_local = None
        self._despatch_date_utc = None
        self._eta_local = None
        self._eta_utc = None
        self._carrier = None
        self._carrier_service = None
        self._company_carrier_account = None
        self._is_test = None
        self._is_international = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if consignment_number is not None:
            self.consignment_number = consignment_number
        if despatch_date_local is not None:
            self.despatch_date_local = despatch_date_local
        if despatch_date_utc is not None:
            self.despatch_date_utc = despatch_date_utc
        if eta_local is not None:
            self.eta_local = eta_local
        if eta_utc is not None:
            self.eta_utc = eta_utc
        if carrier is not None:
            self.carrier = carrier
        if carrier_service is not None:
            self.carrier_service = carrier_service
        if company_carrier_account is not None:
            self.company_carrier_account = company_carrier_account
        if is_test is not None:
            self.is_test = is_test
        if is_international is not None:
            self.is_international = is_international

    @property
    def id(self):
        """Gets the id of this CreateQuoteResponseV2.  # noqa: E501

        Machship's Id reference for this consignment. Use this id when interacting via the API  # noqa: E501

        :return: The id of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateQuoteResponseV2.

        Machship's Id reference for this consignment. Use this id when interacting via the API  # noqa: E501

        :param id: The id of this CreateQuoteResponseV2.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def consignment_number(self):
        """Gets the consignment_number of this CreateQuoteResponseV2.  # noqa: E501

        Machship's MS Number. This is the human friendly Machship consignment number that is sent to the carrier  # noqa: E501

        :return: The consignment_number of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._consignment_number

    @consignment_number.setter
    def consignment_number(self, consignment_number):
        """Sets the consignment_number of this CreateQuoteResponseV2.

        Machship's MS Number. This is the human friendly Machship consignment number that is sent to the carrier  # noqa: E501

        :param consignment_number: The consignment_number of this CreateQuoteResponseV2.  # noqa: E501
        :type: str
        """

        self._consignment_number = consignment_number

    @property
    def despatch_date_local(self):
        """Gets the despatch_date_local of this CreateQuoteResponseV2.  # noqa: E501


        :return: The despatch_date_local of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: datetime
        """
        return self._despatch_date_local

    @despatch_date_local.setter
    def despatch_date_local(self, despatch_date_local):
        """Sets the despatch_date_local of this CreateQuoteResponseV2.


        :param despatch_date_local: The despatch_date_local of this CreateQuoteResponseV2.  # noqa: E501
        :type: datetime
        """

        self._despatch_date_local = despatch_date_local

    @property
    def despatch_date_utc(self):
        """Gets the despatch_date_utc of this CreateQuoteResponseV2.  # noqa: E501


        :return: The despatch_date_utc of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: datetime
        """
        return self._despatch_date_utc

    @despatch_date_utc.setter
    def despatch_date_utc(self, despatch_date_utc):
        """Sets the despatch_date_utc of this CreateQuoteResponseV2.


        :param despatch_date_utc: The despatch_date_utc of this CreateQuoteResponseV2.  # noqa: E501
        :type: datetime
        """

        self._despatch_date_utc = despatch_date_utc

    @property
    def eta_local(self):
        """Gets the eta_local of this CreateQuoteResponseV2.  # noqa: E501


        :return: The eta_local of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: datetime
        """
        return self._eta_local

    @eta_local.setter
    def eta_local(self, eta_local):
        """Sets the eta_local of this CreateQuoteResponseV2.


        :param eta_local: The eta_local of this CreateQuoteResponseV2.  # noqa: E501
        :type: datetime
        """

        self._eta_local = eta_local

    @property
    def eta_utc(self):
        """Gets the eta_utc of this CreateQuoteResponseV2.  # noqa: E501


        :return: The eta_utc of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: datetime
        """
        return self._eta_utc

    @eta_utc.setter
    def eta_utc(self, eta_utc):
        """Sets the eta_utc of this CreateQuoteResponseV2.


        :param eta_utc: The eta_utc of this CreateQuoteResponseV2.  # noqa: E501
        :type: datetime
        """

        self._eta_utc = eta_utc

    @property
    def carrier(self):
        """Gets the carrier of this CreateQuoteResponseV2.  # noqa: E501


        :return: The carrier of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: CarrierLite
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this CreateQuoteResponseV2.


        :param carrier: The carrier of this CreateQuoteResponseV2.  # noqa: E501
        :type: CarrierLite
        """

        self._carrier = carrier

    @property
    def carrier_service(self):
        """Gets the carrier_service of this CreateQuoteResponseV2.  # noqa: E501


        :return: The carrier_service of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: CarrierServiceLite
        """
        return self._carrier_service

    @carrier_service.setter
    def carrier_service(self, carrier_service):
        """Sets the carrier_service of this CreateQuoteResponseV2.


        :param carrier_service: The carrier_service of this CreateQuoteResponseV2.  # noqa: E501
        :type: CarrierServiceLite
        """

        self._carrier_service = carrier_service

    @property
    def company_carrier_account(self):
        """Gets the company_carrier_account of this CreateQuoteResponseV2.  # noqa: E501


        :return: The company_carrier_account of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: CompanyCarrierAccountLite
        """
        return self._company_carrier_account

    @company_carrier_account.setter
    def company_carrier_account(self, company_carrier_account):
        """Sets the company_carrier_account of this CreateQuoteResponseV2.


        :param company_carrier_account: The company_carrier_account of this CreateQuoteResponseV2.  # noqa: E501
        :type: CompanyCarrierAccountLite
        """

        self._company_carrier_account = company_carrier_account

    @property
    def is_test(self):
        """Gets the is_test of this CreateQuoteResponseV2.  # noqa: E501


        :return: The is_test of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_test

    @is_test.setter
    def is_test(self, is_test):
        """Sets the is_test of this CreateQuoteResponseV2.


        :param is_test: The is_test of this CreateQuoteResponseV2.  # noqa: E501
        :type: bool
        """

        self._is_test = is_test

    @property
    def is_international(self):
        """Gets the is_international of this CreateQuoteResponseV2.  # noqa: E501


        :return: The is_international of this CreateQuoteResponseV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_international

    @is_international.setter
    def is_international(self, is_international):
        """Sets the is_international of this CreateQuoteResponseV2.


        :param is_international: The is_international of this CreateQuoteResponseV2.  # noqa: E501
        :type: bool
        """

        self._is_international = is_international

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
        if issubclass(CreateQuoteResponseV2, dict):
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
        if not isinstance(other, CreateQuoteResponseV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other