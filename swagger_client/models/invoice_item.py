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

class InvoiceItem(object):
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
        'invoice_id': 'int',
        'invoice': 'Invoice',
        'insertion_guid': 'str',
        'crc_insertion_guid': 'str',
        'billing_charge_insertion_guid': 'str',
        'invoice_document_number': 'str',
        'consignment': 'Consignment',
        'has_consignment': 'bool',
        'id': 'int',
        'description': 'str',
        'quantity': 'float',
        'base_charge_each': 'float',
        'fuel_levy_each': 'float',
        'tax_amount_each': 'float',
        'tax_percentage': 'float',
        'total_base_charge': 'float',
        'total_fuel_levy': 'float',
        'total_tax': 'float',
        'total': 'float',
        'item_type_abbreviation': 'str',
        'item_type_name': 'str',
        'machship_item_type': 'str',
        'consignment_number': 'str',
        'is_manual_entry': 'bool',
        'consignment_id': 'int',
        'consignment_reconciliation_charges': 'list[ConsignmentReconciliationCharge]',
        'company_billing_charge': 'CompanyBillingCharge',
        'is_international': 'bool'
    }

    attribute_map = {
        'invoice_id': 'invoiceId',
        'invoice': 'invoice',
        'insertion_guid': 'insertionGuid',
        'crc_insertion_guid': 'crcInsertionGuid',
        'billing_charge_insertion_guid': 'billingChargeInsertionGuid',
        'invoice_document_number': 'invoiceDocumentNumber',
        'consignment': 'consignment',
        'has_consignment': 'hasConsignment',
        'id': 'id',
        'description': 'description',
        'quantity': 'quantity',
        'base_charge_each': 'baseChargeEach',
        'fuel_levy_each': 'fuelLevyEach',
        'tax_amount_each': 'taxAmountEach',
        'tax_percentage': 'taxPercentage',
        'total_base_charge': 'totalBaseCharge',
        'total_fuel_levy': 'totalFuelLevy',
        'total_tax': 'totalTax',
        'total': 'total',
        'item_type_abbreviation': 'itemTypeAbbreviation',
        'item_type_name': 'itemTypeName',
        'machship_item_type': 'machshipItemType',
        'consignment_number': 'consignmentNumber',
        'is_manual_entry': 'isManualEntry',
        'consignment_id': 'consignmentId',
        'consignment_reconciliation_charges': 'consignmentReconciliationCharges',
        'company_billing_charge': 'companyBillingCharge',
        'is_international': 'isInternational'
    }

    def __init__(self, invoice_id=None, invoice=None, insertion_guid=None, crc_insertion_guid=None, billing_charge_insertion_guid=None, invoice_document_number=None, consignment=None, has_consignment=None, id=None, description=None, quantity=None, base_charge_each=None, fuel_levy_each=None, tax_amount_each=None, tax_percentage=None, total_base_charge=None, total_fuel_levy=None, total_tax=None, total=None, item_type_abbreviation=None, item_type_name=None, machship_item_type=None, consignment_number=None, is_manual_entry=None, consignment_id=None, consignment_reconciliation_charges=None, company_billing_charge=None, is_international=None):  # noqa: E501
        """InvoiceItem - a model defined in Swagger"""  # noqa: E501
        self._invoice_id = None
        self._invoice = None
        self._insertion_guid = None
        self._crc_insertion_guid = None
        self._billing_charge_insertion_guid = None
        self._invoice_document_number = None
        self._consignment = None
        self._has_consignment = None
        self._id = None
        self._description = None
        self._quantity = None
        self._base_charge_each = None
        self._fuel_levy_each = None
        self._tax_amount_each = None
        self._tax_percentage = None
        self._total_base_charge = None
        self._total_fuel_levy = None
        self._total_tax = None
        self._total = None
        self._item_type_abbreviation = None
        self._item_type_name = None
        self._machship_item_type = None
        self._consignment_number = None
        self._is_manual_entry = None
        self._consignment_id = None
        self._consignment_reconciliation_charges = None
        self._company_billing_charge = None
        self._is_international = None
        self.discriminator = None
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if invoice is not None:
            self.invoice = invoice
        if insertion_guid is not None:
            self.insertion_guid = insertion_guid
        if crc_insertion_guid is not None:
            self.crc_insertion_guid = crc_insertion_guid
        if billing_charge_insertion_guid is not None:
            self.billing_charge_insertion_guid = billing_charge_insertion_guid
        if invoice_document_number is not None:
            self.invoice_document_number = invoice_document_number
        if consignment is not None:
            self.consignment = consignment
        if has_consignment is not None:
            self.has_consignment = has_consignment
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        self.quantity = quantity
        if base_charge_each is not None:
            self.base_charge_each = base_charge_each
        if fuel_levy_each is not None:
            self.fuel_levy_each = fuel_levy_each
        if tax_amount_each is not None:
            self.tax_amount_each = tax_amount_each
        if tax_percentage is not None:
            self.tax_percentage = tax_percentage
        if total_base_charge is not None:
            self.total_base_charge = total_base_charge
        if total_fuel_levy is not None:
            self.total_fuel_levy = total_fuel_levy
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if item_type_abbreviation is not None:
            self.item_type_abbreviation = item_type_abbreviation
        if item_type_name is not None:
            self.item_type_name = item_type_name
        if machship_item_type is not None:
            self.machship_item_type = machship_item_type
        if consignment_number is not None:
            self.consignment_number = consignment_number
        if is_manual_entry is not None:
            self.is_manual_entry = is_manual_entry
        if consignment_id is not None:
            self.consignment_id = consignment_id
        if consignment_reconciliation_charges is not None:
            self.consignment_reconciliation_charges = consignment_reconciliation_charges
        if company_billing_charge is not None:
            self.company_billing_charge = company_billing_charge
        if is_international is not None:
            self.is_international = is_international

    @property
    def invoice_id(self):
        """Gets the invoice_id of this InvoiceItem.  # noqa: E501


        :return: The invoice_id of this InvoiceItem.  # noqa: E501
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this InvoiceItem.


        :param invoice_id: The invoice_id of this InvoiceItem.  # noqa: E501
        :type: int
        """

        self._invoice_id = invoice_id

    @property
    def invoice(self):
        """Gets the invoice of this InvoiceItem.  # noqa: E501


        :return: The invoice of this InvoiceItem.  # noqa: E501
        :rtype: Invoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this InvoiceItem.


        :param invoice: The invoice of this InvoiceItem.  # noqa: E501
        :type: Invoice
        """

        self._invoice = invoice

    @property
    def insertion_guid(self):
        """Gets the insertion_guid of this InvoiceItem.  # noqa: E501


        :return: The insertion_guid of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._insertion_guid

    @insertion_guid.setter
    def insertion_guid(self, insertion_guid):
        """Sets the insertion_guid of this InvoiceItem.


        :param insertion_guid: The insertion_guid of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._insertion_guid = insertion_guid

    @property
    def crc_insertion_guid(self):
        """Gets the crc_insertion_guid of this InvoiceItem.  # noqa: E501


        :return: The crc_insertion_guid of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._crc_insertion_guid

    @crc_insertion_guid.setter
    def crc_insertion_guid(self, crc_insertion_guid):
        """Sets the crc_insertion_guid of this InvoiceItem.


        :param crc_insertion_guid: The crc_insertion_guid of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._crc_insertion_guid = crc_insertion_guid

    @property
    def billing_charge_insertion_guid(self):
        """Gets the billing_charge_insertion_guid of this InvoiceItem.  # noqa: E501

        This is used to link the invoice item to the billing charge when generating invoices  # noqa: E501

        :return: The billing_charge_insertion_guid of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._billing_charge_insertion_guid

    @billing_charge_insertion_guid.setter
    def billing_charge_insertion_guid(self, billing_charge_insertion_guid):
        """Sets the billing_charge_insertion_guid of this InvoiceItem.

        This is used to link the invoice item to the billing charge when generating invoices  # noqa: E501

        :param billing_charge_insertion_guid: The billing_charge_insertion_guid of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._billing_charge_insertion_guid = billing_charge_insertion_guid

    @property
    def invoice_document_number(self):
        """Gets the invoice_document_number of this InvoiceItem.  # noqa: E501


        :return: The invoice_document_number of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._invoice_document_number

    @invoice_document_number.setter
    def invoice_document_number(self, invoice_document_number):
        """Sets the invoice_document_number of this InvoiceItem.


        :param invoice_document_number: The invoice_document_number of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._invoice_document_number = invoice_document_number

    @property
    def consignment(self):
        """Gets the consignment of this InvoiceItem.  # noqa: E501


        :return: The consignment of this InvoiceItem.  # noqa: E501
        :rtype: Consignment
        """
        return self._consignment

    @consignment.setter
    def consignment(self, consignment):
        """Sets the consignment of this InvoiceItem.


        :param consignment: The consignment of this InvoiceItem.  # noqa: E501
        :type: Consignment
        """

        self._consignment = consignment

    @property
    def has_consignment(self):
        """Gets the has_consignment of this InvoiceItem.  # noqa: E501


        :return: The has_consignment of this InvoiceItem.  # noqa: E501
        :rtype: bool
        """
        return self._has_consignment

    @has_consignment.setter
    def has_consignment(self, has_consignment):
        """Sets the has_consignment of this InvoiceItem.


        :param has_consignment: The has_consignment of this InvoiceItem.  # noqa: E501
        :type: bool
        """

        self._has_consignment = has_consignment

    @property
    def id(self):
        """Gets the id of this InvoiceItem.  # noqa: E501


        :return: The id of this InvoiceItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceItem.


        :param id: The id of this InvoiceItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this InvoiceItem.  # noqa: E501


        :return: The description of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InvoiceItem.


        :param description: The description of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def quantity(self):
        """Gets the quantity of this InvoiceItem.  # noqa: E501


        :return: The quantity of this InvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InvoiceItem.


        :param quantity: The quantity of this InvoiceItem.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def base_charge_each(self):
        """Gets the base_charge_each of this InvoiceItem.  # noqa: E501


        :return: The base_charge_each of this InvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._base_charge_each

    @base_charge_each.setter
    def base_charge_each(self, base_charge_each):
        """Sets the base_charge_each of this InvoiceItem.


        :param base_charge_each: The base_charge_each of this InvoiceItem.  # noqa: E501
        :type: float
        """

        self._base_charge_each = base_charge_each

    @property
    def fuel_levy_each(self):
        """Gets the fuel_levy_each of this InvoiceItem.  # noqa: E501


        :return: The fuel_levy_each of this InvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._fuel_levy_each

    @fuel_levy_each.setter
    def fuel_levy_each(self, fuel_levy_each):
        """Sets the fuel_levy_each of this InvoiceItem.


        :param fuel_levy_each: The fuel_levy_each of this InvoiceItem.  # noqa: E501
        :type: float
        """

        self._fuel_levy_each = fuel_levy_each

    @property
    def tax_amount_each(self):
        """Gets the tax_amount_each of this InvoiceItem.  # noqa: E501


        :return: The tax_amount_each of this InvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount_each

    @tax_amount_each.setter
    def tax_amount_each(self, tax_amount_each):
        """Sets the tax_amount_each of this InvoiceItem.


        :param tax_amount_each: The tax_amount_each of this InvoiceItem.  # noqa: E501
        :type: float
        """

        self._tax_amount_each = tax_amount_each

    @property
    def tax_percentage(self):
        """Gets the tax_percentage of this InvoiceItem.  # noqa: E501


        :return: The tax_percentage of this InvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage):
        """Sets the tax_percentage of this InvoiceItem.


        :param tax_percentage: The tax_percentage of this InvoiceItem.  # noqa: E501
        :type: float
        """

        self._tax_percentage = tax_percentage

    @property
    def total_base_charge(self):
        """Gets the total_base_charge of this InvoiceItem.  # noqa: E501


        :return: The total_base_charge of this InvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._total_base_charge

    @total_base_charge.setter
    def total_base_charge(self, total_base_charge):
        """Sets the total_base_charge of this InvoiceItem.


        :param total_base_charge: The total_base_charge of this InvoiceItem.  # noqa: E501
        :type: float
        """

        self._total_base_charge = total_base_charge

    @property
    def total_fuel_levy(self):
        """Gets the total_fuel_levy of this InvoiceItem.  # noqa: E501


        :return: The total_fuel_levy of this InvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._total_fuel_levy

    @total_fuel_levy.setter
    def total_fuel_levy(self, total_fuel_levy):
        """Sets the total_fuel_levy of this InvoiceItem.


        :param total_fuel_levy: The total_fuel_levy of this InvoiceItem.  # noqa: E501
        :type: float
        """

        self._total_fuel_levy = total_fuel_levy

    @property
    def total_tax(self):
        """Gets the total_tax of this InvoiceItem.  # noqa: E501


        :return: The total_tax of this InvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this InvoiceItem.


        :param total_tax: The total_tax of this InvoiceItem.  # noqa: E501
        :type: float
        """

        self._total_tax = total_tax

    @property
    def total(self):
        """Gets the total of this InvoiceItem.  # noqa: E501


        :return: The total of this InvoiceItem.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InvoiceItem.


        :param total: The total of this InvoiceItem.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def item_type_abbreviation(self):
        """Gets the item_type_abbreviation of this InvoiceItem.  # noqa: E501

        This information is not persisted and is only used when generating the csv invoices.  This helps determine which type of line item we are currently using  # noqa: E501

        :return: The item_type_abbreviation of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._item_type_abbreviation

    @item_type_abbreviation.setter
    def item_type_abbreviation(self, item_type_abbreviation):
        """Sets the item_type_abbreviation of this InvoiceItem.

        This information is not persisted and is only used when generating the csv invoices.  This helps determine which type of line item we are currently using  # noqa: E501

        :param item_type_abbreviation: The item_type_abbreviation of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._item_type_abbreviation = item_type_abbreviation

    @property
    def item_type_name(self):
        """Gets the item_type_name of this InvoiceItem.  # noqa: E501


        :return: The item_type_name of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._item_type_name

    @item_type_name.setter
    def item_type_name(self, item_type_name):
        """Sets the item_type_name of this InvoiceItem.


        :param item_type_name: The item_type_name of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._item_type_name = item_type_name

    @property
    def machship_item_type(self):
        """Gets the machship_item_type of this InvoiceItem.  # noqa: E501


        :return: The machship_item_type of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._machship_item_type

    @machship_item_type.setter
    def machship_item_type(self, machship_item_type):
        """Sets the machship_item_type of this InvoiceItem.


        :param machship_item_type: The machship_item_type of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._machship_item_type = machship_item_type

    @property
    def consignment_number(self):
        """Gets the consignment_number of this InvoiceItem.  # noqa: E501

        This is only used when generating the invoices for csv and pdf.  # noqa: E501

        :return: The consignment_number of this InvoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._consignment_number

    @consignment_number.setter
    def consignment_number(self, consignment_number):
        """Sets the consignment_number of this InvoiceItem.

        This is only used when generating the invoices for csv and pdf.  # noqa: E501

        :param consignment_number: The consignment_number of this InvoiceItem.  # noqa: E501
        :type: str
        """

        self._consignment_number = consignment_number

    @property
    def is_manual_entry(self):
        """Gets the is_manual_entry of this InvoiceItem.  # noqa: E501


        :return: The is_manual_entry of this InvoiceItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_manual_entry

    @is_manual_entry.setter
    def is_manual_entry(self, is_manual_entry):
        """Sets the is_manual_entry of this InvoiceItem.


        :param is_manual_entry: The is_manual_entry of this InvoiceItem.  # noqa: E501
        :type: bool
        """

        self._is_manual_entry = is_manual_entry

    @property
    def consignment_id(self):
        """Gets the consignment_id of this InvoiceItem.  # noqa: E501


        :return: The consignment_id of this InvoiceItem.  # noqa: E501
        :rtype: int
        """
        return self._consignment_id

    @consignment_id.setter
    def consignment_id(self, consignment_id):
        """Sets the consignment_id of this InvoiceItem.


        :param consignment_id: The consignment_id of this InvoiceItem.  # noqa: E501
        :type: int
        """

        self._consignment_id = consignment_id

    @property
    def consignment_reconciliation_charges(self):
        """Gets the consignment_reconciliation_charges of this InvoiceItem.  # noqa: E501


        :return: The consignment_reconciliation_charges of this InvoiceItem.  # noqa: E501
        :rtype: list[ConsignmentReconciliationCharge]
        """
        return self._consignment_reconciliation_charges

    @consignment_reconciliation_charges.setter
    def consignment_reconciliation_charges(self, consignment_reconciliation_charges):
        """Sets the consignment_reconciliation_charges of this InvoiceItem.


        :param consignment_reconciliation_charges: The consignment_reconciliation_charges of this InvoiceItem.  # noqa: E501
        :type: list[ConsignmentReconciliationCharge]
        """

        self._consignment_reconciliation_charges = consignment_reconciliation_charges

    @property
    def company_billing_charge(self):
        """Gets the company_billing_charge of this InvoiceItem.  # noqa: E501


        :return: The company_billing_charge of this InvoiceItem.  # noqa: E501
        :rtype: CompanyBillingCharge
        """
        return self._company_billing_charge

    @company_billing_charge.setter
    def company_billing_charge(self, company_billing_charge):
        """Sets the company_billing_charge of this InvoiceItem.


        :param company_billing_charge: The company_billing_charge of this InvoiceItem.  # noqa: E501
        :type: CompanyBillingCharge
        """

        self._company_billing_charge = company_billing_charge

    @property
    def is_international(self):
        """Gets the is_international of this InvoiceItem.  # noqa: E501


        :return: The is_international of this InvoiceItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_international

    @is_international.setter
    def is_international(self, is_international):
        """Sets the is_international of this InvoiceItem.


        :param is_international: The is_international of this InvoiceItem.  # noqa: E501
        :type: bool
        """

        self._is_international = is_international

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
        if issubclass(InvoiceItem, dict):
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
        if not isinstance(other, InvoiceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
