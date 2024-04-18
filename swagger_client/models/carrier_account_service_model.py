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

class CarrierAccountServiceModel(object):
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
        'carrier_account': 'CarrierAccountLite',
        'carrier_account_id': 'int',
        'carrier_service': 'CarrierServiceLite',
        'carrier_service_id': 'int',
        'new_fuel_levy_markup_percentage': 'float',
        'fuel_surcharge_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'carrier_account': 'carrierAccount',
        'carrier_account_id': 'carrierAccountId',
        'carrier_service': 'carrierService',
        'carrier_service_id': 'carrierServiceId',
        'new_fuel_levy_markup_percentage': 'newFuelLevyMarkupPercentage',
        'fuel_surcharge_id': 'fuelSurchargeId'
    }

    def __init__(self, id=None, carrier_account=None, carrier_account_id=None, carrier_service=None, carrier_service_id=None, new_fuel_levy_markup_percentage=None, fuel_surcharge_id=None):  # noqa: E501
        """CarrierAccountServiceModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._carrier_account = None
        self._carrier_account_id = None
        self._carrier_service = None
        self._carrier_service_id = None
        self._new_fuel_levy_markup_percentage = None
        self._fuel_surcharge_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if carrier_account is not None:
            self.carrier_account = carrier_account
        if carrier_account_id is not None:
            self.carrier_account_id = carrier_account_id
        if carrier_service is not None:
            self.carrier_service = carrier_service
        if carrier_service_id is not None:
            self.carrier_service_id = carrier_service_id
        if new_fuel_levy_markup_percentage is not None:
            self.new_fuel_levy_markup_percentage = new_fuel_levy_markup_percentage
        if fuel_surcharge_id is not None:
            self.fuel_surcharge_id = fuel_surcharge_id

    @property
    def id(self):
        """Gets the id of this CarrierAccountServiceModel.  # noqa: E501


        :return: The id of this CarrierAccountServiceModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CarrierAccountServiceModel.


        :param id: The id of this CarrierAccountServiceModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def carrier_account(self):
        """Gets the carrier_account of this CarrierAccountServiceModel.  # noqa: E501


        :return: The carrier_account of this CarrierAccountServiceModel.  # noqa: E501
        :rtype: CarrierAccountLite
        """
        return self._carrier_account

    @carrier_account.setter
    def carrier_account(self, carrier_account):
        """Sets the carrier_account of this CarrierAccountServiceModel.


        :param carrier_account: The carrier_account of this CarrierAccountServiceModel.  # noqa: E501
        :type: CarrierAccountLite
        """

        self._carrier_account = carrier_account

    @property
    def carrier_account_id(self):
        """Gets the carrier_account_id of this CarrierAccountServiceModel.  # noqa: E501


        :return: The carrier_account_id of this CarrierAccountServiceModel.  # noqa: E501
        :rtype: int
        """
        return self._carrier_account_id

    @carrier_account_id.setter
    def carrier_account_id(self, carrier_account_id):
        """Sets the carrier_account_id of this CarrierAccountServiceModel.


        :param carrier_account_id: The carrier_account_id of this CarrierAccountServiceModel.  # noqa: E501
        :type: int
        """

        self._carrier_account_id = carrier_account_id

    @property
    def carrier_service(self):
        """Gets the carrier_service of this CarrierAccountServiceModel.  # noqa: E501


        :return: The carrier_service of this CarrierAccountServiceModel.  # noqa: E501
        :rtype: CarrierServiceLite
        """
        return self._carrier_service

    @carrier_service.setter
    def carrier_service(self, carrier_service):
        """Sets the carrier_service of this CarrierAccountServiceModel.


        :param carrier_service: The carrier_service of this CarrierAccountServiceModel.  # noqa: E501
        :type: CarrierServiceLite
        """

        self._carrier_service = carrier_service

    @property
    def carrier_service_id(self):
        """Gets the carrier_service_id of this CarrierAccountServiceModel.  # noqa: E501


        :return: The carrier_service_id of this CarrierAccountServiceModel.  # noqa: E501
        :rtype: int
        """
        return self._carrier_service_id

    @carrier_service_id.setter
    def carrier_service_id(self, carrier_service_id):
        """Sets the carrier_service_id of this CarrierAccountServiceModel.


        :param carrier_service_id: The carrier_service_id of this CarrierAccountServiceModel.  # noqa: E501
        :type: int
        """

        self._carrier_service_id = carrier_service_id

    @property
    def new_fuel_levy_markup_percentage(self):
        """Gets the new_fuel_levy_markup_percentage of this CarrierAccountServiceModel.  # noqa: E501


        :return: The new_fuel_levy_markup_percentage of this CarrierAccountServiceModel.  # noqa: E501
        :rtype: float
        """
        return self._new_fuel_levy_markup_percentage

    @new_fuel_levy_markup_percentage.setter
    def new_fuel_levy_markup_percentage(self, new_fuel_levy_markup_percentage):
        """Sets the new_fuel_levy_markup_percentage of this CarrierAccountServiceModel.


        :param new_fuel_levy_markup_percentage: The new_fuel_levy_markup_percentage of this CarrierAccountServiceModel.  # noqa: E501
        :type: float
        """

        self._new_fuel_levy_markup_percentage = new_fuel_levy_markup_percentage

    @property
    def fuel_surcharge_id(self):
        """Gets the fuel_surcharge_id of this CarrierAccountServiceModel.  # noqa: E501


        :return: The fuel_surcharge_id of this CarrierAccountServiceModel.  # noqa: E501
        :rtype: int
        """
        return self._fuel_surcharge_id

    @fuel_surcharge_id.setter
    def fuel_surcharge_id(self, fuel_surcharge_id):
        """Sets the fuel_surcharge_id of this CarrierAccountServiceModel.


        :param fuel_surcharge_id: The fuel_surcharge_id of this CarrierAccountServiceModel.  # noqa: E501
        :type: int
        """

        self._fuel_surcharge_id = fuel_surcharge_id

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
        if issubclass(CarrierAccountServiceModel, dict):
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
        if not isinstance(other, CarrierAccountServiceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
