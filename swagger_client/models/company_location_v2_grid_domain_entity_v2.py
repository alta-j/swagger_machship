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

class CompanyLocationV2GridDomainEntityV2(object):
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
        'object': 'list[CompanyLocationV2]',
        'errors': 'list[MachshipValidationResultV2]',
        'total_items': 'int',
        'start_index': 'int',
        'retrieval_size': 'int'
    }

    attribute_map = {
        'object': 'object',
        'errors': 'errors',
        'total_items': 'totalItems',
        'start_index': 'startIndex',
        'retrieval_size': 'retrievalSize'
    }

    def __init__(self, object=None, errors=None, total_items=None, start_index=None, retrieval_size=None):  # noqa: E501
        """CompanyLocationV2GridDomainEntityV2 - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._errors = None
        self._total_items = None
        self._start_index = None
        self._retrieval_size = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if errors is not None:
            self.errors = errors
        if total_items is not None:
            self.total_items = total_items
        if start_index is not None:
            self.start_index = start_index
        if retrieval_size is not None:
            self.retrieval_size = retrieval_size

    @property
    def object(self):
        """Gets the object of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501


        :return: The object of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501
        :rtype: list[CompanyLocationV2]
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this CompanyLocationV2GridDomainEntityV2.


        :param object: The object of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501
        :type: list[CompanyLocationV2]
        """

        self._object = object

    @property
    def errors(self):
        """Gets the errors of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501


        :return: The errors of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501
        :rtype: list[MachshipValidationResultV2]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this CompanyLocationV2GridDomainEntityV2.


        :param errors: The errors of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501
        :type: list[MachshipValidationResultV2]
        """

        self._errors = errors

    @property
    def total_items(self):
        """Gets the total_items of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501


        :return: The total_items of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this CompanyLocationV2GridDomainEntityV2.


        :param total_items: The total_items of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def start_index(self):
        """Gets the start_index of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501


        :return: The start_index of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this CompanyLocationV2GridDomainEntityV2.


        :param start_index: The start_index of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501
        :type: int
        """

        self._start_index = start_index

    @property
    def retrieval_size(self):
        """Gets the retrieval_size of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501


        :return: The retrieval_size of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501
        :rtype: int
        """
        return self._retrieval_size

    @retrieval_size.setter
    def retrieval_size(self, retrieval_size):
        """Sets the retrieval_size of this CompanyLocationV2GridDomainEntityV2.


        :param retrieval_size: The retrieval_size of this CompanyLocationV2GridDomainEntityV2.  # noqa: E501
        :type: int
        """

        self._retrieval_size = retrieval_size

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
        if issubclass(CompanyLocationV2GridDomainEntityV2, dict):
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
        if not isinstance(other, CompanyLocationV2GridDomainEntityV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
