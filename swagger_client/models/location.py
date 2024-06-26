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

class Location(object):
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
        'postcode': 'str',
        'state': 'State',
        'state_id': 'int',
        'time_zone_id': 'int',
        'time_zone': 'TimeZoneModel',
        'suburb': 'str',
        'search_str': 'str',
        'country_code': 'str',
        'description': 'str',
        'description_short': 'str',
        'is_from': 'bool',
        'location_aliases': 'list[LocationAlias]',
        'location_type': 'LocationType',
        'country_id': 'int',
        'country': 'Country',
        'sub_locality': 'str'
    }

    attribute_map = {
        'id': 'id',
        'postcode': 'postcode',
        'state': 'state',
        'state_id': 'stateId',
        'time_zone_id': 'timeZoneId',
        'time_zone': 'timeZone',
        'suburb': 'suburb',
        'search_str': 'searchStr',
        'country_code': 'countryCode',
        'description': 'description',
        'description_short': 'descriptionShort',
        'is_from': 'isFrom',
        'location_aliases': 'locationAliases',
        'location_type': 'locationType',
        'country_id': 'countryId',
        'country': 'country',
        'sub_locality': 'subLocality'
    }

    def __init__(self, id=None, postcode=None, state=None, state_id=None, time_zone_id=None, time_zone=None, suburb=None, search_str=None, country_code=None, description=None, description_short=None, is_from=None, location_aliases=None, location_type=None, country_id=None, country=None, sub_locality=None):  # noqa: E501
        """Location - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._postcode = None
        self._state = None
        self._state_id = None
        self._time_zone_id = None
        self._time_zone = None
        self._suburb = None
        self._search_str = None
        self._country_code = None
        self._description = None
        self._description_short = None
        self._is_from = None
        self._location_aliases = None
        self._location_type = None
        self._country_id = None
        self._country = None
        self._sub_locality = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if postcode is not None:
            self.postcode = postcode
        if state is not None:
            self.state = state
        if state_id is not None:
            self.state_id = state_id
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if time_zone is not None:
            self.time_zone = time_zone
        if suburb is not None:
            self.suburb = suburb
        if search_str is not None:
            self.search_str = search_str
        if country_code is not None:
            self.country_code = country_code
        if description is not None:
            self.description = description
        if description_short is not None:
            self.description_short = description_short
        if is_from is not None:
            self.is_from = is_from
        if location_aliases is not None:
            self.location_aliases = location_aliases
        if location_type is not None:
            self.location_type = location_type
        if country_id is not None:
            self.country_id = country_id
        if country is not None:
            self.country = country
        if sub_locality is not None:
            self.sub_locality = sub_locality

    @property
    def id(self):
        """Gets the id of this Location.  # noqa: E501


        :return: The id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Location.


        :param id: The id of this Location.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def postcode(self):
        """Gets the postcode of this Location.  # noqa: E501


        :return: The postcode of this Location.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this Location.


        :param postcode: The postcode of this Location.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def state(self):
        """Gets the state of this Location.  # noqa: E501


        :return: The state of this Location.  # noqa: E501
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Location.


        :param state: The state of this Location.  # noqa: E501
        :type: State
        """

        self._state = state

    @property
    def state_id(self):
        """Gets the state_id of this Location.  # noqa: E501


        :return: The state_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """Sets the state_id of this Location.


        :param state_id: The state_id of this Location.  # noqa: E501
        :type: int
        """

        self._state_id = state_id

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this Location.  # noqa: E501


        :return: The time_zone_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this Location.


        :param time_zone_id: The time_zone_id of this Location.  # noqa: E501
        :type: int
        """

        self._time_zone_id = time_zone_id

    @property
    def time_zone(self):
        """Gets the time_zone of this Location.  # noqa: E501


        :return: The time_zone of this Location.  # noqa: E501
        :rtype: TimeZoneModel
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Location.


        :param time_zone: The time_zone of this Location.  # noqa: E501
        :type: TimeZoneModel
        """

        self._time_zone = time_zone

    @property
    def suburb(self):
        """Gets the suburb of this Location.  # noqa: E501


        :return: The suburb of this Location.  # noqa: E501
        :rtype: str
        """
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        """Sets the suburb of this Location.


        :param suburb: The suburb of this Location.  # noqa: E501
        :type: str
        """

        self._suburb = suburb

    @property
    def search_str(self):
        """Gets the search_str of this Location.  # noqa: E501

        used if the user only passed in a string for the location. Location Service will then try to find location based on str  # noqa: E501

        :return: The search_str of this Location.  # noqa: E501
        :rtype: str
        """
        return self._search_str

    @search_str.setter
    def search_str(self, search_str):
        """Sets the search_str of this Location.

        used if the user only passed in a string for the location. Location Service will then try to find location based on str  # noqa: E501

        :param search_str: The search_str of this Location.  # noqa: E501
        :type: str
        """

        self._search_str = search_str

    @property
    def country_code(self):
        """Gets the country_code of this Location.  # noqa: E501

        The country code is used to determine the international location  # noqa: E501

        :return: The country_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Location.

        The country code is used to determine the international location  # noqa: E501

        :param country_code: The country_code of this Location.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def description(self):
        """Gets the description of this Location.  # noqa: E501


        :return: The description of this Location.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Location.


        :param description: The description of this Location.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def description_short(self):
        """Gets the description_short of this Location.  # noqa: E501


        :return: The description_short of this Location.  # noqa: E501
        :rtype: str
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """Sets the description_short of this Location.


        :param description_short: The description_short of this Location.  # noqa: E501
        :type: str
        """

        self._description_short = description_short

    @property
    def is_from(self):
        """Gets the is_from of this Location.  # noqa: E501


        :return: The is_from of this Location.  # noqa: E501
        :rtype: bool
        """
        return self._is_from

    @is_from.setter
    def is_from(self, is_from):
        """Sets the is_from of this Location.


        :param is_from: The is_from of this Location.  # noqa: E501
        :type: bool
        """

        self._is_from = is_from

    @property
    def location_aliases(self):
        """Gets the location_aliases of this Location.  # noqa: E501


        :return: The location_aliases of this Location.  # noqa: E501
        :rtype: list[LocationAlias]
        """
        return self._location_aliases

    @location_aliases.setter
    def location_aliases(self, location_aliases):
        """Sets the location_aliases of this Location.


        :param location_aliases: The location_aliases of this Location.  # noqa: E501
        :type: list[LocationAlias]
        """

        self._location_aliases = location_aliases

    @property
    def location_type(self):
        """Gets the location_type of this Location.  # noqa: E501


        :return: The location_type of this Location.  # noqa: E501
        :rtype: LocationType
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this Location.


        :param location_type: The location_type of this Location.  # noqa: E501
        :type: LocationType
        """

        self._location_type = location_type

    @property
    def country_id(self):
        """Gets the country_id of this Location.  # noqa: E501


        :return: The country_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this Location.


        :param country_id: The country_id of this Location.  # noqa: E501
        :type: int
        """

        self._country_id = country_id

    @property
    def country(self):
        """Gets the country of this Location.  # noqa: E501


        :return: The country of this Location.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Location.


        :param country: The country of this Location.  # noqa: E501
        :type: Country
        """

        self._country = country

    @property
    def sub_locality(self):
        """Gets the sub_locality of this Location.  # noqa: E501


        :return: The sub_locality of this Location.  # noqa: E501
        :rtype: str
        """
        return self._sub_locality

    @sub_locality.setter
    def sub_locality(self, sub_locality):
        """Sets the sub_locality of this Location.


        :param sub_locality: The sub_locality of this Location.  # noqa: E501
        :type: str
        """

        self._sub_locality = sub_locality

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
        if issubclass(Location, dict):
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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
