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

class MachshipCarrierIntegration(object):
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
        'is_generic': 'bool',
        'is_carrier_default': 'bool',
        'has_consignment_ref_pool': 'bool',
        'has_item_ref_pool': 'bool',
        'has_manifest_ref_pool': 'bool',
        'show_pickup_fields_when_manifesting': 'bool',
        'is_international': 'bool',
        'supports_sending_commercial_invoice': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_generic': 'isGeneric',
        'is_carrier_default': 'isCarrierDefault',
        'has_consignment_ref_pool': 'hasConsignmentRefPool',
        'has_item_ref_pool': 'hasItemRefPool',
        'has_manifest_ref_pool': 'hasManifestRefPool',
        'show_pickup_fields_when_manifesting': 'showPickupFieldsWhenManifesting',
        'is_international': 'isInternational',
        'supports_sending_commercial_invoice': 'supportsSendingCommercialInvoice'
    }

    def __init__(self, id=None, name=None, is_generic=None, is_carrier_default=None, has_consignment_ref_pool=None, has_item_ref_pool=None, has_manifest_ref_pool=None, show_pickup_fields_when_manifesting=None, is_international=None, supports_sending_commercial_invoice=None):  # noqa: E501
        """MachshipCarrierIntegration - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._is_generic = None
        self._is_carrier_default = None
        self._has_consignment_ref_pool = None
        self._has_item_ref_pool = None
        self._has_manifest_ref_pool = None
        self._show_pickup_fields_when_manifesting = None
        self._is_international = None
        self._supports_sending_commercial_invoice = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if is_generic is not None:
            self.is_generic = is_generic
        if is_carrier_default is not None:
            self.is_carrier_default = is_carrier_default
        if has_consignment_ref_pool is not None:
            self.has_consignment_ref_pool = has_consignment_ref_pool
        if has_item_ref_pool is not None:
            self.has_item_ref_pool = has_item_ref_pool
        if has_manifest_ref_pool is not None:
            self.has_manifest_ref_pool = has_manifest_ref_pool
        if show_pickup_fields_when_manifesting is not None:
            self.show_pickup_fields_when_manifesting = show_pickup_fields_when_manifesting
        if is_international is not None:
            self.is_international = is_international
        if supports_sending_commercial_invoice is not None:
            self.supports_sending_commercial_invoice = supports_sending_commercial_invoice

    @property
    def id(self):
        """Gets the id of this MachshipCarrierIntegration.  # noqa: E501


        :return: The id of this MachshipCarrierIntegration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MachshipCarrierIntegration.


        :param id: The id of this MachshipCarrierIntegration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MachshipCarrierIntegration.  # noqa: E501


        :return: The name of this MachshipCarrierIntegration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MachshipCarrierIntegration.


        :param name: The name of this MachshipCarrierIntegration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_generic(self):
        """Gets the is_generic of this MachshipCarrierIntegration.  # noqa: E501

        When true this means that this is they type of integration that is available for accounts of any carrier  # noqa: E501

        :return: The is_generic of this MachshipCarrierIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._is_generic

    @is_generic.setter
    def is_generic(self, is_generic):
        """Sets the is_generic of this MachshipCarrierIntegration.

        When true this means that this is they type of integration that is available for accounts of any carrier  # noqa: E501

        :param is_generic: The is_generic of this MachshipCarrierIntegration.  # noqa: E501
        :type: bool
        """

        self._is_generic = is_generic

    @property
    def is_carrier_default(self):
        """Gets the is_carrier_default of this MachshipCarrierIntegration.  # noqa: E501

        Whether or not the carrier specifies this integration as its default type  # noqa: E501

        :return: The is_carrier_default of this MachshipCarrierIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._is_carrier_default

    @is_carrier_default.setter
    def is_carrier_default(self, is_carrier_default):
        """Sets the is_carrier_default of this MachshipCarrierIntegration.

        Whether or not the carrier specifies this integration as its default type  # noqa: E501

        :param is_carrier_default: The is_carrier_default of this MachshipCarrierIntegration.  # noqa: E501
        :type: bool
        """

        self._is_carrier_default = is_carrier_default

    @property
    def has_consignment_ref_pool(self):
        """Gets the has_consignment_ref_pool of this MachshipCarrierIntegration.  # noqa: E501


        :return: The has_consignment_ref_pool of this MachshipCarrierIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._has_consignment_ref_pool

    @has_consignment_ref_pool.setter
    def has_consignment_ref_pool(self, has_consignment_ref_pool):
        """Sets the has_consignment_ref_pool of this MachshipCarrierIntegration.


        :param has_consignment_ref_pool: The has_consignment_ref_pool of this MachshipCarrierIntegration.  # noqa: E501
        :type: bool
        """

        self._has_consignment_ref_pool = has_consignment_ref_pool

    @property
    def has_item_ref_pool(self):
        """Gets the has_item_ref_pool of this MachshipCarrierIntegration.  # noqa: E501


        :return: The has_item_ref_pool of this MachshipCarrierIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._has_item_ref_pool

    @has_item_ref_pool.setter
    def has_item_ref_pool(self, has_item_ref_pool):
        """Sets the has_item_ref_pool of this MachshipCarrierIntegration.


        :param has_item_ref_pool: The has_item_ref_pool of this MachshipCarrierIntegration.  # noqa: E501
        :type: bool
        """

        self._has_item_ref_pool = has_item_ref_pool

    @property
    def has_manifest_ref_pool(self):
        """Gets the has_manifest_ref_pool of this MachshipCarrierIntegration.  # noqa: E501


        :return: The has_manifest_ref_pool of this MachshipCarrierIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._has_manifest_ref_pool

    @has_manifest_ref_pool.setter
    def has_manifest_ref_pool(self, has_manifest_ref_pool):
        """Sets the has_manifest_ref_pool of this MachshipCarrierIntegration.


        :param has_manifest_ref_pool: The has_manifest_ref_pool of this MachshipCarrierIntegration.  # noqa: E501
        :type: bool
        """

        self._has_manifest_ref_pool = has_manifest_ref_pool

    @property
    def show_pickup_fields_when_manifesting(self):
        """Gets the show_pickup_fields_when_manifesting of this MachshipCarrierIntegration.  # noqa: E501


        :return: The show_pickup_fields_when_manifesting of this MachshipCarrierIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._show_pickup_fields_when_manifesting

    @show_pickup_fields_when_manifesting.setter
    def show_pickup_fields_when_manifesting(self, show_pickup_fields_when_manifesting):
        """Sets the show_pickup_fields_when_manifesting of this MachshipCarrierIntegration.


        :param show_pickup_fields_when_manifesting: The show_pickup_fields_when_manifesting of this MachshipCarrierIntegration.  # noqa: E501
        :type: bool
        """

        self._show_pickup_fields_when_manifesting = show_pickup_fields_when_manifesting

    @property
    def is_international(self):
        """Gets the is_international of this MachshipCarrierIntegration.  # noqa: E501


        :return: The is_international of this MachshipCarrierIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._is_international

    @is_international.setter
    def is_international(self, is_international):
        """Sets the is_international of this MachshipCarrierIntegration.


        :param is_international: The is_international of this MachshipCarrierIntegration.  # noqa: E501
        :type: bool
        """

        self._is_international = is_international

    @property
    def supports_sending_commercial_invoice(self):
        """Gets the supports_sending_commercial_invoice of this MachshipCarrierIntegration.  # noqa: E501


        :return: The supports_sending_commercial_invoice of this MachshipCarrierIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._supports_sending_commercial_invoice

    @supports_sending_commercial_invoice.setter
    def supports_sending_commercial_invoice(self, supports_sending_commercial_invoice):
        """Sets the supports_sending_commercial_invoice of this MachshipCarrierIntegration.


        :param supports_sending_commercial_invoice: The supports_sending_commercial_invoice of this MachshipCarrierIntegration.  # noqa: E501
        :type: bool
        """

        self._supports_sending_commercial_invoice = supports_sending_commercial_invoice

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
        if issubclass(MachshipCarrierIntegration, dict):
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
        if not isinstance(other, MachshipCarrierIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
