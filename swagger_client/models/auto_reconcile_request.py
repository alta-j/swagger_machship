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

class AutoReconcileRequest(object):
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
        'consignment_ids': 'list[int]',
        'reason': 'str'
    }

    attribute_map = {
        'consignment_ids': 'consignmentIds',
        'reason': 'reason'
    }

    def __init__(self, consignment_ids=None, reason=None):  # noqa: E501
        """AutoReconcileRequest - a model defined in Swagger"""  # noqa: E501
        self._consignment_ids = None
        self._reason = None
        self.discriminator = None
        if consignment_ids is not None:
            self.consignment_ids = consignment_ids
        if reason is not None:
            self.reason = reason

    @property
    def consignment_ids(self):
        """Gets the consignment_ids of this AutoReconcileRequest.  # noqa: E501


        :return: The consignment_ids of this AutoReconcileRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._consignment_ids

    @consignment_ids.setter
    def consignment_ids(self, consignment_ids):
        """Sets the consignment_ids of this AutoReconcileRequest.


        :param consignment_ids: The consignment_ids of this AutoReconcileRequest.  # noqa: E501
        :type: list[int]
        """

        self._consignment_ids = consignment_ids

    @property
    def reason(self):
        """Gets the reason of this AutoReconcileRequest.  # noqa: E501


        :return: The reason of this AutoReconcileRequest.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this AutoReconcileRequest.


        :param reason: The reason of this AutoReconcileRequest.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if issubclass(AutoReconcileRequest, dict):
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
        if not isinstance(other, AutoReconcileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
