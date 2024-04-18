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

class CarrierServiceGroup(object):
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
        'carrier_id': 'int',
        'carrier': 'Carrier',
        'carrier_services': 'list[CarrierServiceModel]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'carrier_id': 'carrierId',
        'carrier': 'carrier',
        'carrier_services': 'carrierServices'
    }

    def __init__(self, id=None, name=None, carrier_id=None, carrier=None, carrier_services=None):  # noqa: E501
        """CarrierServiceGroup - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._carrier_id = None
        self._carrier = None
        self._carrier_services = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if carrier_id is not None:
            self.carrier_id = carrier_id
        if carrier is not None:
            self.carrier = carrier
        if carrier_services is not None:
            self.carrier_services = carrier_services

    @property
    def id(self):
        """Gets the id of this CarrierServiceGroup.  # noqa: E501


        :return: The id of this CarrierServiceGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CarrierServiceGroup.


        :param id: The id of this CarrierServiceGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CarrierServiceGroup.  # noqa: E501


        :return: The name of this CarrierServiceGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CarrierServiceGroup.


        :param name: The name of this CarrierServiceGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def carrier_id(self):
        """Gets the carrier_id of this CarrierServiceGroup.  # noqa: E501


        :return: The carrier_id of this CarrierServiceGroup.  # noqa: E501
        :rtype: int
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this CarrierServiceGroup.


        :param carrier_id: The carrier_id of this CarrierServiceGroup.  # noqa: E501
        :type: int
        """

        self._carrier_id = carrier_id

    @property
    def carrier(self):
        """Gets the carrier of this CarrierServiceGroup.  # noqa: E501


        :return: The carrier of this CarrierServiceGroup.  # noqa: E501
        :rtype: Carrier
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this CarrierServiceGroup.


        :param carrier: The carrier of this CarrierServiceGroup.  # noqa: E501
        :type: Carrier
        """

        self._carrier = carrier

    @property
    def carrier_services(self):
        """Gets the carrier_services of this CarrierServiceGroup.  # noqa: E501


        :return: The carrier_services of this CarrierServiceGroup.  # noqa: E501
        :rtype: list[CarrierServiceModel]
        """
        return self._carrier_services

    @carrier_services.setter
    def carrier_services(self, carrier_services):
        """Sets the carrier_services of this CarrierServiceGroup.


        :param carrier_services: The carrier_services of this CarrierServiceGroup.  # noqa: E501
        :type: list[CarrierServiceModel]
        """

        self._carrier_services = carrier_services

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
        if issubclass(CarrierServiceGroup, dict):
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
        if not isinstance(other, CarrierServiceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
