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

class IdentityCompanyLink(object):
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
        'company': 'CompanyV2',
        'roles': 'list[RoleV2]'
    }

    attribute_map = {
        'company': 'company',
        'roles': 'roles'
    }

    def __init__(self, company=None, roles=None):  # noqa: E501
        """IdentityCompanyLink - a model defined in Swagger"""  # noqa: E501
        self._company = None
        self._roles = None
        self.discriminator = None
        if company is not None:
            self.company = company
        if roles is not None:
            self.roles = roles

    @property
    def company(self):
        """Gets the company of this IdentityCompanyLink.  # noqa: E501


        :return: The company of this IdentityCompanyLink.  # noqa: E501
        :rtype: CompanyV2
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this IdentityCompanyLink.


        :param company: The company of this IdentityCompanyLink.  # noqa: E501
        :type: CompanyV2
        """

        self._company = company

    @property
    def roles(self):
        """Gets the roles of this IdentityCompanyLink.  # noqa: E501


        :return: The roles of this IdentityCompanyLink.  # noqa: E501
        :rtype: list[RoleV2]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this IdentityCompanyLink.


        :param roles: The roles of this IdentityCompanyLink.  # noqa: E501
        :type: list[RoleV2]
        """

        self._roles = roles

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
        if issubclass(IdentityCompanyLink, dict):
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
        if not isinstance(other, IdentityCompanyLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
