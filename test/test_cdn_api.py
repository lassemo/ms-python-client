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
from swagger_client.api.cdn_api import CDNApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCDNApi(unittest.TestCase):
    """CDNApi unit test stubs"""

    def setUp(self):
        self.api = CDNApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cdn_purgeurls_post(self):
        """Test case for cdn_purgeurls_post

        Post a list of strings to purged from the CDN.  Returns an estimate for how long it takes to do the purge operation.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
