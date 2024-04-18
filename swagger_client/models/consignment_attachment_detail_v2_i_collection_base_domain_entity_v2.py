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

class ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2(object):
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
        'object': 'list[ConsignmentAttachmentDetailV2]',
        'errors': 'list[MachshipValidationResultV2]'
    }

    attribute_map = {
        'object': 'object',
        'errors': 'errors'
    }

    def __init__(self, object=None, errors=None):  # noqa: E501
        """ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2 - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._errors = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if errors is not None:
            self.errors = errors

    @property
    def object(self):
        """Gets the object of this ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2.  # noqa: E501


        :return: The object of this ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2.  # noqa: E501
        :rtype: list[ConsignmentAttachmentDetailV2]
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2.


        :param object: The object of this ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2.  # noqa: E501
        :type: list[ConsignmentAttachmentDetailV2]
        """

        self._object = object

    @property
    def errors(self):
        """Gets the errors of this ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2.  # noqa: E501


        :return: The errors of this ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2.  # noqa: E501
        :rtype: list[MachshipValidationResultV2]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2.


        :param errors: The errors of this ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2.  # noqa: E501
        :type: list[MachshipValidationResultV2]
        """

        self._errors = errors

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
        if issubclass(ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2, dict):
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
        if not isinstance(other, ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
