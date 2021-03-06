# coding: utf-8

"""
    MediaStore API

    MediaStore API for MediaStore  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.image_api import ImageApi  # noqa: E501
from swagger_client.rest import ApiException


class TestImageApi(unittest.TestCase):
    """ImageApi unit test stubs"""

    def setUp(self):
        self.api = ImageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_image_upload_put(self):
        """Test case for image_upload_put

        Upload an image to MediaStore.  # noqa: E501
        """
        pass

    def test_image_upload_to_genericstore_put(self):
        """Test case for image_upload_to_genericstore_put

        Uploads an image to the users generic store.  # noqa: E501
        """
        pass

    def test_image_upload_to_privatestore_put(self):
        """Test case for image_upload_to_privatestore_put

        Upload an image to users private store.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
