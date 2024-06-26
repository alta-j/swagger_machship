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

class CompanyCarrierAccountService(object):
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
        'company_carrier_account_id': 'int',
        'company_carrier_account': 'CompanyCarrierAccountLite',
        'carrier_service_id': 'int',
        'carrier_service': 'CarrierServiceLite'
    }

    attribute_map = {
        'id': 'id',
        'company_carrier_account_id': 'companyCarrierAccountId',
        'company_carrier_account': 'companyCarrierAccount',
        'carrier_service_id': 'carrierServiceId',
        'carrier_service': 'carrierService'
    }

    def __init__(self, id=None, company_carrier_account_id=None, company_carrier_account=None, carrier_service_id=None, carrier_service=None):  # noqa: E501
        """CompanyCarrierAccountService - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._company_carrier_account_id = None
        self._company_carrier_account = None
        self._carrier_service_id = None
        self._carrier_service = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if company_carrier_account_id is not None:
            self.company_carrier_account_id = company_carrier_account_id
        if company_carrier_account is not None:
            self.company_carrier_account = company_carrier_account
        if carrier_service_id is not None:
            self.carrier_service_id = carrier_service_id
        if carrier_service is not None:
            self.carrier_service = carrier_service

    @property
    def id(self):
        """Gets the id of this CompanyCarrierAccountService.  # noqa: E501


        :return: The id of this CompanyCarrierAccountService.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyCarrierAccountService.


        :param id: The id of this CompanyCarrierAccountService.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def company_carrier_account_id(self):
        """Gets the company_carrier_account_id of this CompanyCarrierAccountService.  # noqa: E501


        :return: The company_carrier_account_id of this CompanyCarrierAccountService.  # noqa: E501
        :rtype: int
        """
        return self._company_carrier_account_id

    @company_carrier_account_id.setter
    def company_carrier_account_id(self, company_carrier_account_id):
        """Sets the company_carrier_account_id of this CompanyCarrierAccountService.


        :param company_carrier_account_id: The company_carrier_account_id of this CompanyCarrierAccountService.  # noqa: E501
        :type: int
        """

        self._company_carrier_account_id = company_carrier_account_id

    @property
    def company_carrier_account(self):
        """Gets the company_carrier_account of this CompanyCarrierAccountService.  # noqa: E501


        :return: The company_carrier_account of this CompanyCarrierAccountService.  # noqa: E501
        :rtype: CompanyCarrierAccountLite
        """
        return self._company_carrier_account

    @company_carrier_account.setter
    def company_carrier_account(self, company_carrier_account):
        """Sets the company_carrier_account of this CompanyCarrierAccountService.


        :param company_carrier_account: The company_carrier_account of this CompanyCarrierAccountService.  # noqa: E501
        :type: CompanyCarrierAccountLite
        """

        self._company_carrier_account = company_carrier_account

    @property
    def carrier_service_id(self):
        """Gets the carrier_service_id of this CompanyCarrierAccountService.  # noqa: E501


        :return: The carrier_service_id of this CompanyCarrierAccountService.  # noqa: E501
        :rtype: int
        """
        return self._carrier_service_id

    @carrier_service_id.setter
    def carrier_service_id(self, carrier_service_id):
        """Sets the carrier_service_id of this CompanyCarrierAccountService.


        :param carrier_service_id: The carrier_service_id of this CompanyCarrierAccountService.  # noqa: E501
        :type: int
        """

        self._carrier_service_id = carrier_service_id

    @property
    def carrier_service(self):
        """Gets the carrier_service of this CompanyCarrierAccountService.  # noqa: E501


        :return: The carrier_service of this CompanyCarrierAccountService.  # noqa: E501
        :rtype: CarrierServiceLite
        """
        return self._carrier_service

    @carrier_service.setter
    def carrier_service(self, carrier_service):
        """Sets the carrier_service of this CompanyCarrierAccountService.


        :param carrier_service: The carrier_service of this CompanyCarrierAccountService.  # noqa: E501
        :type: CarrierServiceLite
        """

        self._carrier_service = carrier_service

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
        if issubclass(CompanyCarrierAccountService, dict):
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
        if not isinstance(other, CompanyCarrierAccountService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
