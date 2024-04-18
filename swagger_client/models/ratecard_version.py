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

class RatecardVersion(object):
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
        'ratecard_id': 'int',
        'ratecard': 'RatecardLite',
        'effective_date': 'datetime',
        'total_rows': 'int',
        'rate_count': 'int',
        'display_name': 'str',
        'effective_date_display_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ratecard_id': 'ratecardId',
        'ratecard': 'ratecard',
        'effective_date': 'effectiveDate',
        'total_rows': 'totalRows',
        'rate_count': 'rateCount',
        'display_name': 'displayName',
        'effective_date_display_name': 'effectiveDateDisplayName'
    }

    def __init__(self, id=None, ratecard_id=None, ratecard=None, effective_date=None, total_rows=None, rate_count=None, display_name=None, effective_date_display_name=None):  # noqa: E501
        """RatecardVersion - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._ratecard_id = None
        self._ratecard = None
        self._effective_date = None
        self._total_rows = None
        self._rate_count = None
        self._display_name = None
        self._effective_date_display_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if ratecard_id is not None:
            self.ratecard_id = ratecard_id
        if ratecard is not None:
            self.ratecard = ratecard
        if effective_date is not None:
            self.effective_date = effective_date
        if total_rows is not None:
            self.total_rows = total_rows
        if rate_count is not None:
            self.rate_count = rate_count
        if display_name is not None:
            self.display_name = display_name
        if effective_date_display_name is not None:
            self.effective_date_display_name = effective_date_display_name

    @property
    def id(self):
        """Gets the id of this RatecardVersion.  # noqa: E501


        :return: The id of this RatecardVersion.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RatecardVersion.


        :param id: The id of this RatecardVersion.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ratecard_id(self):
        """Gets the ratecard_id of this RatecardVersion.  # noqa: E501


        :return: The ratecard_id of this RatecardVersion.  # noqa: E501
        :rtype: int
        """
        return self._ratecard_id

    @ratecard_id.setter
    def ratecard_id(self, ratecard_id):
        """Sets the ratecard_id of this RatecardVersion.


        :param ratecard_id: The ratecard_id of this RatecardVersion.  # noqa: E501
        :type: int
        """

        self._ratecard_id = ratecard_id

    @property
    def ratecard(self):
        """Gets the ratecard of this RatecardVersion.  # noqa: E501


        :return: The ratecard of this RatecardVersion.  # noqa: E501
        :rtype: RatecardLite
        """
        return self._ratecard

    @ratecard.setter
    def ratecard(self, ratecard):
        """Sets the ratecard of this RatecardVersion.


        :param ratecard: The ratecard of this RatecardVersion.  # noqa: E501
        :type: RatecardLite
        """

        self._ratecard = ratecard

    @property
    def effective_date(self):
        """Gets the effective_date of this RatecardVersion.  # noqa: E501


        :return: The effective_date of this RatecardVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this RatecardVersion.


        :param effective_date: The effective_date of this RatecardVersion.  # noqa: E501
        :type: datetime
        """

        self._effective_date = effective_date

    @property
    def total_rows(self):
        """Gets the total_rows of this RatecardVersion.  # noqa: E501


        :return: The total_rows of this RatecardVersion.  # noqa: E501
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this RatecardVersion.


        :param total_rows: The total_rows of this RatecardVersion.  # noqa: E501
        :type: int
        """

        self._total_rows = total_rows

    @property
    def rate_count(self):
        """Gets the rate_count of this RatecardVersion.  # noqa: E501


        :return: The rate_count of this RatecardVersion.  # noqa: E501
        :rtype: int
        """
        return self._rate_count

    @rate_count.setter
    def rate_count(self, rate_count):
        """Sets the rate_count of this RatecardVersion.


        :param rate_count: The rate_count of this RatecardVersion.  # noqa: E501
        :type: int
        """

        self._rate_count = rate_count

    @property
    def display_name(self):
        """Gets the display_name of this RatecardVersion.  # noqa: E501


        :return: The display_name of this RatecardVersion.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this RatecardVersion.


        :param display_name: The display_name of this RatecardVersion.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def effective_date_display_name(self):
        """Gets the effective_date_display_name of this RatecardVersion.  # noqa: E501


        :return: The effective_date_display_name of this RatecardVersion.  # noqa: E501
        :rtype: str
        """
        return self._effective_date_display_name

    @effective_date_display_name.setter
    def effective_date_display_name(self, effective_date_display_name):
        """Sets the effective_date_display_name of this RatecardVersion.


        :param effective_date_display_name: The effective_date_display_name of this RatecardVersion.  # noqa: E501
        :type: str
        """

        self._effective_date_display_name = effective_date_display_name

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
        if issubclass(RatecardVersion, dict):
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
        if not isinstance(other, RatecardVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other