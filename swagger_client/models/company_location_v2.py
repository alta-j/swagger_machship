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

class CompanyLocationV2(object):
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
        'location_type': 'CompanyLocationType',
        'name': 'str',
        'abbreviation': 'str',
        'contact': 'str',
        'phone': 'str',
        'email': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'address_lines_friendly': 'str',
        'company_id': 'int',
        'location_id': 'int',
        'location': 'LocationV2',
        'special_instructions': 'str',
        'reference1': 'str',
        'reference2': 'str',
        'default_pickup_time': 'TimeSpan',
        'default_closing_time': 'TimeSpan',
        'default_pickup_instructions': 'str',
        'is_international': 'bool',
        'international_city': 'str',
        'international_postcode': 'str',
        'international_province': 'str',
        'international_country_id': 'int',
        'international_country': 'Country'
    }

    attribute_map = {
        'id': 'id',
        'location_type': 'locationType',
        'name': 'name',
        'abbreviation': 'abbreviation',
        'contact': 'contact',
        'phone': 'phone',
        'email': 'email',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'address_lines_friendly': 'addressLinesFriendly',
        'company_id': 'companyId',
        'location_id': 'locationId',
        'location': 'location',
        'special_instructions': 'specialInstructions',
        'reference1': 'reference1',
        'reference2': 'reference2',
        'default_pickup_time': 'defaultPickupTime',
        'default_closing_time': 'defaultClosingTime',
        'default_pickup_instructions': 'defaultPickupInstructions',
        'is_international': 'isInternational',
        'international_city': 'internationalCity',
        'international_postcode': 'internationalPostcode',
        'international_province': 'internationalProvince',
        'international_country_id': 'internationalCountryId',
        'international_country': 'internationalCountry'
    }

    def __init__(self, id=None, location_type=None, name=None, abbreviation=None, contact=None, phone=None, email=None, address_line1=None, address_line2=None, address_lines_friendly=None, company_id=None, location_id=None, location=None, special_instructions=None, reference1=None, reference2=None, default_pickup_time=None, default_closing_time=None, default_pickup_instructions=None, is_international=None, international_city=None, international_postcode=None, international_province=None, international_country_id=None, international_country=None):  # noqa: E501
        """CompanyLocationV2 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._location_type = None
        self._name = None
        self._abbreviation = None
        self._contact = None
        self._phone = None
        self._email = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_lines_friendly = None
        self._company_id = None
        self._location_id = None
        self._location = None
        self._special_instructions = None
        self._reference1 = None
        self._reference2 = None
        self._default_pickup_time = None
        self._default_closing_time = None
        self._default_pickup_instructions = None
        self._is_international = None
        self._international_city = None
        self._international_postcode = None
        self._international_province = None
        self._international_country_id = None
        self._international_country = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if location_type is not None:
            self.location_type = location_type
        self.name = name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if contact is not None:
            self.contact = contact
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_lines_friendly is not None:
            self.address_lines_friendly = address_lines_friendly
        if company_id is not None:
            self.company_id = company_id
        if location_id is not None:
            self.location_id = location_id
        if location is not None:
            self.location = location
        if special_instructions is not None:
            self.special_instructions = special_instructions
        if reference1 is not None:
            self.reference1 = reference1
        if reference2 is not None:
            self.reference2 = reference2
        if default_pickup_time is not None:
            self.default_pickup_time = default_pickup_time
        if default_closing_time is not None:
            self.default_closing_time = default_closing_time
        if default_pickup_instructions is not None:
            self.default_pickup_instructions = default_pickup_instructions
        if is_international is not None:
            self.is_international = is_international
        if international_city is not None:
            self.international_city = international_city
        if international_postcode is not None:
            self.international_postcode = international_postcode
        if international_province is not None:
            self.international_province = international_province
        if international_country_id is not None:
            self.international_country_id = international_country_id
        if international_country is not None:
            self.international_country = international_country

    @property
    def id(self):
        """Gets the id of this CompanyLocationV2.  # noqa: E501


        :return: The id of this CompanyLocationV2.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyLocationV2.


        :param id: The id of this CompanyLocationV2.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def location_type(self):
        """Gets the location_type of this CompanyLocationV2.  # noqa: E501


        :return: The location_type of this CompanyLocationV2.  # noqa: E501
        :rtype: CompanyLocationType
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this CompanyLocationV2.


        :param location_type: The location_type of this CompanyLocationV2.  # noqa: E501
        :type: CompanyLocationType
        """

        self._location_type = location_type

    @property
    def name(self):
        """Gets the name of this CompanyLocationV2.  # noqa: E501


        :return: The name of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompanyLocationV2.


        :param name: The name of this CompanyLocationV2.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this CompanyLocationV2.  # noqa: E501


        :return: The abbreviation of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this CompanyLocationV2.


        :param abbreviation: The abbreviation of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def contact(self):
        """Gets the contact of this CompanyLocationV2.  # noqa: E501


        :return: The contact of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this CompanyLocationV2.


        :param contact: The contact of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def phone(self):
        """Gets the phone of this CompanyLocationV2.  # noqa: E501


        :return: The phone of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CompanyLocationV2.


        :param phone: The phone of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this CompanyLocationV2.  # noqa: E501


        :return: The email of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CompanyLocationV2.


        :param email: The email of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def address_line1(self):
        """Gets the address_line1 of this CompanyLocationV2.  # noqa: E501


        :return: The address_line1 of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this CompanyLocationV2.


        :param address_line1: The address_line1 of this CompanyLocationV2.  # noqa: E501
        :type: str
        """
        if address_line1 is None:
            raise ValueError("Invalid value for `address_line1`, must not be `None`")  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this CompanyLocationV2.  # noqa: E501


        :return: The address_line2 of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this CompanyLocationV2.


        :param address_line2: The address_line2 of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def address_lines_friendly(self):
        """Gets the address_lines_friendly of this CompanyLocationV2.  # noqa: E501


        :return: The address_lines_friendly of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._address_lines_friendly

    @address_lines_friendly.setter
    def address_lines_friendly(self, address_lines_friendly):
        """Sets the address_lines_friendly of this CompanyLocationV2.


        :param address_lines_friendly: The address_lines_friendly of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._address_lines_friendly = address_lines_friendly

    @property
    def company_id(self):
        """Gets the company_id of this CompanyLocationV2.  # noqa: E501


        :return: The company_id of this CompanyLocationV2.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CompanyLocationV2.


        :param company_id: The company_id of this CompanyLocationV2.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def location_id(self):
        """Gets the location_id of this CompanyLocationV2.  # noqa: E501


        :return: The location_id of this CompanyLocationV2.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this CompanyLocationV2.


        :param location_id: The location_id of this CompanyLocationV2.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def location(self):
        """Gets the location of this CompanyLocationV2.  # noqa: E501


        :return: The location of this CompanyLocationV2.  # noqa: E501
        :rtype: LocationV2
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CompanyLocationV2.


        :param location: The location of this CompanyLocationV2.  # noqa: E501
        :type: LocationV2
        """

        self._location = location

    @property
    def special_instructions(self):
        """Gets the special_instructions of this CompanyLocationV2.  # noqa: E501


        :return: The special_instructions of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, special_instructions):
        """Sets the special_instructions of this CompanyLocationV2.


        :param special_instructions: The special_instructions of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._special_instructions = special_instructions

    @property
    def reference1(self):
        """Gets the reference1 of this CompanyLocationV2.  # noqa: E501


        :return: The reference1 of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._reference1

    @reference1.setter
    def reference1(self, reference1):
        """Sets the reference1 of this CompanyLocationV2.


        :param reference1: The reference1 of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._reference1 = reference1

    @property
    def reference2(self):
        """Gets the reference2 of this CompanyLocationV2.  # noqa: E501


        :return: The reference2 of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._reference2

    @reference2.setter
    def reference2(self, reference2):
        """Sets the reference2 of this CompanyLocationV2.


        :param reference2: The reference2 of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._reference2 = reference2

    @property
    def default_pickup_time(self):
        """Gets the default_pickup_time of this CompanyLocationV2.  # noqa: E501


        :return: The default_pickup_time of this CompanyLocationV2.  # noqa: E501
        :rtype: TimeSpan
        """
        return self._default_pickup_time

    @default_pickup_time.setter
    def default_pickup_time(self, default_pickup_time):
        """Sets the default_pickup_time of this CompanyLocationV2.


        :param default_pickup_time: The default_pickup_time of this CompanyLocationV2.  # noqa: E501
        :type: TimeSpan
        """

        self._default_pickup_time = default_pickup_time

    @property
    def default_closing_time(self):
        """Gets the default_closing_time of this CompanyLocationV2.  # noqa: E501


        :return: The default_closing_time of this CompanyLocationV2.  # noqa: E501
        :rtype: TimeSpan
        """
        return self._default_closing_time

    @default_closing_time.setter
    def default_closing_time(self, default_closing_time):
        """Sets the default_closing_time of this CompanyLocationV2.


        :param default_closing_time: The default_closing_time of this CompanyLocationV2.  # noqa: E501
        :type: TimeSpan
        """

        self._default_closing_time = default_closing_time

    @property
    def default_pickup_instructions(self):
        """Gets the default_pickup_instructions of this CompanyLocationV2.  # noqa: E501


        :return: The default_pickup_instructions of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._default_pickup_instructions

    @default_pickup_instructions.setter
    def default_pickup_instructions(self, default_pickup_instructions):
        """Sets the default_pickup_instructions of this CompanyLocationV2.


        :param default_pickup_instructions: The default_pickup_instructions of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._default_pickup_instructions = default_pickup_instructions

    @property
    def is_international(self):
        """Gets the is_international of this CompanyLocationV2.  # noqa: E501


        :return: The is_international of this CompanyLocationV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_international

    @is_international.setter
    def is_international(self, is_international):
        """Sets the is_international of this CompanyLocationV2.


        :param is_international: The is_international of this CompanyLocationV2.  # noqa: E501
        :type: bool
        """

        self._is_international = is_international

    @property
    def international_city(self):
        """Gets the international_city of this CompanyLocationV2.  # noqa: E501


        :return: The international_city of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._international_city

    @international_city.setter
    def international_city(self, international_city):
        """Sets the international_city of this CompanyLocationV2.


        :param international_city: The international_city of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._international_city = international_city

    @property
    def international_postcode(self):
        """Gets the international_postcode of this CompanyLocationV2.  # noqa: E501


        :return: The international_postcode of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._international_postcode

    @international_postcode.setter
    def international_postcode(self, international_postcode):
        """Sets the international_postcode of this CompanyLocationV2.


        :param international_postcode: The international_postcode of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._international_postcode = international_postcode

    @property
    def international_province(self):
        """Gets the international_province of this CompanyLocationV2.  # noqa: E501


        :return: The international_province of this CompanyLocationV2.  # noqa: E501
        :rtype: str
        """
        return self._international_province

    @international_province.setter
    def international_province(self, international_province):
        """Sets the international_province of this CompanyLocationV2.


        :param international_province: The international_province of this CompanyLocationV2.  # noqa: E501
        :type: str
        """

        self._international_province = international_province

    @property
    def international_country_id(self):
        """Gets the international_country_id of this CompanyLocationV2.  # noqa: E501


        :return: The international_country_id of this CompanyLocationV2.  # noqa: E501
        :rtype: int
        """
        return self._international_country_id

    @international_country_id.setter
    def international_country_id(self, international_country_id):
        """Sets the international_country_id of this CompanyLocationV2.


        :param international_country_id: The international_country_id of this CompanyLocationV2.  # noqa: E501
        :type: int
        """

        self._international_country_id = international_country_id

    @property
    def international_country(self):
        """Gets the international_country of this CompanyLocationV2.  # noqa: E501


        :return: The international_country of this CompanyLocationV2.  # noqa: E501
        :rtype: Country
        """
        return self._international_country

    @international_country.setter
    def international_country(self, international_country):
        """Sets the international_country of this CompanyLocationV2.


        :param international_country: The international_country of this CompanyLocationV2.  # noqa: E501
        :type: Country
        """

        self._international_country = international_country

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
        if issubclass(CompanyLocationV2, dict):
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
        if not isinstance(other, CompanyLocationV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
