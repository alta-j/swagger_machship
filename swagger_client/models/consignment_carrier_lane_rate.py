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

class ConsignmentCarrierLaneRate(object):
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
        'consignment': 'Consignment',
        'consignment_id': 'int',
        'carrier_lane_rate': 'CarrierLaneRate',
        'carrier_lane_rate_id': 'int',
        'cost_price': 'float',
        'sell_price': 'float',
        'cubic_conversion_rate': 'float',
        'total_cubic_weight': 'float',
        'sell_carrier_lane_rate_id': 'int',
        'distance': 'float',
        'time': 'float',
        'sell_cubic_conversion_rate': 'float',
        'total_sell_cubic_weight': 'float'
    }

    attribute_map = {
        'id': 'id',
        'consignment': 'consignment',
        'consignment_id': 'consignmentId',
        'carrier_lane_rate': 'carrierLaneRate',
        'carrier_lane_rate_id': 'carrierLaneRateId',
        'cost_price': 'costPrice',
        'sell_price': 'sellPrice',
        'cubic_conversion_rate': 'cubicConversionRate',
        'total_cubic_weight': 'totalCubicWeight',
        'sell_carrier_lane_rate_id': 'sellCarrierLaneRateId',
        'distance': 'distance',
        'time': 'time',
        'sell_cubic_conversion_rate': 'sellCubicConversionRate',
        'total_sell_cubic_weight': 'totalSellCubicWeight'
    }

    def __init__(self, id=None, consignment=None, consignment_id=None, carrier_lane_rate=None, carrier_lane_rate_id=None, cost_price=None, sell_price=None, cubic_conversion_rate=None, total_cubic_weight=None, sell_carrier_lane_rate_id=None, distance=None, time=None, sell_cubic_conversion_rate=None, total_sell_cubic_weight=None):  # noqa: E501
        """ConsignmentCarrierLaneRate - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._consignment = None
        self._consignment_id = None
        self._carrier_lane_rate = None
        self._carrier_lane_rate_id = None
        self._cost_price = None
        self._sell_price = None
        self._cubic_conversion_rate = None
        self._total_cubic_weight = None
        self._sell_carrier_lane_rate_id = None
        self._distance = None
        self._time = None
        self._sell_cubic_conversion_rate = None
        self._total_sell_cubic_weight = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if consignment is not None:
            self.consignment = consignment
        if consignment_id is not None:
            self.consignment_id = consignment_id
        if carrier_lane_rate is not None:
            self.carrier_lane_rate = carrier_lane_rate
        if carrier_lane_rate_id is not None:
            self.carrier_lane_rate_id = carrier_lane_rate_id
        if cost_price is not None:
            self.cost_price = cost_price
        if sell_price is not None:
            self.sell_price = sell_price
        if cubic_conversion_rate is not None:
            self.cubic_conversion_rate = cubic_conversion_rate
        if total_cubic_weight is not None:
            self.total_cubic_weight = total_cubic_weight
        if sell_carrier_lane_rate_id is not None:
            self.sell_carrier_lane_rate_id = sell_carrier_lane_rate_id
        if distance is not None:
            self.distance = distance
        if time is not None:
            self.time = time
        if sell_cubic_conversion_rate is not None:
            self.sell_cubic_conversion_rate = sell_cubic_conversion_rate
        if total_sell_cubic_weight is not None:
            self.total_sell_cubic_weight = total_sell_cubic_weight

    @property
    def id(self):
        """Gets the id of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The id of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConsignmentCarrierLaneRate.


        :param id: The id of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def consignment(self):
        """Gets the consignment of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The consignment of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: Consignment
        """
        return self._consignment

    @consignment.setter
    def consignment(self, consignment):
        """Sets the consignment of this ConsignmentCarrierLaneRate.


        :param consignment: The consignment of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: Consignment
        """

        self._consignment = consignment

    @property
    def consignment_id(self):
        """Gets the consignment_id of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The consignment_id of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: int
        """
        return self._consignment_id

    @consignment_id.setter
    def consignment_id(self, consignment_id):
        """Sets the consignment_id of this ConsignmentCarrierLaneRate.


        :param consignment_id: The consignment_id of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: int
        """

        self._consignment_id = consignment_id

    @property
    def carrier_lane_rate(self):
        """Gets the carrier_lane_rate of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The carrier_lane_rate of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: CarrierLaneRate
        """
        return self._carrier_lane_rate

    @carrier_lane_rate.setter
    def carrier_lane_rate(self, carrier_lane_rate):
        """Sets the carrier_lane_rate of this ConsignmentCarrierLaneRate.


        :param carrier_lane_rate: The carrier_lane_rate of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: CarrierLaneRate
        """

        self._carrier_lane_rate = carrier_lane_rate

    @property
    def carrier_lane_rate_id(self):
        """Gets the carrier_lane_rate_id of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The carrier_lane_rate_id of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: int
        """
        return self._carrier_lane_rate_id

    @carrier_lane_rate_id.setter
    def carrier_lane_rate_id(self, carrier_lane_rate_id):
        """Sets the carrier_lane_rate_id of this ConsignmentCarrierLaneRate.


        :param carrier_lane_rate_id: The carrier_lane_rate_id of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: int
        """

        self._carrier_lane_rate_id = carrier_lane_rate_id

    @property
    def cost_price(self):
        """Gets the cost_price of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The cost_price of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: float
        """
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        """Sets the cost_price of this ConsignmentCarrierLaneRate.


        :param cost_price: The cost_price of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: float
        """

        self._cost_price = cost_price

    @property
    def sell_price(self):
        """Gets the sell_price of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The sell_price of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: float
        """
        return self._sell_price

    @sell_price.setter
    def sell_price(self, sell_price):
        """Sets the sell_price of this ConsignmentCarrierLaneRate.


        :param sell_price: The sell_price of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: float
        """

        self._sell_price = sell_price

    @property
    def cubic_conversion_rate(self):
        """Gets the cubic_conversion_rate of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The cubic_conversion_rate of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: float
        """
        return self._cubic_conversion_rate

    @cubic_conversion_rate.setter
    def cubic_conversion_rate(self, cubic_conversion_rate):
        """Sets the cubic_conversion_rate of this ConsignmentCarrierLaneRate.


        :param cubic_conversion_rate: The cubic_conversion_rate of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: float
        """

        self._cubic_conversion_rate = cubic_conversion_rate

    @property
    def total_cubic_weight(self):
        """Gets the total_cubic_weight of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The total_cubic_weight of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: float
        """
        return self._total_cubic_weight

    @total_cubic_weight.setter
    def total_cubic_weight(self, total_cubic_weight):
        """Sets the total_cubic_weight of this ConsignmentCarrierLaneRate.


        :param total_cubic_weight: The total_cubic_weight of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: float
        """

        self._total_cubic_weight = total_cubic_weight

    @property
    def sell_carrier_lane_rate_id(self):
        """Gets the sell_carrier_lane_rate_id of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The sell_carrier_lane_rate_id of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: int
        """
        return self._sell_carrier_lane_rate_id

    @sell_carrier_lane_rate_id.setter
    def sell_carrier_lane_rate_id(self, sell_carrier_lane_rate_id):
        """Sets the sell_carrier_lane_rate_id of this ConsignmentCarrierLaneRate.


        :param sell_carrier_lane_rate_id: The sell_carrier_lane_rate_id of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: int
        """

        self._sell_carrier_lane_rate_id = sell_carrier_lane_rate_id

    @property
    def distance(self):
        """Gets the distance of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The distance of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this ConsignmentCarrierLaneRate.


        :param distance: The distance of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def time(self):
        """Gets the time of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The time of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ConsignmentCarrierLaneRate.


        :param time: The time of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: float
        """

        self._time = time

    @property
    def sell_cubic_conversion_rate(self):
        """Gets the sell_cubic_conversion_rate of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The sell_cubic_conversion_rate of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: float
        """
        return self._sell_cubic_conversion_rate

    @sell_cubic_conversion_rate.setter
    def sell_cubic_conversion_rate(self, sell_cubic_conversion_rate):
        """Sets the sell_cubic_conversion_rate of this ConsignmentCarrierLaneRate.


        :param sell_cubic_conversion_rate: The sell_cubic_conversion_rate of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: float
        """

        self._sell_cubic_conversion_rate = sell_cubic_conversion_rate

    @property
    def total_sell_cubic_weight(self):
        """Gets the total_sell_cubic_weight of this ConsignmentCarrierLaneRate.  # noqa: E501


        :return: The total_sell_cubic_weight of this ConsignmentCarrierLaneRate.  # noqa: E501
        :rtype: float
        """
        return self._total_sell_cubic_weight

    @total_sell_cubic_weight.setter
    def total_sell_cubic_weight(self, total_sell_cubic_weight):
        """Sets the total_sell_cubic_weight of this ConsignmentCarrierLaneRate.


        :param total_sell_cubic_weight: The total_sell_cubic_weight of this ConsignmentCarrierLaneRate.  # noqa: E501
        :type: float
        """

        self._total_sell_cubic_weight = total_sell_cubic_weight

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
        if issubclass(ConsignmentCarrierLaneRate, dict):
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
        if not isinstance(other, ConsignmentCarrierLaneRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other