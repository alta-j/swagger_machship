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

class OrganisationLinkDetail(object):
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
        'from_organisation_details': 'OrganisationDetail',
        'to_organisation_details': 'OrganisationDetail'
    }

    attribute_map = {
        'id': 'id',
        'from_organisation_details': 'fromOrganisationDetails',
        'to_organisation_details': 'toOrganisationDetails'
    }

    def __init__(self, id=None, from_organisation_details=None, to_organisation_details=None):  # noqa: E501
        """OrganisationLinkDetail - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._from_organisation_details = None
        self._to_organisation_details = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if from_organisation_details is not None:
            self.from_organisation_details = from_organisation_details
        if to_organisation_details is not None:
            self.to_organisation_details = to_organisation_details

    @property
    def id(self):
        """Gets the id of this OrganisationLinkDetail.  # noqa: E501

        The ID of the link in MachShip  # noqa: E501

        :return: The id of this OrganisationLinkDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganisationLinkDetail.

        The ID of the link in MachShip  # noqa: E501

        :param id: The id of this OrganisationLinkDetail.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def from_organisation_details(self):
        """Gets the from_organisation_details of this OrganisationLinkDetail.  # noqa: E501


        :return: The from_organisation_details of this OrganisationLinkDetail.  # noqa: E501
        :rtype: OrganisationDetail
        """
        return self._from_organisation_details

    @from_organisation_details.setter
    def from_organisation_details(self, from_organisation_details):
        """Sets the from_organisation_details of this OrganisationLinkDetail.


        :param from_organisation_details: The from_organisation_details of this OrganisationLinkDetail.  # noqa: E501
        :type: OrganisationDetail
        """

        self._from_organisation_details = from_organisation_details

    @property
    def to_organisation_details(self):
        """Gets the to_organisation_details of this OrganisationLinkDetail.  # noqa: E501


        :return: The to_organisation_details of this OrganisationLinkDetail.  # noqa: E501
        :rtype: OrganisationDetail
        """
        return self._to_organisation_details

    @to_organisation_details.setter
    def to_organisation_details(self, to_organisation_details):
        """Sets the to_organisation_details of this OrganisationLinkDetail.


        :param to_organisation_details: The to_organisation_details of this OrganisationLinkDetail.  # noqa: E501
        :type: OrganisationDetail
        """

        self._to_organisation_details = to_organisation_details

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
        if issubclass(OrganisationLinkDetail, dict):
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
        if not isinstance(other, OrganisationLinkDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
