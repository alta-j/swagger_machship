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

class CompanyLocationReceiverAccount(object):
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
        'company_location_id': 'int',
        'company_location': 'CompanyLocation',
        'receiver_account_id': 'int',
        'receiver_account': 'ReceiverAccount'
    }

    attribute_map = {
        'id': 'id',
        'company_location_id': 'companyLocationId',
        'company_location': 'companyLocation',
        'receiver_account_id': 'receiverAccountId',
        'receiver_account': 'receiverAccount'
    }

    def __init__(self, id=None, company_location_id=None, company_location=None, receiver_account_id=None, receiver_account=None):  # noqa: E501
        """CompanyLocationReceiverAccount - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._company_location_id = None
        self._company_location = None
        self._receiver_account_id = None
        self._receiver_account = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if company_location_id is not None:
            self.company_location_id = company_location_id
        if company_location is not None:
            self.company_location = company_location
        if receiver_account_id is not None:
            self.receiver_account_id = receiver_account_id
        if receiver_account is not None:
            self.receiver_account = receiver_account

    @property
    def id(self):
        """Gets the id of this CompanyLocationReceiverAccount.  # noqa: E501


        :return: The id of this CompanyLocationReceiverAccount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyLocationReceiverAccount.


        :param id: The id of this CompanyLocationReceiverAccount.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def company_location_id(self):
        """Gets the company_location_id of this CompanyLocationReceiverAccount.  # noqa: E501


        :return: The company_location_id of this CompanyLocationReceiverAccount.  # noqa: E501
        :rtype: int
        """
        return self._company_location_id

    @company_location_id.setter
    def company_location_id(self, company_location_id):
        """Sets the company_location_id of this CompanyLocationReceiverAccount.


        :param company_location_id: The company_location_id of this CompanyLocationReceiverAccount.  # noqa: E501
        :type: int
        """

        self._company_location_id = company_location_id

    @property
    def company_location(self):
        """Gets the company_location of this CompanyLocationReceiverAccount.  # noqa: E501


        :return: The company_location of this CompanyLocationReceiverAccount.  # noqa: E501
        :rtype: CompanyLocation
        """
        return self._company_location

    @company_location.setter
    def company_location(self, company_location):
        """Sets the company_location of this CompanyLocationReceiverAccount.


        :param company_location: The company_location of this CompanyLocationReceiverAccount.  # noqa: E501
        :type: CompanyLocation
        """

        self._company_location = company_location

    @property
    def receiver_account_id(self):
        """Gets the receiver_account_id of this CompanyLocationReceiverAccount.  # noqa: E501


        :return: The receiver_account_id of this CompanyLocationReceiverAccount.  # noqa: E501
        :rtype: int
        """
        return self._receiver_account_id

    @receiver_account_id.setter
    def receiver_account_id(self, receiver_account_id):
        """Sets the receiver_account_id of this CompanyLocationReceiverAccount.


        :param receiver_account_id: The receiver_account_id of this CompanyLocationReceiverAccount.  # noqa: E501
        :type: int
        """

        self._receiver_account_id = receiver_account_id

    @property
    def receiver_account(self):
        """Gets the receiver_account of this CompanyLocationReceiverAccount.  # noqa: E501


        :return: The receiver_account of this CompanyLocationReceiverAccount.  # noqa: E501
        :rtype: ReceiverAccount
        """
        return self._receiver_account

    @receiver_account.setter
    def receiver_account(self, receiver_account):
        """Sets the receiver_account of this CompanyLocationReceiverAccount.


        :param receiver_account: The receiver_account of this CompanyLocationReceiverAccount.  # noqa: E501
        :type: ReceiverAccount
        """

        self._receiver_account = receiver_account

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
        if issubclass(CompanyLocationReceiverAccount, dict):
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
        if not isinstance(other, CompanyLocationReceiverAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
