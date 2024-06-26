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

class CreateIdentityV2(object):
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
        'unique_id': 'str',
        'given_name': 'str',
        'family_name': 'str',
        'display_name': 'str',
        'email_address': 'str',
        'identifying_claim': 'str',
        'password': 'str',
        'phone': 'str',
        'business_phone': 'str',
        'mobile': 'str',
        'position': 'str',
        'notes': 'str',
        'enable_email_notifications': 'bool',
        'user_type': 'UserType',
        'test_mode_setting': 'UserTestModeSetting',
        'organisation_id': 'int',
        'identity_provider_id': 'int',
        'owning_company_id': 'int',
        'user_and_company_links': 'list[CreateIdentityUserAndCompanyLink]'
    }

    attribute_map = {
        'unique_id': 'uniqueId',
        'given_name': 'givenName',
        'family_name': 'familyName',
        'display_name': 'displayName',
        'email_address': 'emailAddress',
        'identifying_claim': 'identifyingClaim',
        'password': 'password',
        'phone': 'phone',
        'business_phone': 'businessPhone',
        'mobile': 'mobile',
        'position': 'position',
        'notes': 'notes',
        'enable_email_notifications': 'enableEmailNotifications',
        'user_type': 'userType',
        'test_mode_setting': 'testModeSetting',
        'organisation_id': 'organisationId',
        'identity_provider_id': 'identityProviderId',
        'owning_company_id': 'owningCompanyId',
        'user_and_company_links': 'userAndCompanyLinks'
    }

    def __init__(self, unique_id=None, given_name=None, family_name=None, display_name=None, email_address=None, identifying_claim=None, password=None, phone=None, business_phone=None, mobile=None, position=None, notes=None, enable_email_notifications=None, user_type=None, test_mode_setting=None, organisation_id=None, identity_provider_id=None, owning_company_id=None, user_and_company_links=None):  # noqa: E501
        """CreateIdentityV2 - a model defined in Swagger"""  # noqa: E501
        self._unique_id = None
        self._given_name = None
        self._family_name = None
        self._display_name = None
        self._email_address = None
        self._identifying_claim = None
        self._password = None
        self._phone = None
        self._business_phone = None
        self._mobile = None
        self._position = None
        self._notes = None
        self._enable_email_notifications = None
        self._user_type = None
        self._test_mode_setting = None
        self._organisation_id = None
        self._identity_provider_id = None
        self._owning_company_id = None
        self._user_and_company_links = None
        self.discriminator = None
        if unique_id is not None:
            self.unique_id = unique_id
        self.given_name = given_name
        self.family_name = family_name
        self.display_name = display_name
        self.email_address = email_address
        self.identifying_claim = identifying_claim
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if business_phone is not None:
            self.business_phone = business_phone
        if mobile is not None:
            self.mobile = mobile
        if position is not None:
            self.position = position
        if notes is not None:
            self.notes = notes
        if enable_email_notifications is not None:
            self.enable_email_notifications = enable_email_notifications
        if user_type is not None:
            self.user_type = user_type
        if test_mode_setting is not None:
            self.test_mode_setting = test_mode_setting
        self.organisation_id = organisation_id
        self.identity_provider_id = identity_provider_id
        self.owning_company_id = owning_company_id
        if user_and_company_links is not None:
            self.user_and_company_links = user_and_company_links

    @property
    def unique_id(self):
        """Gets the unique_id of this CreateIdentityV2.  # noqa: E501


        :return: The unique_id of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this CreateIdentityV2.


        :param unique_id: The unique_id of this CreateIdentityV2.  # noqa: E501
        :type: str
        """

        self._unique_id = unique_id

    @property
    def given_name(self):
        """Gets the given_name of this CreateIdentityV2.  # noqa: E501


        :return: The given_name of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this CreateIdentityV2.


        :param given_name: The given_name of this CreateIdentityV2.  # noqa: E501
        :type: str
        """
        if given_name is None:
            raise ValueError("Invalid value for `given_name`, must not be `None`")  # noqa: E501

        self._given_name = given_name

    @property
    def family_name(self):
        """Gets the family_name of this CreateIdentityV2.  # noqa: E501


        :return: The family_name of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this CreateIdentityV2.


        :param family_name: The family_name of this CreateIdentityV2.  # noqa: E501
        :type: str
        """
        if family_name is None:
            raise ValueError("Invalid value for `family_name`, must not be `None`")  # noqa: E501

        self._family_name = family_name

    @property
    def display_name(self):
        """Gets the display_name of this CreateIdentityV2.  # noqa: E501


        :return: The display_name of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateIdentityV2.


        :param display_name: The display_name of this CreateIdentityV2.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def email_address(self):
        """Gets the email_address of this CreateIdentityV2.  # noqa: E501


        :return: The email_address of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CreateIdentityV2.


        :param email_address: The email_address of this CreateIdentityV2.  # noqa: E501
        :type: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def identifying_claim(self):
        """Gets the identifying_claim of this CreateIdentityV2.  # noqa: E501


        :return: The identifying_claim of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._identifying_claim

    @identifying_claim.setter
    def identifying_claim(self, identifying_claim):
        """Sets the identifying_claim of this CreateIdentityV2.


        :param identifying_claim: The identifying_claim of this CreateIdentityV2.  # noqa: E501
        :type: str
        """
        if identifying_claim is None:
            raise ValueError("Invalid value for `identifying_claim`, must not be `None`")  # noqa: E501

        self._identifying_claim = identifying_claim

    @property
    def password(self):
        """Gets the password of this CreateIdentityV2.  # noqa: E501


        :return: The password of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateIdentityV2.


        :param password: The password of this CreateIdentityV2.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def phone(self):
        """Gets the phone of this CreateIdentityV2.  # noqa: E501


        :return: The phone of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CreateIdentityV2.


        :param phone: The phone of this CreateIdentityV2.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def business_phone(self):
        """Gets the business_phone of this CreateIdentityV2.  # noqa: E501


        :return: The business_phone of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._business_phone

    @business_phone.setter
    def business_phone(self, business_phone):
        """Sets the business_phone of this CreateIdentityV2.


        :param business_phone: The business_phone of this CreateIdentityV2.  # noqa: E501
        :type: str
        """

        self._business_phone = business_phone

    @property
    def mobile(self):
        """Gets the mobile of this CreateIdentityV2.  # noqa: E501


        :return: The mobile of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this CreateIdentityV2.


        :param mobile: The mobile of this CreateIdentityV2.  # noqa: E501
        :type: str
        """

        self._mobile = mobile

    @property
    def position(self):
        """Gets the position of this CreateIdentityV2.  # noqa: E501


        :return: The position of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CreateIdentityV2.


        :param position: The position of this CreateIdentityV2.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def notes(self):
        """Gets the notes of this CreateIdentityV2.  # noqa: E501


        :return: The notes of this CreateIdentityV2.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreateIdentityV2.


        :param notes: The notes of this CreateIdentityV2.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def enable_email_notifications(self):
        """Gets the enable_email_notifications of this CreateIdentityV2.  # noqa: E501


        :return: The enable_email_notifications of this CreateIdentityV2.  # noqa: E501
        :rtype: bool
        """
        return self._enable_email_notifications

    @enable_email_notifications.setter
    def enable_email_notifications(self, enable_email_notifications):
        """Sets the enable_email_notifications of this CreateIdentityV2.


        :param enable_email_notifications: The enable_email_notifications of this CreateIdentityV2.  # noqa: E501
        :type: bool
        """

        self._enable_email_notifications = enable_email_notifications

    @property
    def user_type(self):
        """Gets the user_type of this CreateIdentityV2.  # noqa: E501


        :return: The user_type of this CreateIdentityV2.  # noqa: E501
        :rtype: UserType
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this CreateIdentityV2.


        :param user_type: The user_type of this CreateIdentityV2.  # noqa: E501
        :type: UserType
        """

        self._user_type = user_type

    @property
    def test_mode_setting(self):
        """Gets the test_mode_setting of this CreateIdentityV2.  # noqa: E501


        :return: The test_mode_setting of this CreateIdentityV2.  # noqa: E501
        :rtype: UserTestModeSetting
        """
        return self._test_mode_setting

    @test_mode_setting.setter
    def test_mode_setting(self, test_mode_setting):
        """Sets the test_mode_setting of this CreateIdentityV2.


        :param test_mode_setting: The test_mode_setting of this CreateIdentityV2.  # noqa: E501
        :type: UserTestModeSetting
        """

        self._test_mode_setting = test_mode_setting

    @property
    def organisation_id(self):
        """Gets the organisation_id of this CreateIdentityV2.  # noqa: E501


        :return: The organisation_id of this CreateIdentityV2.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this CreateIdentityV2.


        :param organisation_id: The organisation_id of this CreateIdentityV2.  # noqa: E501
        :type: int
        """
        if organisation_id is None:
            raise ValueError("Invalid value for `organisation_id`, must not be `None`")  # noqa: E501

        self._organisation_id = organisation_id

    @property
    def identity_provider_id(self):
        """Gets the identity_provider_id of this CreateIdentityV2.  # noqa: E501


        :return: The identity_provider_id of this CreateIdentityV2.  # noqa: E501
        :rtype: int
        """
        return self._identity_provider_id

    @identity_provider_id.setter
    def identity_provider_id(self, identity_provider_id):
        """Sets the identity_provider_id of this CreateIdentityV2.


        :param identity_provider_id: The identity_provider_id of this CreateIdentityV2.  # noqa: E501
        :type: int
        """
        if identity_provider_id is None:
            raise ValueError("Invalid value for `identity_provider_id`, must not be `None`")  # noqa: E501

        self._identity_provider_id = identity_provider_id

    @property
    def owning_company_id(self):
        """Gets the owning_company_id of this CreateIdentityV2.  # noqa: E501


        :return: The owning_company_id of this CreateIdentityV2.  # noqa: E501
        :rtype: int
        """
        return self._owning_company_id

    @owning_company_id.setter
    def owning_company_id(self, owning_company_id):
        """Sets the owning_company_id of this CreateIdentityV2.


        :param owning_company_id: The owning_company_id of this CreateIdentityV2.  # noqa: E501
        :type: int
        """
        if owning_company_id is None:
            raise ValueError("Invalid value for `owning_company_id`, must not be `None`")  # noqa: E501

        self._owning_company_id = owning_company_id

    @property
    def user_and_company_links(self):
        """Gets the user_and_company_links of this CreateIdentityV2.  # noqa: E501


        :return: The user_and_company_links of this CreateIdentityV2.  # noqa: E501
        :rtype: list[CreateIdentityUserAndCompanyLink]
        """
        return self._user_and_company_links

    @user_and_company_links.setter
    def user_and_company_links(self, user_and_company_links):
        """Sets the user_and_company_links of this CreateIdentityV2.


        :param user_and_company_links: The user_and_company_links of this CreateIdentityV2.  # noqa: E501
        :type: list[CreateIdentityUserAndCompanyLink]
        """

        self._user_and_company_links = user_and_company_links

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
        if issubclass(CreateIdentityV2, dict):
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
        if not isinstance(other, CreateIdentityV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
