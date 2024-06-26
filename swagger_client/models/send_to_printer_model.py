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

class SendToPrinterModel(object):
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
        'any_group_is_dg': 'bool',
        'can_print_item_labels': 'bool',
        'can_print_consignments': 'bool',
        'can_print_manifests': 'bool',
        'all_groups_are_dg': 'bool',
        'all_groups_can_print_item_labels': 'bool',
        'all_groups_can_print_consignments': 'bool',
        'all_groups_can_print_manifests': 'bool',
        'all_groups_can_print_commercial_invoice': 'bool',
        'any_group_has_commercial_invoice': 'bool',
        'printers': 'list[PrinterLite]',
        'groups': 'list[SendToPrinterGroup]',
        'default_item_printer': 'PrinterLite',
        'default_a4_printer': 'PrinterLite'
    }

    attribute_map = {
        'any_group_is_dg': 'anyGroupIsDg',
        'can_print_item_labels': 'canPrintItemLabels',
        'can_print_consignments': 'canPrintConsignments',
        'can_print_manifests': 'canPrintManifests',
        'all_groups_are_dg': 'allGroupsAreDg',
        'all_groups_can_print_item_labels': 'allGroupsCanPrintItemLabels',
        'all_groups_can_print_consignments': 'allGroupsCanPrintConsignments',
        'all_groups_can_print_manifests': 'allGroupsCanPrintManifests',
        'all_groups_can_print_commercial_invoice': 'allGroupsCanPrintCommercialInvoice',
        'any_group_has_commercial_invoice': 'anyGroupHasCommercialInvoice',
        'printers': 'printers',
        'groups': 'groups',
        'default_item_printer': 'defaultItemPrinter',
        'default_a4_printer': 'defaultA4Printer'
    }

    def __init__(self, any_group_is_dg=None, can_print_item_labels=None, can_print_consignments=None, can_print_manifests=None, all_groups_are_dg=None, all_groups_can_print_item_labels=None, all_groups_can_print_consignments=None, all_groups_can_print_manifests=None, all_groups_can_print_commercial_invoice=None, any_group_has_commercial_invoice=None, printers=None, groups=None, default_item_printer=None, default_a4_printer=None):  # noqa: E501
        """SendToPrinterModel - a model defined in Swagger"""  # noqa: E501
        self._any_group_is_dg = None
        self._can_print_item_labels = None
        self._can_print_consignments = None
        self._can_print_manifests = None
        self._all_groups_are_dg = None
        self._all_groups_can_print_item_labels = None
        self._all_groups_can_print_consignments = None
        self._all_groups_can_print_manifests = None
        self._all_groups_can_print_commercial_invoice = None
        self._any_group_has_commercial_invoice = None
        self._printers = None
        self._groups = None
        self._default_item_printer = None
        self._default_a4_printer = None
        self.discriminator = None
        if any_group_is_dg is not None:
            self.any_group_is_dg = any_group_is_dg
        if can_print_item_labels is not None:
            self.can_print_item_labels = can_print_item_labels
        if can_print_consignments is not None:
            self.can_print_consignments = can_print_consignments
        if can_print_manifests is not None:
            self.can_print_manifests = can_print_manifests
        if all_groups_are_dg is not None:
            self.all_groups_are_dg = all_groups_are_dg
        if all_groups_can_print_item_labels is not None:
            self.all_groups_can_print_item_labels = all_groups_can_print_item_labels
        if all_groups_can_print_consignments is not None:
            self.all_groups_can_print_consignments = all_groups_can_print_consignments
        if all_groups_can_print_manifests is not None:
            self.all_groups_can_print_manifests = all_groups_can_print_manifests
        if all_groups_can_print_commercial_invoice is not None:
            self.all_groups_can_print_commercial_invoice = all_groups_can_print_commercial_invoice
        if any_group_has_commercial_invoice is not None:
            self.any_group_has_commercial_invoice = any_group_has_commercial_invoice
        if printers is not None:
            self.printers = printers
        if groups is not None:
            self.groups = groups
        if default_item_printer is not None:
            self.default_item_printer = default_item_printer
        if default_a4_printer is not None:
            self.default_a4_printer = default_a4_printer

    @property
    def any_group_is_dg(self):
        """Gets the any_group_is_dg of this SendToPrinterModel.  # noqa: E501


        :return: The any_group_is_dg of this SendToPrinterModel.  # noqa: E501
        :rtype: bool
        """
        return self._any_group_is_dg

    @any_group_is_dg.setter
    def any_group_is_dg(self, any_group_is_dg):
        """Sets the any_group_is_dg of this SendToPrinterModel.


        :param any_group_is_dg: The any_group_is_dg of this SendToPrinterModel.  # noqa: E501
        :type: bool
        """

        self._any_group_is_dg = any_group_is_dg

    @property
    def can_print_item_labels(self):
        """Gets the can_print_item_labels of this SendToPrinterModel.  # noqa: E501


        :return: The can_print_item_labels of this SendToPrinterModel.  # noqa: E501
        :rtype: bool
        """
        return self._can_print_item_labels

    @can_print_item_labels.setter
    def can_print_item_labels(self, can_print_item_labels):
        """Sets the can_print_item_labels of this SendToPrinterModel.


        :param can_print_item_labels: The can_print_item_labels of this SendToPrinterModel.  # noqa: E501
        :type: bool
        """

        self._can_print_item_labels = can_print_item_labels

    @property
    def can_print_consignments(self):
        """Gets the can_print_consignments of this SendToPrinterModel.  # noqa: E501


        :return: The can_print_consignments of this SendToPrinterModel.  # noqa: E501
        :rtype: bool
        """
        return self._can_print_consignments

    @can_print_consignments.setter
    def can_print_consignments(self, can_print_consignments):
        """Sets the can_print_consignments of this SendToPrinterModel.


        :param can_print_consignments: The can_print_consignments of this SendToPrinterModel.  # noqa: E501
        :type: bool
        """

        self._can_print_consignments = can_print_consignments

    @property
    def can_print_manifests(self):
        """Gets the can_print_manifests of this SendToPrinterModel.  # noqa: E501


        :return: The can_print_manifests of this SendToPrinterModel.  # noqa: E501
        :rtype: bool
        """
        return self._can_print_manifests

    @can_print_manifests.setter
    def can_print_manifests(self, can_print_manifests):
        """Sets the can_print_manifests of this SendToPrinterModel.


        :param can_print_manifests: The can_print_manifests of this SendToPrinterModel.  # noqa: E501
        :type: bool
        """

        self._can_print_manifests = can_print_manifests

    @property
    def all_groups_are_dg(self):
        """Gets the all_groups_are_dg of this SendToPrinterModel.  # noqa: E501


        :return: The all_groups_are_dg of this SendToPrinterModel.  # noqa: E501
        :rtype: bool
        """
        return self._all_groups_are_dg

    @all_groups_are_dg.setter
    def all_groups_are_dg(self, all_groups_are_dg):
        """Sets the all_groups_are_dg of this SendToPrinterModel.


        :param all_groups_are_dg: The all_groups_are_dg of this SendToPrinterModel.  # noqa: E501
        :type: bool
        """

        self._all_groups_are_dg = all_groups_are_dg

    @property
    def all_groups_can_print_item_labels(self):
        """Gets the all_groups_can_print_item_labels of this SendToPrinterModel.  # noqa: E501


        :return: The all_groups_can_print_item_labels of this SendToPrinterModel.  # noqa: E501
        :rtype: bool
        """
        return self._all_groups_can_print_item_labels

    @all_groups_can_print_item_labels.setter
    def all_groups_can_print_item_labels(self, all_groups_can_print_item_labels):
        """Sets the all_groups_can_print_item_labels of this SendToPrinterModel.


        :param all_groups_can_print_item_labels: The all_groups_can_print_item_labels of this SendToPrinterModel.  # noqa: E501
        :type: bool
        """

        self._all_groups_can_print_item_labels = all_groups_can_print_item_labels

    @property
    def all_groups_can_print_consignments(self):
        """Gets the all_groups_can_print_consignments of this SendToPrinterModel.  # noqa: E501


        :return: The all_groups_can_print_consignments of this SendToPrinterModel.  # noqa: E501
        :rtype: bool
        """
        return self._all_groups_can_print_consignments

    @all_groups_can_print_consignments.setter
    def all_groups_can_print_consignments(self, all_groups_can_print_consignments):
        """Sets the all_groups_can_print_consignments of this SendToPrinterModel.


        :param all_groups_can_print_consignments: The all_groups_can_print_consignments of this SendToPrinterModel.  # noqa: E501
        :type: bool
        """

        self._all_groups_can_print_consignments = all_groups_can_print_consignments

    @property
    def all_groups_can_print_manifests(self):
        """Gets the all_groups_can_print_manifests of this SendToPrinterModel.  # noqa: E501


        :return: The all_groups_can_print_manifests of this SendToPrinterModel.  # noqa: E501
        :rtype: bool
        """
        return self._all_groups_can_print_manifests

    @all_groups_can_print_manifests.setter
    def all_groups_can_print_manifests(self, all_groups_can_print_manifests):
        """Sets the all_groups_can_print_manifests of this SendToPrinterModel.


        :param all_groups_can_print_manifests: The all_groups_can_print_manifests of this SendToPrinterModel.  # noqa: E501
        :type: bool
        """

        self._all_groups_can_print_manifests = all_groups_can_print_manifests

    @property
    def all_groups_can_print_commercial_invoice(self):
        """Gets the all_groups_can_print_commercial_invoice of this SendToPrinterModel.  # noqa: E501


        :return: The all_groups_can_print_commercial_invoice of this SendToPrinterModel.  # noqa: E501
        :rtype: bool
        """
        return self._all_groups_can_print_commercial_invoice

    @all_groups_can_print_commercial_invoice.setter
    def all_groups_can_print_commercial_invoice(self, all_groups_can_print_commercial_invoice):
        """Sets the all_groups_can_print_commercial_invoice of this SendToPrinterModel.


        :param all_groups_can_print_commercial_invoice: The all_groups_can_print_commercial_invoice of this SendToPrinterModel.  # noqa: E501
        :type: bool
        """

        self._all_groups_can_print_commercial_invoice = all_groups_can_print_commercial_invoice

    @property
    def any_group_has_commercial_invoice(self):
        """Gets the any_group_has_commercial_invoice of this SendToPrinterModel.  # noqa: E501


        :return: The any_group_has_commercial_invoice of this SendToPrinterModel.  # noqa: E501
        :rtype: bool
        """
        return self._any_group_has_commercial_invoice

    @any_group_has_commercial_invoice.setter
    def any_group_has_commercial_invoice(self, any_group_has_commercial_invoice):
        """Sets the any_group_has_commercial_invoice of this SendToPrinterModel.


        :param any_group_has_commercial_invoice: The any_group_has_commercial_invoice of this SendToPrinterModel.  # noqa: E501
        :type: bool
        """

        self._any_group_has_commercial_invoice = any_group_has_commercial_invoice

    @property
    def printers(self):
        """Gets the printers of this SendToPrinterModel.  # noqa: E501


        :return: The printers of this SendToPrinterModel.  # noqa: E501
        :rtype: list[PrinterLite]
        """
        return self._printers

    @printers.setter
    def printers(self, printers):
        """Sets the printers of this SendToPrinterModel.


        :param printers: The printers of this SendToPrinterModel.  # noqa: E501
        :type: list[PrinterLite]
        """

        self._printers = printers

    @property
    def groups(self):
        """Gets the groups of this SendToPrinterModel.  # noqa: E501


        :return: The groups of this SendToPrinterModel.  # noqa: E501
        :rtype: list[SendToPrinterGroup]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this SendToPrinterModel.


        :param groups: The groups of this SendToPrinterModel.  # noqa: E501
        :type: list[SendToPrinterGroup]
        """

        self._groups = groups

    @property
    def default_item_printer(self):
        """Gets the default_item_printer of this SendToPrinterModel.  # noqa: E501


        :return: The default_item_printer of this SendToPrinterModel.  # noqa: E501
        :rtype: PrinterLite
        """
        return self._default_item_printer

    @default_item_printer.setter
    def default_item_printer(self, default_item_printer):
        """Sets the default_item_printer of this SendToPrinterModel.


        :param default_item_printer: The default_item_printer of this SendToPrinterModel.  # noqa: E501
        :type: PrinterLite
        """

        self._default_item_printer = default_item_printer

    @property
    def default_a4_printer(self):
        """Gets the default_a4_printer of this SendToPrinterModel.  # noqa: E501


        :return: The default_a4_printer of this SendToPrinterModel.  # noqa: E501
        :rtype: PrinterLite
        """
        return self._default_a4_printer

    @default_a4_printer.setter
    def default_a4_printer(self, default_a4_printer):
        """Sets the default_a4_printer of this SendToPrinterModel.


        :param default_a4_printer: The default_a4_printer of this SendToPrinterModel.  # noqa: E501
        :type: PrinterLite
        """

        self._default_a4_printer = default_a4_printer

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
        if issubclass(SendToPrinterModel, dict):
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
        if not isinstance(other, SendToPrinterModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
