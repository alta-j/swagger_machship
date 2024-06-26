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

class ConsignmentToConsolidate(object):
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
        'carrier': 'CarrierLite',
        'service': 'CarrierServiceLite',
        'account': 'CarrierAccountLite',
        'company_carrier_account': 'CompanyCarrierAccountLite',
        'is_pending_consignment': 'bool',
        'has_printed_labels': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'consignment_number': 'consignmentNumber',
        'carrier': 'carrier',
        'service': 'service',
        'account': 'account',
        'company_carrier_account': 'companyCarrierAccount',
        'is_pending_consignment': 'isPendingConsignment',
        'has_printed_labels': 'hasPrintedLabels'
    }

    def __init__(self, id=None, consignment_number=None, carrier=None, service=None, account=None, company_carrier_account=None, is_pending_consignment=None, has_printed_labels=None):  # noqa: E501
        """ConsignmentToConsolidate - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._consignment_number = None
        self._carrier = None
        self._service = None
        self._account = None
        self._company_carrier_account = None
        self._is_pending_consignment = None
        self._has_printed_labels = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if consignment_number is not None:
            self.consignment_number = consignment_number
        if carrier is not None:
            self.carrier = carrier
        if service is not None:
            self.service = service
        if account is not None:
            self.account = account
        if company_carrier_account is not None:
            self.company_carrier_account = company_carrier_account
        if is_pending_consignment is not None:
            self.is_pending_consignment = is_pending_consignment
        if has_printed_labels is not None:
            self.has_printed_labels = has_printed_labels

    @property
    def id(self):
        """Gets the id of this ConsignmentToConsolidate.  # noqa: E501

        Machship's Consignment / Pending Consignment ID  # noqa: E501

        :return: The id of this ConsignmentToConsolidate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConsignmentToConsolidate.

        Machship's Consignment / Pending Consignment ID  # noqa: E501

        :param id: The id of this ConsignmentToConsolidate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def consignment_number(self):
        """Gets the consignment_number of this ConsignmentToConsolidate.  # noqa: E501

        Machship's Consignment (MS) or Pending Consignment (PS) number  # noqa: E501

        :return: The consignment_number of this ConsignmentToConsolidate.  # noqa: E501
        :rtype: str
        """
        return self._consignment_number

    @consignment_number.setter
    def consignment_number(self, consignment_number):
        """Sets the consignment_number of this ConsignmentToConsolidate.

        Machship's Consignment (MS) or Pending Consignment (PS) number  # noqa: E501

        :param consignment_number: The consignment_number of this ConsignmentToConsolidate.  # noqa: E501
        :type: str
        """

        self._consignment_number = consignment_number

    @property
    def carrier(self):
        """Gets the carrier of this ConsignmentToConsolidate.  # noqa: E501


        :return: The carrier of this ConsignmentToConsolidate.  # noqa: E501
        :rtype: CarrierLite
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this ConsignmentToConsolidate.


        :param carrier: The carrier of this ConsignmentToConsolidate.  # noqa: E501
        :type: CarrierLite
        """

        self._carrier = carrier

    @property
    def service(self):
        """Gets the service of this ConsignmentToConsolidate.  # noqa: E501


        :return: The service of this ConsignmentToConsolidate.  # noqa: E501
        :rtype: CarrierServiceLite
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ConsignmentToConsolidate.


        :param service: The service of this ConsignmentToConsolidate.  # noqa: E501
        :type: CarrierServiceLite
        """

        self._service = service

    @property
    def account(self):
        """Gets the account of this ConsignmentToConsolidate.  # noqa: E501


        :return: The account of this ConsignmentToConsolidate.  # noqa: E501
        :rtype: CarrierAccountLite
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ConsignmentToConsolidate.


        :param account: The account of this ConsignmentToConsolidate.  # noqa: E501
        :type: CarrierAccountLite
        """

        self._account = account

    @property
    def company_carrier_account(self):
        """Gets the company_carrier_account of this ConsignmentToConsolidate.  # noqa: E501


        :return: The company_carrier_account of this ConsignmentToConsolidate.  # noqa: E501
        :rtype: CompanyCarrierAccountLite
        """
        return self._company_carrier_account

    @company_carrier_account.setter
    def company_carrier_account(self, company_carrier_account):
        """Sets the company_carrier_account of this ConsignmentToConsolidate.


        :param company_carrier_account: The company_carrier_account of this ConsignmentToConsolidate.  # noqa: E501
        :type: CompanyCarrierAccountLite
        """

        self._company_carrier_account = company_carrier_account

    @property
    def is_pending_consignment(self):
        """Gets the is_pending_consignment of this ConsignmentToConsolidate.  # noqa: E501


        :return: The is_pending_consignment of this ConsignmentToConsolidate.  # noqa: E501
        :rtype: bool
        """
        return self._is_pending_consignment

    @is_pending_consignment.setter
    def is_pending_consignment(self, is_pending_consignment):
        """Sets the is_pending_consignment of this ConsignmentToConsolidate.


        :param is_pending_consignment: The is_pending_consignment of this ConsignmentToConsolidate.  # noqa: E501
        :type: bool
        """

        self._is_pending_consignment = is_pending_consignment

    @property
    def has_printed_labels(self):
        """Gets the has_printed_labels of this ConsignmentToConsolidate.  # noqa: E501


        :return: The has_printed_labels of this ConsignmentToConsolidate.  # noqa: E501
        :rtype: bool
        """
        return self._has_printed_labels

    @has_printed_labels.setter
    def has_printed_labels(self, has_printed_labels):
        """Sets the has_printed_labels of this ConsignmentToConsolidate.


        :param has_printed_labels: The has_printed_labels of this ConsignmentToConsolidate.  # noqa: E501
        :type: bool
        """

        self._has_printed_labels = has_printed_labels

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
        if issubclass(ConsignmentToConsolidate, dict):
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
        if not isinstance(other, ConsignmentToConsolidate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
