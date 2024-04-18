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

class RouteServiceType(object):
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
        'abbreviation': 'str',
        'guid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'abbreviation': 'abbreviation',
        'guid': 'guid'
    }

    def __init__(self, id=None, name=None, abbreviation=None, guid=None):  # noqa: E501
        """RouteServiceType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._abbreviation = None
        self._guid = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if guid is not None:
            self.guid = guid

    @property
    def id(self):
        """Gets the id of this RouteServiceType.  # noqa: E501


        :return: The id of this RouteServiceType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RouteServiceType.


        :param id: The id of this RouteServiceType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RouteServiceType.  # noqa: E501


        :return: The name of this RouteServiceType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RouteServiceType.


        :param name: The name of this RouteServiceType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this RouteServiceType.  # noqa: E501


        :return: The abbreviation of this RouteServiceType.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this RouteServiceType.


        :param abbreviation: The abbreviation of this RouteServiceType.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def guid(self):
        """Gets the guid of this RouteServiceType.  # noqa: E501


        :return: The guid of this RouteServiceType.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this RouteServiceType.


        :param guid: The guid of this RouteServiceType.  # noqa: E501
        :type: str
        """

        self._guid = guid

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
        if issubclass(RouteServiceType, dict):
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
        if not isinstance(other, RouteServiceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
