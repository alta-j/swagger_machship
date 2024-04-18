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

class CompanyCarrierAccountSellLaneRateWithBreakSets(object):
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
        'carrier_service_id': 'int',
        'carrier_service': 'CarrierServiceLite',
        'company_carrier_account_id': 'int',
        'from_zone_id': 'int',
        'from_zone': 'CarrierZoneLite',
        'to_zone_id': 'int',
        'to_zone': 'CarrierZoneLite',
        'reciprocal': 'bool',
        'total_markup': 'float',
        'total_markup_type': 'SellRateType',
        'minimum_charge': 'float',
        'minimum_charge_type': 'SellRateType',
        'basic_charge': 'float',
        'basic_charge_type': 'SellRateType',
        'break_charge': 'float',
        'break_charge_type': 'SellRateType',
        'sell_lane_rate_breaks': 'list[CompanyCarrierAccountSellLaneRateBreak]',
        'cubic_conversion_rate': 'float',
        'total_rows': 'int',
        'grouped_break_sets': 'list[CompanyCarrierAccountSellLaneRateGroupedBreakSet]',
        'company_carrier_account': 'CompanyCarrierAccountLite',
        'carrier_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'carrier_service_id': 'carrierServiceId',
        'carrier_service': 'carrierService',
        'company_carrier_account_id': 'companyCarrierAccountId',
        'from_zone_id': 'fromZoneId',
        'from_zone': 'fromZone',
        'to_zone_id': 'toZoneId',
        'to_zone': 'toZone',
        'reciprocal': 'reciprocal',
        'total_markup': 'totalMarkup',
        'total_markup_type': 'totalMarkupType',
        'minimum_charge': 'minimumCharge',
        'minimum_charge_type': 'minimumChargeType',
        'basic_charge': 'basicCharge',
        'basic_charge_type': 'basicChargeType',
        'break_charge': 'breakCharge',
        'break_charge_type': 'breakChargeType',
        'sell_lane_rate_breaks': 'sellLaneRateBreaks',
        'cubic_conversion_rate': 'cubicConversionRate',
        'total_rows': 'totalRows',
        'grouped_break_sets': 'groupedBreakSets',
        'company_carrier_account': 'companyCarrierAccount',
        'carrier_id': 'carrierId'
    }

    def __init__(self, id=None, carrier_service_id=None, carrier_service=None, company_carrier_account_id=None, from_zone_id=None, from_zone=None, to_zone_id=None, to_zone=None, reciprocal=None, total_markup=None, total_markup_type=None, minimum_charge=None, minimum_charge_type=None, basic_charge=None, basic_charge_type=None, break_charge=None, break_charge_type=None, sell_lane_rate_breaks=None, cubic_conversion_rate=None, total_rows=None, grouped_break_sets=None, company_carrier_account=None, carrier_id=None):  # noqa: E501
        """CompanyCarrierAccountSellLaneRateWithBreakSets - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._carrier_service_id = None
        self._carrier_service = None
        self._company_carrier_account_id = None
        self._from_zone_id = None
        self._from_zone = None
        self._to_zone_id = None
        self._to_zone = None
        self._reciprocal = None
        self._total_markup = None
        self._total_markup_type = None
        self._minimum_charge = None
        self._minimum_charge_type = None
        self._basic_charge = None
        self._basic_charge_type = None
        self._break_charge = None
        self._break_charge_type = None
        self._sell_lane_rate_breaks = None
        self._cubic_conversion_rate = None
        self._total_rows = None
        self._grouped_break_sets = None
        self._company_carrier_account = None
        self._carrier_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if carrier_service_id is not None:
            self.carrier_service_id = carrier_service_id
        if carrier_service is not None:
            self.carrier_service = carrier_service
        if company_carrier_account_id is not None:
            self.company_carrier_account_id = company_carrier_account_id
        if from_zone_id is not None:
            self.from_zone_id = from_zone_id
        if from_zone is not None:
            self.from_zone = from_zone
        if to_zone_id is not None:
            self.to_zone_id = to_zone_id
        if to_zone is not None:
            self.to_zone = to_zone
        if reciprocal is not None:
            self.reciprocal = reciprocal
        if total_markup is not None:
            self.total_markup = total_markup
        if total_markup_type is not None:
            self.total_markup_type = total_markup_type
        if minimum_charge is not None:
            self.minimum_charge = minimum_charge
        if minimum_charge_type is not None:
            self.minimum_charge_type = minimum_charge_type
        if basic_charge is not None:
            self.basic_charge = basic_charge
        if basic_charge_type is not None:
            self.basic_charge_type = basic_charge_type
        if break_charge is not None:
            self.break_charge = break_charge
        if break_charge_type is not None:
            self.break_charge_type = break_charge_type
        if sell_lane_rate_breaks is not None:
            self.sell_lane_rate_breaks = sell_lane_rate_breaks
        if cubic_conversion_rate is not None:
            self.cubic_conversion_rate = cubic_conversion_rate
        if total_rows is not None:
            self.total_rows = total_rows
        if grouped_break_sets is not None:
            self.grouped_break_sets = grouped_break_sets
        if company_carrier_account is not None:
            self.company_carrier_account = company_carrier_account
        if carrier_id is not None:
            self.carrier_id = carrier_id

    @property
    def id(self):
        """Gets the id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param id: The id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def carrier_service_id(self):
        """Gets the carrier_service_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The carrier_service_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: int
        """
        return self._carrier_service_id

    @carrier_service_id.setter
    def carrier_service_id(self, carrier_service_id):
        """Sets the carrier_service_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param carrier_service_id: The carrier_service_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: int
        """

        self._carrier_service_id = carrier_service_id

    @property
    def carrier_service(self):
        """Gets the carrier_service of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The carrier_service of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: CarrierServiceLite
        """
        return self._carrier_service

    @carrier_service.setter
    def carrier_service(self, carrier_service):
        """Sets the carrier_service of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param carrier_service: The carrier_service of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: CarrierServiceLite
        """

        self._carrier_service = carrier_service

    @property
    def company_carrier_account_id(self):
        """Gets the company_carrier_account_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The company_carrier_account_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: int
        """
        return self._company_carrier_account_id

    @company_carrier_account_id.setter
    def company_carrier_account_id(self, company_carrier_account_id):
        """Sets the company_carrier_account_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param company_carrier_account_id: The company_carrier_account_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: int
        """

        self._company_carrier_account_id = company_carrier_account_id

    @property
    def from_zone_id(self):
        """Gets the from_zone_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The from_zone_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: int
        """
        return self._from_zone_id

    @from_zone_id.setter
    def from_zone_id(self, from_zone_id):
        """Sets the from_zone_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param from_zone_id: The from_zone_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: int
        """

        self._from_zone_id = from_zone_id

    @property
    def from_zone(self):
        """Gets the from_zone of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The from_zone of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: CarrierZoneLite
        """
        return self._from_zone

    @from_zone.setter
    def from_zone(self, from_zone):
        """Sets the from_zone of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param from_zone: The from_zone of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: CarrierZoneLite
        """

        self._from_zone = from_zone

    @property
    def to_zone_id(self):
        """Gets the to_zone_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The to_zone_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: int
        """
        return self._to_zone_id

    @to_zone_id.setter
    def to_zone_id(self, to_zone_id):
        """Sets the to_zone_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param to_zone_id: The to_zone_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: int
        """

        self._to_zone_id = to_zone_id

    @property
    def to_zone(self):
        """Gets the to_zone of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The to_zone of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: CarrierZoneLite
        """
        return self._to_zone

    @to_zone.setter
    def to_zone(self, to_zone):
        """Sets the to_zone of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param to_zone: The to_zone of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: CarrierZoneLite
        """

        self._to_zone = to_zone

    @property
    def reciprocal(self):
        """Gets the reciprocal of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The reciprocal of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: bool
        """
        return self._reciprocal

    @reciprocal.setter
    def reciprocal(self, reciprocal):
        """Sets the reciprocal of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param reciprocal: The reciprocal of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: bool
        """

        self._reciprocal = reciprocal

    @property
    def total_markup(self):
        """Gets the total_markup of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501

        Markup for the entire leg.  # noqa: E501

        :return: The total_markup of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: float
        """
        return self._total_markup

    @total_markup.setter
    def total_markup(self, total_markup):
        """Sets the total_markup of this CompanyCarrierAccountSellLaneRateWithBreakSets.

        Markup for the entire leg.  # noqa: E501

        :param total_markup: The total_markup of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: float
        """

        self._total_markup = total_markup

    @property
    def total_markup_type(self):
        """Gets the total_markup_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The total_markup_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: SellRateType
        """
        return self._total_markup_type

    @total_markup_type.setter
    def total_markup_type(self, total_markup_type):
        """Sets the total_markup_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param total_markup_type: The total_markup_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: SellRateType
        """

        self._total_markup_type = total_markup_type

    @property
    def minimum_charge(self):
        """Gets the minimum_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501

        Markup for the minimum  # noqa: E501

        :return: The minimum_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: float
        """
        return self._minimum_charge

    @minimum_charge.setter
    def minimum_charge(self, minimum_charge):
        """Sets the minimum_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.

        Markup for the minimum  # noqa: E501

        :param minimum_charge: The minimum_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: float
        """

        self._minimum_charge = minimum_charge

    @property
    def minimum_charge_type(self):
        """Gets the minimum_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The minimum_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: SellRateType
        """
        return self._minimum_charge_type

    @minimum_charge_type.setter
    def minimum_charge_type(self, minimum_charge_type):
        """Sets the minimum_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param minimum_charge_type: The minimum_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: SellRateType
        """

        self._minimum_charge_type = minimum_charge_type

    @property
    def basic_charge(self):
        """Gets the basic_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501

        Markup for the basic  # noqa: E501

        :return: The basic_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: float
        """
        return self._basic_charge

    @basic_charge.setter
    def basic_charge(self, basic_charge):
        """Sets the basic_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.

        Markup for the basic  # noqa: E501

        :param basic_charge: The basic_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: float
        """

        self._basic_charge = basic_charge

    @property
    def basic_charge_type(self):
        """Gets the basic_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The basic_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: SellRateType
        """
        return self._basic_charge_type

    @basic_charge_type.setter
    def basic_charge_type(self, basic_charge_type):
        """Sets the basic_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param basic_charge_type: The basic_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: SellRateType
        """

        self._basic_charge_type = basic_charge_type

    @property
    def break_charge(self):
        """Gets the break_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The break_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: float
        """
        return self._break_charge

    @break_charge.setter
    def break_charge(self, break_charge):
        """Sets the break_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param break_charge: The break_charge of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: float
        """

        self._break_charge = break_charge

    @property
    def break_charge_type(self):
        """Gets the break_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The break_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: SellRateType
        """
        return self._break_charge_type

    @break_charge_type.setter
    def break_charge_type(self, break_charge_type):
        """Sets the break_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param break_charge_type: The break_charge_type of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: SellRateType
        """

        self._break_charge_type = break_charge_type

    @property
    def sell_lane_rate_breaks(self):
        """Gets the sell_lane_rate_breaks of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The sell_lane_rate_breaks of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: list[CompanyCarrierAccountSellLaneRateBreak]
        """
        return self._sell_lane_rate_breaks

    @sell_lane_rate_breaks.setter
    def sell_lane_rate_breaks(self, sell_lane_rate_breaks):
        """Sets the sell_lane_rate_breaks of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param sell_lane_rate_breaks: The sell_lane_rate_breaks of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: list[CompanyCarrierAccountSellLaneRateBreak]
        """

        self._sell_lane_rate_breaks = sell_lane_rate_breaks

    @property
    def cubic_conversion_rate(self):
        """Gets the cubic_conversion_rate of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The cubic_conversion_rate of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: float
        """
        return self._cubic_conversion_rate

    @cubic_conversion_rate.setter
    def cubic_conversion_rate(self, cubic_conversion_rate):
        """Sets the cubic_conversion_rate of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param cubic_conversion_rate: The cubic_conversion_rate of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: float
        """

        self._cubic_conversion_rate = cubic_conversion_rate

    @property
    def total_rows(self):
        """Gets the total_rows of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The total_rows of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param total_rows: The total_rows of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: int
        """

        self._total_rows = total_rows

    @property
    def grouped_break_sets(self):
        """Gets the grouped_break_sets of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The grouped_break_sets of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: list[CompanyCarrierAccountSellLaneRateGroupedBreakSet]
        """
        return self._grouped_break_sets

    @grouped_break_sets.setter
    def grouped_break_sets(self, grouped_break_sets):
        """Sets the grouped_break_sets of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param grouped_break_sets: The grouped_break_sets of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: list[CompanyCarrierAccountSellLaneRateGroupedBreakSet]
        """

        self._grouped_break_sets = grouped_break_sets

    @property
    def company_carrier_account(self):
        """Gets the company_carrier_account of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The company_carrier_account of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: CompanyCarrierAccountLite
        """
        return self._company_carrier_account

    @company_carrier_account.setter
    def company_carrier_account(self, company_carrier_account):
        """Sets the company_carrier_account of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param company_carrier_account: The company_carrier_account of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: CompanyCarrierAccountLite
        """

        self._company_carrier_account = company_carrier_account

    @property
    def carrier_id(self):
        """Gets the carrier_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501


        :return: The carrier_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :rtype: int
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.


        :param carrier_id: The carrier_id of this CompanyCarrierAccountSellLaneRateWithBreakSets.  # noqa: E501
        :type: int
        """

        self._carrier_id = carrier_id

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
        if issubclass(CompanyCarrierAccountSellLaneRateWithBreakSets, dict):
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
        if not isinstance(other, CompanyCarrierAccountSellLaneRateWithBreakSets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
