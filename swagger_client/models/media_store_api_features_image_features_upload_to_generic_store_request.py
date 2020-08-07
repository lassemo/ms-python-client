# coding: utf-8

"""
    MediaStore API

    MediaStore API for MediaStore  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest(object):
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
        'filename': 'str',
        'file_content': 'str',
        'title': 'str',
        'description': 'str',
        'internal_id': 'str',
        'product_group_id': 'str',
        'product_group_name': 'str',
        'media_group_id': 'str',
        'media_group_name': 'str'
    }

    attribute_map = {
        'filename': 'filename',
        'file_content': 'fileContent',
        'title': 'title',
        'description': 'description',
        'internal_id': 'internalId',
        'product_group_id': 'productGroupId',
        'product_group_name': 'productGroupName',
        'media_group_id': 'mediaGroupId',
        'media_group_name': 'mediaGroupName'
    }

    def __init__(self, filename=None, file_content=None, title=None, description=None, internal_id=None, product_group_id=None, product_group_name=None, media_group_id=None, media_group_name=None):  # noqa: E501
        """MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest - a model defined in Swagger"""  # noqa: E501
        self._filename = None
        self._file_content = None
        self._title = None
        self._description = None
        self._internal_id = None
        self._product_group_id = None
        self._product_group_name = None
        self._media_group_id = None
        self._media_group_name = None
        self.discriminator = None
        self.filename = filename
        self.file_content = file_content
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if internal_id is not None:
            self.internal_id = internal_id
        if product_group_id is not None:
            self.product_group_id = product_group_id
        if product_group_name is not None:
            self.product_group_name = product_group_name
        if media_group_id is not None:
            self.media_group_id = media_group_id
        if media_group_name is not None:
            self.media_group_name = media_group_name

    @property
    def filename(self):
        """Gets the filename of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501

        Image file name.  # noqa: E501

        :return: The filename of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.

        Image file name.  # noqa: E501

        :param filename: The filename of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def file_content(self):
        """Gets the file_content of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501

        Image file content.  Format: Base64 encoded byte array.  # noqa: E501

        :return: The file_content of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_content

    @file_content.setter
    def file_content(self, file_content):
        """Sets the file_content of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.

        Image file content.  Format: Base64 encoded byte array.  # noqa: E501

        :param file_content: The file_content of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :type: str
        """
        if file_content is None:
            raise ValueError("Invalid value for `file_content`, must not be `None`")  # noqa: E501

        self._file_content = file_content

    @property
    def title(self):
        """Gets the title of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501

        A Title of the image  # noqa: E501

        :return: The title of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.

        A Title of the image  # noqa: E501

        :param title: The title of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501

        A descriptive text of the image  # noqa: E501

        :return: The description of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.

        A descriptive text of the image  # noqa: E501

        :param description: The description of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def internal_id(self):
        """Gets the internal_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501

        An internal Id for the image  # noqa: E501

        :return: The internal_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.

        An internal Id for the image  # noqa: E501

        :param internal_id: The internal_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def product_group_id(self):
        """Gets the product_group_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501

        Obsolete (use MediaGroupID).A product group/category identification  # noqa: E501

        :return: The product_group_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._product_group_id

    @product_group_id.setter
    def product_group_id(self, product_group_id):
        """Sets the product_group_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.

        Obsolete (use MediaGroupID).A product group/category identification  # noqa: E501

        :param product_group_id: The product_group_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :type: str
        """

        self._product_group_id = product_group_id

    @property
    def product_group_name(self):
        """Gets the product_group_name of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501

        Obsolete (use MediaGroupName). A product group/category friendly name. This is the string that will show to users for product groups. E.g. \"Banana\"  # noqa: E501

        :return: The product_group_name of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._product_group_name

    @product_group_name.setter
    def product_group_name(self, product_group_name):
        """Sets the product_group_name of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.

        Obsolete (use MediaGroupName). A product group/category friendly name. This is the string that will show to users for product groups. E.g. \"Banana\"  # noqa: E501

        :param product_group_name: The product_group_name of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :type: str
        """

        self._product_group_name = product_group_name

    @property
    def media_group_id(self):
        """Gets the media_group_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501

        A media group/category identification. If this field is filled it will override ProductGroupID  # noqa: E501

        :return: The media_group_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._media_group_id

    @media_group_id.setter
    def media_group_id(self, media_group_id):
        """Sets the media_group_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.

        A media group/category identification. If this field is filled it will override ProductGroupID  # noqa: E501

        :param media_group_id: The media_group_id of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :type: str
        """

        self._media_group_id = media_group_id

    @property
    def media_group_name(self):
        """Gets the media_group_name of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501

        A product group/category friendly name. This is the string that will show to users for product groups. E.g. \"Banana\" . If this field is filled it will override any value in ProductGroupName  # noqa: E501

        :return: The media_group_name of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :rtype: str
        """
        return self._media_group_name

    @media_group_name.setter
    def media_group_name(self, media_group_name):
        """Sets the media_group_name of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.

        A product group/category friendly name. This is the string that will show to users for product groups. E.g. \"Banana\" . If this field is filled it will override any value in ProductGroupName  # noqa: E501

        :param media_group_name: The media_group_name of this MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.  # noqa: E501
        :type: str
        """

        self._media_group_name = media_group_name

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
        if issubclass(MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest, dict):
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
        if not isinstance(other, MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
