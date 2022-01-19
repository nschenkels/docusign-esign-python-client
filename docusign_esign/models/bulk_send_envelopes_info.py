# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class BulkSendEnvelopesInfo(object):
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
        'completed': 'str',
        'declined': 'str',
        'voided': 'str'
    }

    attribute_map = {
        'completed': 'completed',
        'declined': 'declined',
        'voided': 'voided'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkSendEnvelopesInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._completed = None
        self._declined = None
        self._voided = None
        self.discriminator = None

        setattr(self, "_{}".format('completed'), kwargs.get('completed', None))
        setattr(self, "_{}".format('declined'), kwargs.get('declined', None))
        setattr(self, "_{}".format('voided'), kwargs.get('voided', None))

    @property
    def completed(self):
        """Gets the completed of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The completed of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param completed: The completed of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._completed = completed

    @property
    def declined(self):
        """Gets the declined of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The declined of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._declined

    @declined.setter
    def declined(self, declined):
        """Sets the declined of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param declined: The declined of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._declined = declined

    @property
    def voided(self):
        """Gets the voided of this BulkSendEnvelopesInfo.  # noqa: E501

          # noqa: E501

        :return: The voided of this BulkSendEnvelopesInfo.  # noqa: E501
        :rtype: str
        """
        return self._voided

    @voided.setter
    def voided(self, voided):
        """Sets the voided of this BulkSendEnvelopesInfo.

          # noqa: E501

        :param voided: The voided of this BulkSendEnvelopesInfo.  # noqa: E501
        :type: str
        """

        self._voided = voided

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
        if issubclass(BulkSendEnvelopesInfo, dict):
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
        if not isinstance(other, BulkSendEnvelopesInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkSendEnvelopesInfo):
            return True

        return self.to_dict() != other.to_dict()