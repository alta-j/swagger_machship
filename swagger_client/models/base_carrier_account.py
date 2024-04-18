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

class BaseCarrierAccount(object):
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
        'name': 'str',
        'account_code': 'str',
        'carrier_id': 'int',
        'carrier_integration_id': 'int',
        'carrier_integration': 'CarrierIntegrationLite',
        'display_name': 'str',
        'carrier_account_services': 'list[CarrierAccountServiceModel]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'account_code': 'accountCode',
        'carrier_id': 'carrierId',
        'carrier_integration_id': 'carrierIntegrationId',
        'carrier_integration': 'carrierIntegration',
        'display_name': 'displayName',
        'carrier_account_services': 'carrierAccountServices'
    }

    def __init__(self, id=None, name=None, account_code=None, carrier_id=None, carrier_integration_id=None, carrier_integration=None, display_name=None, carrier_account_services=None):  # noqa: E501
        """BaseCarrierAccount - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._account_code = None
        self._carrier_id = None
        self._carrier_integration_id = None
        self._carrier_integration = None
        self._display_name = None
        self._carrier_account_services = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.account_code = account_code
        if carrier_id is not None:
            self.carrier_id = carrier_id
        if carrier_integration_id is not None:
            self.carrier_integration_id = carrier_integration_id
        if carrier_integration is not None:
            self.carrier_integration = carrier_integration
        if display_name is not None:
            self.display_name = display_name
        if carrier_account_services is not None:
            self.carrier_account_services = carrier_account_services

    @property
    def id(self):
        """Gets the id of this BaseCarrierAccount.  # noqa: E501


        :return: The id of this BaseCarrierAccount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseCarrierAccount.


        :param id: The id of this BaseCarrierAccount.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BaseCarrierAccount.  # noqa: E501


        :return: The name of this BaseCarrierAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BaseCarrierAccount.


        :param name: The name of this BaseCarrierAccount.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def account_code(self):
        """Gets the account_code of this BaseCarrierAccount.  # noqa: E501


        :return: The account_code of this BaseCarrierAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this BaseCarrierAccount.


        :param account_code: The account_code of this BaseCarrierAccount.  # noqa: E501
        :type: str
        """
        if account_code is None:
            raise ValueError("Invalid value for `account_code`, must not be `None`")  # noqa: E501

        self._account_code = account_code

    @property
    def carrier_id(self):
        """Gets the carrier_id of this BaseCarrierAccount.  # noqa: E501


        :return: The carrier_id of this BaseCarrierAccount.  # noqa: E501
        :rtype: int
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this BaseCarrierAccount.


        :param carrier_id: The carrier_id of this BaseCarrierAccount.  # noqa: E501
        :type: int
        """

        self._carrier_id = carrier_id

    @property
    def carrier_integration_id(self):
        """Gets the carrier_integration_id of this BaseCarrierAccount.  # noqa: E501


        :return: The carrier_integration_id of this BaseCarrierAccount.  # noqa: E501
        :rtype: int
        """
        return self._carrier_integration_id

    @carrier_integration_id.setter
    def carrier_integration_id(self, carrier_integration_id):
        """Sets the carrier_integration_id of this BaseCarrierAccount.


        :param carrier_integration_id: The carrier_integration_id of this BaseCarrierAccount.  # noqa: E501
        :type: int
        """

        self._carrier_integration_id = carrier_integration_id

    @property
    def carrier_integration(self):
        """Gets the carrier_integration of this BaseCarrierAccount.  # noqa: E501


        :return: The carrier_integration of this BaseCarrierAccount.  # noqa: E501
        :rtype: CarrierIntegrationLite
        """
        return self._carrier_integration

    @carrier_integration.setter
    def carrier_integration(self, carrier_integration):
        """Sets the carrier_integration of this BaseCarrierAccount.


        :param carrier_integration: The carrier_integration of this BaseCarrierAccount.  # noqa: E501
        :type: CarrierIntegrationLite
        """

        self._carrier_integration = carrier_integration

    @property
    def display_name(self):
        """Gets the display_name of this BaseCarrierAccount.  # noqa: E501


        :return: The display_name of this BaseCarrierAccount.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BaseCarrierAccount.


        :param display_name: The display_name of this BaseCarrierAccount.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def carrier_account_services(self):
        """Gets the carrier_account_services of this BaseCarrierAccount.  # noqa: E501


        :return: The carrier_account_services of this BaseCarrierAccount.  # noqa: E501
        :rtype: list[CarrierAccountServiceModel]
        """
        return self._carrier_account_services

    @carrier_account_services.setter
    def carrier_account_services(self, carrier_account_services):
        """Sets the carrier_account_services of this BaseCarrierAccount.


        :param carrier_account_services: The carrier_account_services of this BaseCarrierAccount.  # noqa: E501
        :type: list[CarrierAccountServiceModel]
        """

        self._carrier_account_services = carrier_account_services

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
        if issubclass(BaseCarrierAccount, dict):
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
        if not isinstance(other, BaseCarrierAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
