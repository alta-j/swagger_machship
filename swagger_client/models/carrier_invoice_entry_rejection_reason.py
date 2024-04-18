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

class CarrierInvoiceEntryRejectionReason(object):
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
        'reason_type': 'RejectionType',
        'requires_comment': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'reason_type': 'reasonType',
        'requires_comment': 'requiresComment'
    }

    def __init__(self, id=None, name=None, reason_type=None, requires_comment=None):  # noqa: E501
        """CarrierInvoiceEntryRejectionReason - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._reason_type = None
        self._requires_comment = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if reason_type is not None:
            self.reason_type = reason_type
        if requires_comment is not None:
            self.requires_comment = requires_comment

    @property
    def id(self):
        """Gets the id of this CarrierInvoiceEntryRejectionReason.  # noqa: E501


        :return: The id of this CarrierInvoiceEntryRejectionReason.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CarrierInvoiceEntryRejectionReason.


        :param id: The id of this CarrierInvoiceEntryRejectionReason.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CarrierInvoiceEntryRejectionReason.  # noqa: E501


        :return: The name of this CarrierInvoiceEntryRejectionReason.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CarrierInvoiceEntryRejectionReason.


        :param name: The name of this CarrierInvoiceEntryRejectionReason.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reason_type(self):
        """Gets the reason_type of this CarrierInvoiceEntryRejectionReason.  # noqa: E501


        :return: The reason_type of this CarrierInvoiceEntryRejectionReason.  # noqa: E501
        :rtype: RejectionType
        """
        return self._reason_type

    @reason_type.setter
    def reason_type(self, reason_type):
        """Sets the reason_type of this CarrierInvoiceEntryRejectionReason.


        :param reason_type: The reason_type of this CarrierInvoiceEntryRejectionReason.  # noqa: E501
        :type: RejectionType
        """

        self._reason_type = reason_type

    @property
    def requires_comment(self):
        """Gets the requires_comment of this CarrierInvoiceEntryRejectionReason.  # noqa: E501


        :return: The requires_comment of this CarrierInvoiceEntryRejectionReason.  # noqa: E501
        :rtype: bool
        """
        return self._requires_comment

    @requires_comment.setter
    def requires_comment(self, requires_comment):
        """Sets the requires_comment of this CarrierInvoiceEntryRejectionReason.


        :param requires_comment: The requires_comment of this CarrierInvoiceEntryRejectionReason.  # noqa: E501
        :type: bool
        """

        self._requires_comment = requires_comment

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
        if issubclass(CarrierInvoiceEntryRejectionReason, dict):
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
        if not isinstance(other, CarrierInvoiceEntryRejectionReason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other