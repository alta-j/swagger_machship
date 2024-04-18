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

class QuoteForList(object):
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
        'consignment_number': 'str',
        'carrier_and_service_name': 'str',
        'customer_reference': 'str',
        'item_count': 'int',
        'from_name': 'str',
        'from_location': 'Location',
        'from_name_and_location': 'str',
        'to_name': 'str',
        'to_location': 'Location',
        'to_name_and_location': 'str',
        'expiry_date': 'datetime',
        'created_date': 'datetime',
        'is_hourly': 'bool',
        'total': 'float',
        'total_display': 'str',
        'is_dg_consignment': 'bool',
        'total_rows': 'int',
        'is_international': 'bool',
        'international_from_city': 'str',
        'international_from_postcode': 'str',
        'international_from_province': 'str',
        'from_country_id': 'int',
        'from_country': 'Country',
        'international_to_city': 'str',
        'international_to_postcode': 'str',
        'international_to_province': 'str',
        'to_country_id': 'int',
        'to_country': 'Country'
    }

    attribute_map = {
        'id': 'id',
        'consignment_number': 'consignmentNumber',
        'carrier_and_service_name': 'carrierAndServiceName',
        'customer_reference': 'customerReference',
        'item_count': 'itemCount',
        'from_name': 'fromName',
        'from_location': 'fromLocation',
        'from_name_and_location': 'fromNameAndLocation',
        'to_name': 'toName',
        'to_location': 'toLocation',
        'to_name_and_location': 'toNameAndLocation',
        'expiry_date': 'expiryDate',
        'created_date': 'createdDate',
        'is_hourly': 'isHourly',
        'total': 'total',
        'total_display': 'totalDisplay',
        'is_dg_consignment': 'isDgConsignment',
        'total_rows': 'totalRows',
        'is_international': 'isInternational',
        'international_from_city': 'internationalFromCity',
        'international_from_postcode': 'internationalFromPostcode',
        'international_from_province': 'internationalFromProvince',
        'from_country_id': 'fromCountryId',
        'from_country': 'fromCountry',
        'international_to_city': 'internationalToCity',
        'international_to_postcode': 'internationalToPostcode',
        'international_to_province': 'internationalToProvince',
        'to_country_id': 'toCountryId',
        'to_country': 'toCountry'
    }

    def __init__(self, id=None, consignment_number=None, carrier_and_service_name=None, customer_reference=None, item_count=None, from_name=None, from_location=None, from_name_and_location=None, to_name=None, to_location=None, to_name_and_location=None, expiry_date=None, created_date=None, is_hourly=None, total=None, total_display=None, is_dg_consignment=None, total_rows=None, is_international=None, international_from_city=None, international_from_postcode=None, international_from_province=None, from_country_id=None, from_country=None, international_to_city=None, international_to_postcode=None, international_to_province=None, to_country_id=None, to_country=None):  # noqa: E501
        """QuoteForList - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._consignment_number = None
        self._carrier_and_service_name = None
        self._customer_reference = None
        self._item_count = None
        self._from_name = None
        self._from_location = None
        self._from_name_and_location = None
        self._to_name = None
        self._to_location = None
        self._to_name_and_location = None
        self._expiry_date = None
        self._created_date = None
        self._is_hourly = None
        self._total = None
        self._total_display = None
        self._is_dg_consignment = None
        self._total_rows = None
        self._is_international = None
        self._international_from_city = None
        self._international_from_postcode = None
        self._international_from_province = None
        self._from_country_id = None
        self._from_country = None
        self._international_to_city = None
        self._international_to_postcode = None
        self._international_to_province = None
        self._to_country_id = None
        self._to_country = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if consignment_number is not None:
            self.consignment_number = consignment_number
        if carrier_and_service_name is not None:
            self.carrier_and_service_name = carrier_and_service_name
        if customer_reference is not None:
            self.customer_reference = customer_reference
        if item_count is not None:
            self.item_count = item_count
        if from_name is not None:
            self.from_name = from_name
        if from_location is not None:
            self.from_location = from_location
        if from_name_and_location is not None:
            self.from_name_and_location = from_name_and_location
        if to_name is not None:
            self.to_name = to_name
        if to_location is not None:
            self.to_location = to_location
        if to_name_and_location is not None:
            self.to_name_and_location = to_name_and_location
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if created_date is not None:
            self.created_date = created_date
        if is_hourly is not None:
            self.is_hourly = is_hourly
        if total is not None:
            self.total = total
        if total_display is not None:
            self.total_display = total_display
        if is_dg_consignment is not None:
            self.is_dg_consignment = is_dg_consignment
        if total_rows is not None:
            self.total_rows = total_rows
        if is_international is not None:
            self.is_international = is_international
        if international_from_city is not None:
            self.international_from_city = international_from_city
        if international_from_postcode is not None:
            self.international_from_postcode = international_from_postcode
        if international_from_province is not None:
            self.international_from_province = international_from_province
        if from_country_id is not None:
            self.from_country_id = from_country_id
        if from_country is not None:
            self.from_country = from_country
        if international_to_city is not None:
            self.international_to_city = international_to_city
        if international_to_postcode is not None:
            self.international_to_postcode = international_to_postcode
        if international_to_province is not None:
            self.international_to_province = international_to_province
        if to_country_id is not None:
            self.to_country_id = to_country_id
        if to_country is not None:
            self.to_country = to_country

    @property
    def id(self):
        """Gets the id of this QuoteForList.  # noqa: E501


        :return: The id of this QuoteForList.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuoteForList.


        :param id: The id of this QuoteForList.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def consignment_number(self):
        """Gets the consignment_number of this QuoteForList.  # noqa: E501


        :return: The consignment_number of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._consignment_number

    @consignment_number.setter
    def consignment_number(self, consignment_number):
        """Sets the consignment_number of this QuoteForList.


        :param consignment_number: The consignment_number of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._consignment_number = consignment_number

    @property
    def carrier_and_service_name(self):
        """Gets the carrier_and_service_name of this QuoteForList.  # noqa: E501


        :return: The carrier_and_service_name of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._carrier_and_service_name

    @carrier_and_service_name.setter
    def carrier_and_service_name(self, carrier_and_service_name):
        """Sets the carrier_and_service_name of this QuoteForList.


        :param carrier_and_service_name: The carrier_and_service_name of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._carrier_and_service_name = carrier_and_service_name

    @property
    def customer_reference(self):
        """Gets the customer_reference of this QuoteForList.  # noqa: E501


        :return: The customer_reference of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._customer_reference

    @customer_reference.setter
    def customer_reference(self, customer_reference):
        """Sets the customer_reference of this QuoteForList.


        :param customer_reference: The customer_reference of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._customer_reference = customer_reference

    @property
    def item_count(self):
        """Gets the item_count of this QuoteForList.  # noqa: E501


        :return: The item_count of this QuoteForList.  # noqa: E501
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this QuoteForList.


        :param item_count: The item_count of this QuoteForList.  # noqa: E501
        :type: int
        """

        self._item_count = item_count

    @property
    def from_name(self):
        """Gets the from_name of this QuoteForList.  # noqa: E501


        :return: The from_name of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this QuoteForList.


        :param from_name: The from_name of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def from_location(self):
        """Gets the from_location of this QuoteForList.  # noqa: E501


        :return: The from_location of this QuoteForList.  # noqa: E501
        :rtype: Location
        """
        return self._from_location

    @from_location.setter
    def from_location(self, from_location):
        """Sets the from_location of this QuoteForList.


        :param from_location: The from_location of this QuoteForList.  # noqa: E501
        :type: Location
        """

        self._from_location = from_location

    @property
    def from_name_and_location(self):
        """Gets the from_name_and_location of this QuoteForList.  # noqa: E501


        :return: The from_name_and_location of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._from_name_and_location

    @from_name_and_location.setter
    def from_name_and_location(self, from_name_and_location):
        """Sets the from_name_and_location of this QuoteForList.


        :param from_name_and_location: The from_name_and_location of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._from_name_and_location = from_name_and_location

    @property
    def to_name(self):
        """Gets the to_name of this QuoteForList.  # noqa: E501


        :return: The to_name of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name):
        """Sets the to_name of this QuoteForList.


        :param to_name: The to_name of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._to_name = to_name

    @property
    def to_location(self):
        """Gets the to_location of this QuoteForList.  # noqa: E501


        :return: The to_location of this QuoteForList.  # noqa: E501
        :rtype: Location
        """
        return self._to_location

    @to_location.setter
    def to_location(self, to_location):
        """Sets the to_location of this QuoteForList.


        :param to_location: The to_location of this QuoteForList.  # noqa: E501
        :type: Location
        """

        self._to_location = to_location

    @property
    def to_name_and_location(self):
        """Gets the to_name_and_location of this QuoteForList.  # noqa: E501


        :return: The to_name_and_location of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._to_name_and_location

    @to_name_and_location.setter
    def to_name_and_location(self, to_name_and_location):
        """Sets the to_name_and_location of this QuoteForList.


        :param to_name_and_location: The to_name_and_location of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._to_name_and_location = to_name_and_location

    @property
    def expiry_date(self):
        """Gets the expiry_date of this QuoteForList.  # noqa: E501


        :return: The expiry_date of this QuoteForList.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this QuoteForList.


        :param expiry_date: The expiry_date of this QuoteForList.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def created_date(self):
        """Gets the created_date of this QuoteForList.  # noqa: E501


        :return: The created_date of this QuoteForList.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this QuoteForList.


        :param created_date: The created_date of this QuoteForList.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def is_hourly(self):
        """Gets the is_hourly of this QuoteForList.  # noqa: E501


        :return: The is_hourly of this QuoteForList.  # noqa: E501
        :rtype: bool
        """
        return self._is_hourly

    @is_hourly.setter
    def is_hourly(self, is_hourly):
        """Sets the is_hourly of this QuoteForList.


        :param is_hourly: The is_hourly of this QuoteForList.  # noqa: E501
        :type: bool
        """

        self._is_hourly = is_hourly

    @property
    def total(self):
        """Gets the total of this QuoteForList.  # noqa: E501


        :return: The total of this QuoteForList.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this QuoteForList.


        :param total: The total of this QuoteForList.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def total_display(self):
        """Gets the total_display of this QuoteForList.  # noqa: E501


        :return: The total_display of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._total_display

    @total_display.setter
    def total_display(self, total_display):
        """Sets the total_display of this QuoteForList.


        :param total_display: The total_display of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._total_display = total_display

    @property
    def is_dg_consignment(self):
        """Gets the is_dg_consignment of this QuoteForList.  # noqa: E501


        :return: The is_dg_consignment of this QuoteForList.  # noqa: E501
        :rtype: bool
        """
        return self._is_dg_consignment

    @is_dg_consignment.setter
    def is_dg_consignment(self, is_dg_consignment):
        """Sets the is_dg_consignment of this QuoteForList.


        :param is_dg_consignment: The is_dg_consignment of this QuoteForList.  # noqa: E501
        :type: bool
        """

        self._is_dg_consignment = is_dg_consignment

    @property
    def total_rows(self):
        """Gets the total_rows of this QuoteForList.  # noqa: E501


        :return: The total_rows of this QuoteForList.  # noqa: E501
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this QuoteForList.


        :param total_rows: The total_rows of this QuoteForList.  # noqa: E501
        :type: int
        """

        self._total_rows = total_rows

    @property
    def is_international(self):
        """Gets the is_international of this QuoteForList.  # noqa: E501


        :return: The is_international of this QuoteForList.  # noqa: E501
        :rtype: bool
        """
        return self._is_international

    @is_international.setter
    def is_international(self, is_international):
        """Sets the is_international of this QuoteForList.


        :param is_international: The is_international of this QuoteForList.  # noqa: E501
        :type: bool
        """

        self._is_international = is_international

    @property
    def international_from_city(self):
        """Gets the international_from_city of this QuoteForList.  # noqa: E501


        :return: The international_from_city of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._international_from_city

    @international_from_city.setter
    def international_from_city(self, international_from_city):
        """Sets the international_from_city of this QuoteForList.


        :param international_from_city: The international_from_city of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._international_from_city = international_from_city

    @property
    def international_from_postcode(self):
        """Gets the international_from_postcode of this QuoteForList.  # noqa: E501


        :return: The international_from_postcode of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._international_from_postcode

    @international_from_postcode.setter
    def international_from_postcode(self, international_from_postcode):
        """Sets the international_from_postcode of this QuoteForList.


        :param international_from_postcode: The international_from_postcode of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._international_from_postcode = international_from_postcode

    @property
    def international_from_province(self):
        """Gets the international_from_province of this QuoteForList.  # noqa: E501


        :return: The international_from_province of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._international_from_province

    @international_from_province.setter
    def international_from_province(self, international_from_province):
        """Sets the international_from_province of this QuoteForList.


        :param international_from_province: The international_from_province of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._international_from_province = international_from_province

    @property
    def from_country_id(self):
        """Gets the from_country_id of this QuoteForList.  # noqa: E501


        :return: The from_country_id of this QuoteForList.  # noqa: E501
        :rtype: int
        """
        return self._from_country_id

    @from_country_id.setter
    def from_country_id(self, from_country_id):
        """Sets the from_country_id of this QuoteForList.


        :param from_country_id: The from_country_id of this QuoteForList.  # noqa: E501
        :type: int
        """

        self._from_country_id = from_country_id

    @property
    def from_country(self):
        """Gets the from_country of this QuoteForList.  # noqa: E501


        :return: The from_country of this QuoteForList.  # noqa: E501
        :rtype: Country
        """
        return self._from_country

    @from_country.setter
    def from_country(self, from_country):
        """Sets the from_country of this QuoteForList.


        :param from_country: The from_country of this QuoteForList.  # noqa: E501
        :type: Country
        """

        self._from_country = from_country

    @property
    def international_to_city(self):
        """Gets the international_to_city of this QuoteForList.  # noqa: E501


        :return: The international_to_city of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._international_to_city

    @international_to_city.setter
    def international_to_city(self, international_to_city):
        """Sets the international_to_city of this QuoteForList.


        :param international_to_city: The international_to_city of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._international_to_city = international_to_city

    @property
    def international_to_postcode(self):
        """Gets the international_to_postcode of this QuoteForList.  # noqa: E501


        :return: The international_to_postcode of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._international_to_postcode

    @international_to_postcode.setter
    def international_to_postcode(self, international_to_postcode):
        """Sets the international_to_postcode of this QuoteForList.


        :param international_to_postcode: The international_to_postcode of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._international_to_postcode = international_to_postcode

    @property
    def international_to_province(self):
        """Gets the international_to_province of this QuoteForList.  # noqa: E501


        :return: The international_to_province of this QuoteForList.  # noqa: E501
        :rtype: str
        """
        return self._international_to_province

    @international_to_province.setter
    def international_to_province(self, international_to_province):
        """Sets the international_to_province of this QuoteForList.


        :param international_to_province: The international_to_province of this QuoteForList.  # noqa: E501
        :type: str
        """

        self._international_to_province = international_to_province

    @property
    def to_country_id(self):
        """Gets the to_country_id of this QuoteForList.  # noqa: E501


        :return: The to_country_id of this QuoteForList.  # noqa: E501
        :rtype: int
        """
        return self._to_country_id

    @to_country_id.setter
    def to_country_id(self, to_country_id):
        """Sets the to_country_id of this QuoteForList.


        :param to_country_id: The to_country_id of this QuoteForList.  # noqa: E501
        :type: int
        """

        self._to_country_id = to_country_id

    @property
    def to_country(self):
        """Gets the to_country of this QuoteForList.  # noqa: E501


        :return: The to_country of this QuoteForList.  # noqa: E501
        :rtype: Country
        """
        return self._to_country

    @to_country.setter
    def to_country(self, to_country):
        """Sets the to_country of this QuoteForList.


        :param to_country: The to_country of this QuoteForList.  # noqa: E501
        :type: Country
        """

        self._to_country = to_country

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
        if issubclass(QuoteForList, dict):
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
        if not isinstance(other, QuoteForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
