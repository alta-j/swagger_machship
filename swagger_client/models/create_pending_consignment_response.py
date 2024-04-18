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

class CreatePendingConsignmentResponse(object):
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
        'consignment_number': 'str'
    }

    attribute_map = {
        'id': 'id',
        'consignment_number': 'consignmentNumber'
    }

    def __init__(self, id=None, consignment_number=None):  # noqa: E501
        """CreatePendingConsignmentResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._consignment_number = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if consignment_number is not None:
            self.consignment_number = consignment_number

    @property
    def id(self):
        """Gets the id of this CreatePendingConsignmentResponse.  # noqa: E501


        :return: The id of this CreatePendingConsignmentResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatePendingConsignmentResponse.


        :param id: The id of this CreatePendingConsignmentResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def consignment_number(self):
        """Gets the consignment_number of this CreatePendingConsignmentResponse.  # noqa: E501


        :return: The consignment_number of this CreatePendingConsignmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._consignment_number

    @consignment_number.setter
    def consignment_number(self, consignment_number):
        """Sets the consignment_number of this CreatePendingConsignmentResponse.


        :param consignment_number: The consignment_number of this CreatePendingConsignmentResponse.  # noqa: E501
        :type: str
        """

        self._consignment_number = consignment_number

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
        if issubclass(CreatePendingConsignmentResponse, dict):
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
        if not isinstance(other, CreatePendingConsignmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
