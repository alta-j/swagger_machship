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

class TimeZoneModel(object):
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
        'js_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'js_name': 'jsName'
    }

    def __init__(self, id=None, name=None, js_name=None):  # noqa: E501
        """TimeZoneModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._js_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if js_name is not None:
            self.js_name = js_name

    @property
    def id(self):
        """Gets the id of this TimeZoneModel.  # noqa: E501


        :return: The id of this TimeZoneModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimeZoneModel.


        :param id: The id of this TimeZoneModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TimeZoneModel.  # noqa: E501


        :return: The name of this TimeZoneModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TimeZoneModel.


        :param name: The name of this TimeZoneModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def js_name(self):
        """Gets the js_name of this TimeZoneModel.  # noqa: E501


        :return: The js_name of this TimeZoneModel.  # noqa: E501
        :rtype: str
        """
        return self._js_name

    @js_name.setter
    def js_name(self, js_name):
        """Sets the js_name of this TimeZoneModel.


        :param js_name: The js_name of this TimeZoneModel.  # noqa: E501
        :type: str
        """

        self._js_name = js_name

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
        if issubclass(TimeZoneModel, dict):
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
        if not isinstance(other, TimeZoneModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other