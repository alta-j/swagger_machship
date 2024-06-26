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

class CreateConsignmentCombinedLoadSizeItemV2(object):
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
        'length': 'float',
        'height': 'float',
        'weight': 'float',
        'width': 'float'
    }

    attribute_map = {
        'length': 'length',
        'height': 'height',
        'weight': 'weight',
        'width': 'width'
    }

    def __init__(self, length=None, height=None, weight=None, width=None):  # noqa: E501
        """CreateConsignmentCombinedLoadSizeItemV2 - a model defined in Swagger"""  # noqa: E501
        self._length = None
        self._height = None
        self._weight = None
        self._width = None
        self.discriminator = None
        if length is not None:
            self.length = length
        if height is not None:
            self.height = height
        if weight is not None:
            self.weight = weight
        if width is not None:
            self.width = width

    @property
    def length(self):
        """Gets the length of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501


        :return: The length of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this CreateConsignmentCombinedLoadSizeItemV2.


        :param length: The length of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def height(self):
        """Gets the height of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501


        :return: The height of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CreateConsignmentCombinedLoadSizeItemV2.


        :param height: The height of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def weight(self):
        """Gets the weight of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501


        :return: The weight of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateConsignmentCombinedLoadSizeItemV2.


        :param weight: The weight of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def width(self):
        """Gets the width of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501


        :return: The width of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CreateConsignmentCombinedLoadSizeItemV2.


        :param width: The width of this CreateConsignmentCombinedLoadSizeItemV2.  # noqa: E501
        :type: float
        """

        self._width = width

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
        if issubclass(CreateConsignmentCombinedLoadSizeItemV2, dict):
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
        if not isinstance(other, CreateConsignmentCombinedLoadSizeItemV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
