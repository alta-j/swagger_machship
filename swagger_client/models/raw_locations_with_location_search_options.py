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

class RawLocationsWithLocationSearchOptions(object):
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
        'raw_locations': 'list[RawLocation]',
        'location_search_options': 'LocationSearchOptions'
    }

    attribute_map = {
        'raw_locations': 'rawLocations',
        'location_search_options': 'locationSearchOptions'
    }

    def __init__(self, raw_locations=None, location_search_options=None):  # noqa: E501
        """RawLocationsWithLocationSearchOptions - a model defined in Swagger"""  # noqa: E501
        self._raw_locations = None
        self._location_search_options = None
        self.discriminator = None
        if raw_locations is not None:
            self.raw_locations = raw_locations
        if location_search_options is not None:
            self.location_search_options = location_search_options

    @property
    def raw_locations(self):
        """Gets the raw_locations of this RawLocationsWithLocationSearchOptions.  # noqa: E501


        :return: The raw_locations of this RawLocationsWithLocationSearchOptions.  # noqa: E501
        :rtype: list[RawLocation]
        """
        return self._raw_locations

    @raw_locations.setter
    def raw_locations(self, raw_locations):
        """Sets the raw_locations of this RawLocationsWithLocationSearchOptions.


        :param raw_locations: The raw_locations of this RawLocationsWithLocationSearchOptions.  # noqa: E501
        :type: list[RawLocation]
        """

        self._raw_locations = raw_locations

    @property
    def location_search_options(self):
        """Gets the location_search_options of this RawLocationsWithLocationSearchOptions.  # noqa: E501


        :return: The location_search_options of this RawLocationsWithLocationSearchOptions.  # noqa: E501
        :rtype: LocationSearchOptions
        """
        return self._location_search_options

    @location_search_options.setter
    def location_search_options(self, location_search_options):
        """Sets the location_search_options of this RawLocationsWithLocationSearchOptions.


        :param location_search_options: The location_search_options of this RawLocationsWithLocationSearchOptions.  # noqa: E501
        :type: LocationSearchOptions
        """

        self._location_search_options = location_search_options

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
        if issubclass(RawLocationsWithLocationSearchOptions, dict):
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
        if not isinstance(other, RawLocationsWithLocationSearchOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other