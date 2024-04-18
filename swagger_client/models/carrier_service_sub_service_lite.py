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

class CarrierServiceSubServiceLite(object):
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
        'serialised_settings': 'str',
        'is_default': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'abbreviation': 'abbreviation',
        'serialised_settings': 'serialisedSettings',
        'is_default': 'isDefault'
    }

    def __init__(self, id=None, name=None, abbreviation=None, serialised_settings=None, is_default=None):  # noqa: E501
        """CarrierServiceSubServiceLite - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._abbreviation = None
        self._serialised_settings = None
        self._is_default = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if serialised_settings is not None:
            self.serialised_settings = serialised_settings
        if is_default is not None:
            self.is_default = is_default

    @property
    def id(self):
        """Gets the id of this CarrierServiceSubServiceLite.  # noqa: E501


        :return: The id of this CarrierServiceSubServiceLite.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CarrierServiceSubServiceLite.


        :param id: The id of this CarrierServiceSubServiceLite.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CarrierServiceSubServiceLite.  # noqa: E501


        :return: The name of this CarrierServiceSubServiceLite.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CarrierServiceSubServiceLite.


        :param name: The name of this CarrierServiceSubServiceLite.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this CarrierServiceSubServiceLite.  # noqa: E501


        :return: The abbreviation of this CarrierServiceSubServiceLite.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this CarrierServiceSubServiceLite.


        :param abbreviation: The abbreviation of this CarrierServiceSubServiceLite.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def serialised_settings(self):
        """Gets the serialised_settings of this CarrierServiceSubServiceLite.  # noqa: E501


        :return: The serialised_settings of this CarrierServiceSubServiceLite.  # noqa: E501
        :rtype: str
        """
        return self._serialised_settings

    @serialised_settings.setter
    def serialised_settings(self, serialised_settings):
        """Sets the serialised_settings of this CarrierServiceSubServiceLite.


        :param serialised_settings: The serialised_settings of this CarrierServiceSubServiceLite.  # noqa: E501
        :type: str
        """

        self._serialised_settings = serialised_settings

    @property
    def is_default(self):
        """Gets the is_default of this CarrierServiceSubServiceLite.  # noqa: E501


        :return: The is_default of this CarrierServiceSubServiceLite.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this CarrierServiceSubServiceLite.


        :param is_default: The is_default of this CarrierServiceSubServiceLite.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

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
        if issubclass(CarrierServiceSubServiceLite, dict):
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
        if not isinstance(other, CarrierServiceSubServiceLite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
