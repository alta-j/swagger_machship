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

class Role(object):
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
        'company': 'CompanyLite',
        'users': 'list[User]',
        'components': 'list[Component]',
        'user_type': 'UserType'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'company': 'company',
        'users': 'users',
        'components': 'components',
        'user_type': 'userType'
    }

    def __init__(self, id=None, name=None, company=None, users=None, components=None, user_type=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._company = None
        self._users = None
        self._components = None
        self._user_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if company is not None:
            self.company = company
        if users is not None:
            self.users = users
        if components is not None:
            self.components = components
        if user_type is not None:
            self.user_type = user_type

    @property
    def id(self):
        """Gets the id of this Role.  # noqa: E501


        :return: The id of this Role.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.


        :param id: The id of this Role.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Role.  # noqa: E501


        :return: The name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Role.


        :param name: The name of this Role.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def company(self):
        """Gets the company of this Role.  # noqa: E501


        :return: The company of this Role.  # noqa: E501
        :rtype: CompanyLite
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Role.


        :param company: The company of this Role.  # noqa: E501
        :type: CompanyLite
        """

        self._company = company

    @property
    def users(self):
        """Gets the users of this Role.  # noqa: E501


        :return: The users of this Role.  # noqa: E501
        :rtype: list[User]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Role.


        :param users: The users of this Role.  # noqa: E501
        :type: list[User]
        """

        self._users = users

    @property
    def components(self):
        """Gets the components of this Role.  # noqa: E501


        :return: The components of this Role.  # noqa: E501
        :rtype: list[Component]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this Role.


        :param components: The components of this Role.  # noqa: E501
        :type: list[Component]
        """

        self._components = components

    @property
    def user_type(self):
        """Gets the user_type of this Role.  # noqa: E501


        :return: The user_type of this Role.  # noqa: E501
        :rtype: UserType
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this Role.


        :param user_type: The user_type of this Role.  # noqa: E501
        :type: UserType
        """

        self._user_type = user_type

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
