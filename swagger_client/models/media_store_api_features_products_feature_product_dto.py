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

class MediaStoreAPIFeaturesProductsFeatureProductDto(object):
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
        'id': 'str',
        'package_format': 'str',
        'is_closed': 'bool',
        'product_name': 'str',
        'title': 'str',
        'trademark_text': 'str',
        'trademark_other_text': 'str',
        'package_level': 'str',
        'gtin_f_pak': 'str',
        'gtin_d_pak': 'str',
        'supplier_gln': 'str',
        'supplier': 'str',
        'is_food_service': 'bool',
        'sales_text': 'str',
        'epd_numbers': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'package_format': 'packageFormat',
        'is_closed': 'isClosed',
        'product_name': 'productName',
        'title': 'title',
        'trademark_text': 'trademarkText',
        'trademark_other_text': 'trademarkOtherText',
        'package_level': 'packageLevel',
        'gtin_f_pak': 'gtinFPak',
        'gtin_d_pak': 'gtinDPak',
        'supplier_gln': 'supplierGln',
        'supplier': 'supplier',
        'is_food_service': 'isFoodService',
        'sales_text': 'salesText',
        'epd_numbers': 'epdNumbers'
    }

    def __init__(self, id=None, package_format=None, is_closed=None, product_name='', title='', trademark_text='', trademark_other_text='', package_level='', gtin_f_pak='', gtin_d_pak='', supplier_gln='', supplier='', is_food_service=None, sales_text='', epd_numbers=None):  # noqa: E501
        """MediaStoreAPIFeaturesProductsFeatureProductDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._package_format = None
        self._is_closed = None
        self._product_name = None
        self._title = None
        self._trademark_text = None
        self._trademark_other_text = None
        self._package_level = None
        self._gtin_f_pak = None
        self._gtin_d_pak = None
        self._supplier_gln = None
        self._supplier = None
        self._is_food_service = None
        self._sales_text = None
        self._epd_numbers = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if package_format is not None:
            self.package_format = package_format
        if is_closed is not None:
            self.is_closed = is_closed
        if product_name is not None:
            self.product_name = product_name
        if title is not None:
            self.title = title
        if trademark_text is not None:
            self.trademark_text = trademark_text
        if trademark_other_text is not None:
            self.trademark_other_text = trademark_other_text
        if package_level is not None:
            self.package_level = package_level
        if gtin_f_pak is not None:
            self.gtin_f_pak = gtin_f_pak
        if gtin_d_pak is not None:
            self.gtin_d_pak = gtin_d_pak
        if supplier_gln is not None:
            self.supplier_gln = supplier_gln
        if supplier is not None:
            self.supplier = supplier
        if is_food_service is not None:
            self.is_food_service = is_food_service
        if sales_text is not None:
            self.sales_text = sales_text
        if epd_numbers is not None:
            self.epd_numbers = epd_numbers

    @property
    def id(self):
        """Gets the id of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501

        ImageId; GTIN  # noqa: E501

        :return: The id of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MediaStoreAPIFeaturesProductsFeatureProductDto.

        ImageId; GTIN  # noqa: E501

        :param id: The id of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def package_format(self):
        """Gets the package_format of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501

        Gets or sets the package format.  # noqa: E501

        :return: The package_format of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._package_format

    @package_format.setter
    def package_format(self, package_format):
        """Sets the package_format of this MediaStoreAPIFeaturesProductsFeatureProductDto.

        Gets or sets the package format.  # noqa: E501

        :param package_format: The package_format of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._package_format = package_format

    @property
    def is_closed(self):
        """Gets the is_closed of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The is_closed of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """Sets the is_closed of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param is_closed: The is_closed of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: bool
        """

        self._is_closed = is_closed

    @property
    def product_name(self):
        """Gets the product_name of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The product_name of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param product_name: The product_name of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def title(self):
        """Gets the title of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The title of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param title: The title of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def trademark_text(self):
        """Gets the trademark_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The trademark_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._trademark_text

    @trademark_text.setter
    def trademark_text(self, trademark_text):
        """Sets the trademark_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param trademark_text: The trademark_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._trademark_text = trademark_text

    @property
    def trademark_other_text(self):
        """Gets the trademark_other_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The trademark_other_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._trademark_other_text

    @trademark_other_text.setter
    def trademark_other_text(self, trademark_other_text):
        """Sets the trademark_other_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param trademark_other_text: The trademark_other_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._trademark_other_text = trademark_other_text

    @property
    def package_level(self):
        """Gets the package_level of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The package_level of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._package_level

    @package_level.setter
    def package_level(self, package_level):
        """Sets the package_level of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param package_level: The package_level of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._package_level = package_level

    @property
    def gtin_f_pak(self):
        """Gets the gtin_f_pak of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The gtin_f_pak of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._gtin_f_pak

    @gtin_f_pak.setter
    def gtin_f_pak(self, gtin_f_pak):
        """Sets the gtin_f_pak of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param gtin_f_pak: The gtin_f_pak of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._gtin_f_pak = gtin_f_pak

    @property
    def gtin_d_pak(self):
        """Gets the gtin_d_pak of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The gtin_d_pak of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._gtin_d_pak

    @gtin_d_pak.setter
    def gtin_d_pak(self, gtin_d_pak):
        """Sets the gtin_d_pak of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param gtin_d_pak: The gtin_d_pak of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._gtin_d_pak = gtin_d_pak

    @property
    def supplier_gln(self):
        """Gets the supplier_gln of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The supplier_gln of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._supplier_gln

    @supplier_gln.setter
    def supplier_gln(self, supplier_gln):
        """Sets the supplier_gln of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param supplier_gln: The supplier_gln of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._supplier_gln = supplier_gln

    @property
    def supplier(self):
        """Gets the supplier of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The supplier of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param supplier: The supplier of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._supplier = supplier

    @property
    def is_food_service(self):
        """Gets the is_food_service of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The is_food_service of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_food_service

    @is_food_service.setter
    def is_food_service(self, is_food_service):
        """Sets the is_food_service of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param is_food_service: The is_food_service of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: bool
        """

        self._is_food_service = is_food_service

    @property
    def sales_text(self):
        """Gets the sales_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501


        :return: The sales_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: str
        """
        return self._sales_text

    @sales_text.setter
    def sales_text(self, sales_text):
        """Sets the sales_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.


        :param sales_text: The sales_text of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: str
        """

        self._sales_text = sales_text

    @property
    def epd_numbers(self):
        """Gets the epd_numbers of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501

        A list of EPD numbers that the Id/GTIN is a part of.  # noqa: E501

        :return: The epd_numbers of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._epd_numbers

    @epd_numbers.setter
    def epd_numbers(self, epd_numbers):
        """Sets the epd_numbers of this MediaStoreAPIFeaturesProductsFeatureProductDto.

        A list of EPD numbers that the Id/GTIN is a part of.  # noqa: E501

        :param epd_numbers: The epd_numbers of this MediaStoreAPIFeaturesProductsFeatureProductDto.  # noqa: E501
        :type: list[int]
        """

        self._epd_numbers = epd_numbers

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
        if issubclass(MediaStoreAPIFeaturesProductsFeatureProductDto, dict):
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
        if not isinstance(other, MediaStoreAPIFeaturesProductsFeatureProductDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
