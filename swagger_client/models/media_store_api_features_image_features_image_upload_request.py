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

class MediaStoreAPIFeaturesImageFeaturesImageUploadRequest(object):
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
        'gtin': 'int',
        'image_set_id': 'int',
        'epd_number': 'int',
        'available_from': 'datetime',
        'available_to': 'datetime',
        'launch_window_date': 'datetime',
        'sales_date': 'datetime',
        'angle_code': 'str',
        'media_type': 'str',
        'packaging': 'str',
        'variant': 'str',
        'campaign_from': 'datetime',
        'campaign_to': 'datetime',
        'filename': 'str',
        'file_content': 'str'
    }

    attribute_map = {
        'gtin': 'gtin',
        'image_set_id': 'imageSetID',
        'epd_number': 'epdNumber',
        'available_from': 'availableFrom',
        'available_to': 'availableTo',
        'launch_window_date': 'launchWindowDate',
        'sales_date': 'salesDate',
        'angle_code': 'angleCode',
        'media_type': 'mediaType',
        'packaging': 'packaging',
        'variant': 'variant',
        'campaign_from': 'campaignFrom',
        'campaign_to': 'campaignTo',
        'filename': 'filename',
        'file_content': 'fileContent'
    }

    def __init__(self, gtin=None, image_set_id=None, epd_number=None, available_from=None, available_to=None, launch_window_date=None, sales_date=None, angle_code=None, media_type=None, packaging=None, variant=None, campaign_from=None, campaign_to=None, filename=None, file_content=None):  # noqa: E501
        """MediaStoreAPIFeaturesImageFeaturesImageUploadRequest - a model defined in Swagger"""  # noqa: E501
        self._gtin = None
        self._image_set_id = None
        self._epd_number = None
        self._available_from = None
        self._available_to = None
        self._launch_window_date = None
        self._sales_date = None
        self._angle_code = None
        self._media_type = None
        self._packaging = None
        self._variant = None
        self._campaign_from = None
        self._campaign_to = None
        self._filename = None
        self._file_content = None
        self.discriminator = None
        self.gtin = gtin
        if image_set_id is not None:
            self.image_set_id = image_set_id
        if epd_number is not None:
            self.epd_number = epd_number
        if available_from is not None:
            self.available_from = available_from
        if available_to is not None:
            self.available_to = available_to
        if launch_window_date is not None:
            self.launch_window_date = launch_window_date
        if sales_date is not None:
            self.sales_date = sales_date
        self.angle_code = angle_code
        if media_type is not None:
            self.media_type = media_type
        if packaging is not None:
            self.packaging = packaging
        if variant is not None:
            self.variant = variant
        if campaign_from is not None:
            self.campaign_from = campaign_from
        if campaign_to is not None:
            self.campaign_to = campaign_to
        self.filename = filename
        self.file_content = file_content

    @property
    def gtin(self):
        """Gets the gtin of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        Global Trade Item Number  # noqa: E501

        :return: The gtin of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: int
        """
        return self._gtin

    @gtin.setter
    def gtin(self, gtin):
        """Sets the gtin of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        Global Trade Item Number  # noqa: E501

        :param gtin: The gtin of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: int
        """
        if gtin is None:
            raise ValueError("Invalid value for `gtin`, must not be `None`")  # noqa: E501

        self._gtin = gtin

    @property
    def image_set_id(self):
        """Gets the image_set_id of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        Imageset ID. Needs to be set if you want to upload the image to an existing imageset  # noqa: E501

        :return: The image_set_id of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: int
        """
        return self._image_set_id

    @image_set_id.setter
    def image_set_id(self, image_set_id):
        """Sets the image_set_id of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        Imageset ID. Needs to be set if you want to upload the image to an existing imageset  # noqa: E501

        :param image_set_id: The image_set_id of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: int
        """

        self._image_set_id = image_set_id

    @property
    def epd_number(self):
        """Gets the epd_number of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        Number/ID in the EPD database.  # noqa: E501

        :return: The epd_number of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: int
        """
        return self._epd_number

    @epd_number.setter
    def epd_number(self, epd_number):
        """Sets the epd_number of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        Number/ID in the EPD database.  # noqa: E501

        :param epd_number: The epd_number of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: int
        """

        self._epd_number = epd_number

    @property
    def available_from(self):
        """Gets the available_from of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        The date for when this product should be available in Mediastore.  Format: YYYY-MM-DD.  Default: Two days from now.  # noqa: E501

        :return: The available_from of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._available_from

    @available_from.setter
    def available_from(self, available_from):
        """Sets the available_from of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        The date for when this product should be available in Mediastore.  Format: YYYY-MM-DD.  Default: Two days from now.  # noqa: E501

        :param available_from: The available_from of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: datetime
        """

        self._available_from = available_from

    @property
    def available_to(self):
        """Gets the available_to of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        The date for when this product should no longer be available in Mediastore.  Format: YYYY-MM-DD.  Default: No end date.  # noqa: E501

        :return: The available_to of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._available_to

    @available_to.setter
    def available_to(self, available_to):
        """Sets the available_to of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        The date for when this product should no longer be available in Mediastore.  Format: YYYY-MM-DD.  Default: No end date.  # noqa: E501

        :param available_to: The available_to of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: datetime
        """

        self._available_to = available_to

    @property
    def launch_window_date(self):
        """Gets the launch_window_date of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        The date for the Launch Window.  Format: YYYY-MM-DD.  Default: no date and no launch window specified.  # noqa: E501

        :return: The launch_window_date of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._launch_window_date

    @launch_window_date.setter
    def launch_window_date(self, launch_window_date):
        """Sets the launch_window_date of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        The date for the Launch Window.  Format: YYYY-MM-DD.  Default: no date and no launch window specified.  # noqa: E501

        :param launch_window_date: The launch_window_date of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: datetime
        """

        self._launch_window_date = launch_window_date

    @property
    def sales_date(self):
        """Gets the sales_date of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        The date for when the product is available for sales.  Default: Two days from now.  # noqa: E501

        :return: The sales_date of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._sales_date

    @sales_date.setter
    def sales_date(self, sales_date):
        """Sets the sales_date of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        The date for when the product is available for sales.  Default: Two days from now.  # noqa: E501

        :param sales_date: The sales_date of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: datetime
        """

        self._sales_date = sales_date

    @property
    def angle_code(self):
        """Gets the angle_code of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        The angle code for the image.  Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N  # noqa: E501

        :return: The angle_code of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._angle_code

    @angle_code.setter
    def angle_code(self, angle_code):
        """Sets the angle_code of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        The angle code for the image.  Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N  # noqa: E501

        :param angle_code: The angle_code of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: str
        """
        if angle_code is None:
            raise ValueError("Invalid value for `angle_code`, must not be `None`")  # noqa: E501

        self._angle_code = angle_code

    @property
    def media_type(self):
        """Gets the media_type of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        Media type. \"A\" for photo, \"G\" for graphic. Other types are not yet supported.  Default: A  # noqa: E501

        :return: The media_type of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        Media type. \"A\" for photo, \"G\" for graphic. Other types are not yet supported.  Default: A  # noqa: E501

        :param media_type: The media_type of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def packaging(self):
        """Gets the packaging of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        Packaging type. \"1\" for in packaging. Other types are not yet supported.  Default: 1  # noqa: E501

        :return: The packaging of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._packaging

    @packaging.setter
    def packaging(self, packaging):
        """Sets the packaging of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        Packaging type. \"1\" for in packaging. Other types are not yet supported.  Default: 1  # noqa: E501

        :param packaging: The packaging of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: str
        """

        self._packaging = packaging

    @property
    def variant(self):
        """Gets the variant of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        The variant number, if any. Default: 0 (base variant).  # noqa: E501

        :return: The variant of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """Sets the variant of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        The variant number, if any. Default: 0 (base variant).  # noqa: E501

        :param variant: The variant of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: str
        """

        self._variant = variant

    @property
    def campaign_from(self):
        """Gets the campaign_from of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        Campaign from date.  Must be specified if CampaignTo is.  Format: YYYY-MM-DD.  Default: Empty / no campaign.  # noqa: E501

        :return: The campaign_from of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._campaign_from

    @campaign_from.setter
    def campaign_from(self, campaign_from):
        """Sets the campaign_from of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        Campaign from date.  Must be specified if CampaignTo is.  Format: YYYY-MM-DD.  Default: Empty / no campaign.  # noqa: E501

        :param campaign_from: The campaign_from of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: datetime
        """

        self._campaign_from = campaign_from

    @property
    def campaign_to(self):
        """Gets the campaign_to of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        Campaign to date.  Must be specified if CampaignFrom is.  Format: YYYY-MM-DD.  Default: Empty / no campaign.  # noqa: E501

        :return: The campaign_to of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._campaign_to

    @campaign_to.setter
    def campaign_to(self, campaign_to):
        """Sets the campaign_to of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        Campaign to date.  Must be specified if CampaignFrom is.  Format: YYYY-MM-DD.  Default: Empty / no campaign.  # noqa: E501

        :param campaign_to: The campaign_to of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: datetime
        """

        self._campaign_to = campaign_to

    @property
    def filename(self):
        """Gets the filename of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        Image file name.  # noqa: E501

        :return: The filename of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        Image file name.  # noqa: E501

        :param filename: The filename of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def file_content(self):
        """Gets the file_content of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501

        Image file content.  Format: Base64 encoded byte array.  # noqa: E501

        :return: The file_content of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_content

    @file_content.setter
    def file_content(self, file_content):
        """Sets the file_content of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.

        Image file content.  Format: Base64 encoded byte array.  # noqa: E501

        :param file_content: The file_content of this MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.  # noqa: E501
        :type: str
        """
        if file_content is None:
            raise ValueError("Invalid value for `file_content`, must not be `None`")  # noqa: E501

        self._file_content = file_content

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
        if issubclass(MediaStoreAPIFeaturesImageFeaturesImageUploadRequest, dict):
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
        if not isinstance(other, MediaStoreAPIFeaturesImageFeaturesImageUploadRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
