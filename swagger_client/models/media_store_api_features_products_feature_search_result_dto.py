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

class MediaStoreAPIFeaturesProductsFeatureSearchResultDto(object):
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
        'product': 'MediaStoreAPIFeaturesProductsFeatureProductDto',
        'images': 'list[MediaStoreAPIFeaturesProductsFeatureImageDto]',
        'space_images': 'list[MediaStoreAPIFeaturesProductsFeatureImageDto]'
    }

    attribute_map = {
        'product': 'product',
        'images': 'images',
        'space_images': 'spaceImages'
    }

    def __init__(self, product=None, images=None, space_images=None):  # noqa: E501
        """MediaStoreAPIFeaturesProductsFeatureSearchResultDto - a model defined in Swagger"""  # noqa: E501
        self._product = None
        self._images = None
        self._space_images = None
        self.discriminator = None
        if product is not None:
            self.product = product
        if images is not None:
            self.images = images
        if space_images is not None:
            self.space_images = space_images

    @property
    def product(self):
        """Gets the product of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.  # noqa: E501


        :return: The product of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.  # noqa: E501
        :rtype: MediaStoreAPIFeaturesProductsFeatureProductDto
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.


        :param product: The product of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.  # noqa: E501
        :type: MediaStoreAPIFeaturesProductsFeatureProductDto
        """

        self._product = product

    @property
    def images(self):
        """Gets the images of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.  # noqa: E501


        :return: The images of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.  # noqa: E501
        :rtype: list[MediaStoreAPIFeaturesProductsFeatureImageDto]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.


        :param images: The images of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.  # noqa: E501
        :type: list[MediaStoreAPIFeaturesProductsFeatureImageDto]
        """

        self._images = images

    @property
    def space_images(self):
        """Gets the space_images of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.  # noqa: E501


        :return: The space_images of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.  # noqa: E501
        :rtype: list[MediaStoreAPIFeaturesProductsFeatureImageDto]
        """
        return self._space_images

    @space_images.setter
    def space_images(self, space_images):
        """Sets the space_images of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.


        :param space_images: The space_images of this MediaStoreAPIFeaturesProductsFeatureSearchResultDto.  # noqa: E501
        :type: list[MediaStoreAPIFeaturesProductsFeatureImageDto]
        """

        self._space_images = space_images

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
        if issubclass(MediaStoreAPIFeaturesProductsFeatureSearchResultDto, dict):
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
        if not isinstance(other, MediaStoreAPIFeaturesProductsFeatureSearchResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other