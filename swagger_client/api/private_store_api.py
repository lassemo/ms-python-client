# coding: utf-8

"""
    MediaStore API

    MediaStore API for MediaStore  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PrivateStoreApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def privatestore_get(self, **kwargs):  # noqa: E501
        """Gets a list of all the product Ids the user can view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MediaStoreAPIFeaturesProductsFeatureProductIdListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.privatestore_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.privatestore_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def privatestore_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of all the product Ids the user can view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MediaStoreAPIFeaturesProductsFeatureProductIdListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method privatestore_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/privatestore', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MediaStoreAPIFeaturesProductsFeatureProductIdListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def privatestore_id_angle_get(self, id, angle, **kwargs):  # noqa: E501
        """Gets the metadata available for a single image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_id_angle_get(id, angle, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: GTIN (required)
        :param str angle: Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N (required)
        :param int variant: Variant number. Default value: 0
        :param datetime specific_date: Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today
        :param bool in_sales: Return products that are currently in sales only. Default value: false
        :param bool original_only: Return original images only, ignore campaign images. Default value: false
        :param str mediatype: Valid types are A for image and G for graphic illustration. Default are all mediatypes.
        :return: MediaStoreAPIFeaturesProductsFeatureImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.privatestore_id_angle_get_with_http_info(id, angle, **kwargs)  # noqa: E501
        else:
            (data) = self.privatestore_id_angle_get_with_http_info(id, angle, **kwargs)  # noqa: E501
            return data

    def privatestore_id_angle_get_with_http_info(self, id, angle, **kwargs):  # noqa: E501
        """Gets the metadata available for a single image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_id_angle_get_with_http_info(id, angle, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: GTIN (required)
        :param str angle: Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N (required)
        :param int variant: Variant number. Default value: 0
        :param datetime specific_date: Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today
        :param bool in_sales: Return products that are currently in sales only. Default value: false
        :param bool original_only: Return original images only, ignore campaign images. Default value: false
        :param str mediatype: Valid types are A for image and G for graphic illustration. Default are all mediatypes.
        :return: MediaStoreAPIFeaturesProductsFeatureImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'angle', 'variant', 'specific_date', 'in_sales', 'original_only', 'mediatype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method privatestore_id_angle_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `privatestore_id_angle_get`")  # noqa: E501
        # verify the required parameter 'angle' is set
        if ('angle' not in params or
                params['angle'] is None):
            raise ValueError("Missing the required parameter `angle` when calling `privatestore_id_angle_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'angle' in params:
            path_params['angle'] = params['angle']  # noqa: E501

        query_params = []
        if 'variant' in params:
            query_params.append(('variant', params['variant']))  # noqa: E501
        if 'specific_date' in params:
            query_params.append(('specificDate', params['specific_date']))  # noqa: E501
        if 'in_sales' in params:
            query_params.append(('inSales', params['in_sales']))  # noqa: E501
        if 'original_only' in params:
            query_params.append(('originalOnly', params['original_only']))  # noqa: E501
        if 'mediatype' in params:
            query_params.append(('mediatype', params['mediatype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/privatestore/{id}/{angle}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MediaStoreAPIFeaturesProductsFeatureImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def privatestore_id_angle_image_get(self, id, angle, **kwargs):  # noqa: E501
        """Gets the binary file for single image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_id_angle_image_get(id, angle, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: GTIN (required)
        :param str angle: Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N (required)
        :param int variant: Variant number. Default value: 0
        :param datetime specific_date: Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today
        :param bool in_sales: Return products that are currently in sales only. Default value: false
        :param bool original_only: Return original images only, ignore campaign images. Default value: false
        :param str size: Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000 and \"original\". Default value: 752
        :param str mediatype: Valid types are A for image and G for graphic illustration. Default are all mediatypes.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.privatestore_id_angle_image_get_with_http_info(id, angle, **kwargs)  # noqa: E501
        else:
            (data) = self.privatestore_id_angle_image_get_with_http_info(id, angle, **kwargs)  # noqa: E501
            return data

    def privatestore_id_angle_image_get_with_http_info(self, id, angle, **kwargs):  # noqa: E501
        """Gets the binary file for single image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_id_angle_image_get_with_http_info(id, angle, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: GTIN (required)
        :param str angle: Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N (required)
        :param int variant: Variant number. Default value: 0
        :param datetime specific_date: Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today
        :param bool in_sales: Return products that are currently in sales only. Default value: false
        :param bool original_only: Return original images only, ignore campaign images. Default value: false
        :param str size: Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000 and \"original\". Default value: 752
        :param str mediatype: Valid types are A for image and G for graphic illustration. Default are all mediatypes.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'angle', 'variant', 'specific_date', 'in_sales', 'original_only', 'size', 'mediatype']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method privatestore_id_angle_image_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `privatestore_id_angle_image_get`")  # noqa: E501
        # verify the required parameter 'angle' is set
        if ('angle' not in params or
                params['angle'] is None):
            raise ValueError("Missing the required parameter `angle` when calling `privatestore_id_angle_image_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'angle' in params:
            path_params['angle'] = params['angle']  # noqa: E501

        query_params = []
        if 'variant' in params:
            query_params.append(('variant', params['variant']))  # noqa: E501
        if 'specific_date' in params:
            query_params.append(('specificDate', params['specific_date']))  # noqa: E501
        if 'in_sales' in params:
            query_params.append(('inSales', params['in_sales']))  # noqa: E501
        if 'original_only' in params:
            query_params.append(('originalOnly', params['original_only']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'mediatype' in params:
            query_params.append(('mediatype', params['mediatype']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/privatestore/{id}/{angle}/image', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def privatestore_id_get(self, id, **kwargs):  # noqa: E501
        """Gets a list of images for a given GTIN id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: GTIN (required)
        :param str product_group_name: Lookup first product with the product group name if GTIN fails
        :return: MediaStoreAPIFeaturesProductsFeatureProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.privatestore_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.privatestore_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def privatestore_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets a list of images for a given GTIN id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: GTIN (required)
        :param str product_group_name: Lookup first product with the product group name if GTIN fails
        :return: MediaStoreAPIFeaturesProductsFeatureProductResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'product_group_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method privatestore_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `privatestore_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'product_group_name' in params:
            query_params.append(('productGroupName', params['product_group_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/privatestore/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MediaStoreAPIFeaturesProductsFeatureProductResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def privatestore_id_main_get(self, id, **kwargs):  # noqa: E501
        """Gets the metadata available for the main image of a product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_id_main_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: GTIN (required)
        :return: MediaStoreAPIFeaturesProductsFeatureImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.privatestore_id_main_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.privatestore_id_main_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def privatestore_id_main_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets the metadata available for the main image of a product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_id_main_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: GTIN (required)
        :return: MediaStoreAPIFeaturesProductsFeatureImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method privatestore_id_main_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `privatestore_id_main_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/privatestore/{id}/main', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MediaStoreAPIFeaturesProductsFeatureImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def privatestore_id_main_image_get(self, id, **kwargs):  # noqa: E501
        """Gets the binary file for the main image of a product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_id_main_image_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: GTIN (required)
        :param str size: Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \"original\", \"originalJPG\" og \"originalPNG\". Default value: 752.               original is a .tif file with clipping path and without background.              originalJPG is with clipping path and with background.              originalPNG is without clipping path and without background.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.privatestore_id_main_image_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.privatestore_id_main_image_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def privatestore_id_main_image_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets the binary file for the main image of a product  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_id_main_image_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: GTIN (required)
        :param str size: Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \"original\", \"originalJPG\" og \"originalPNG\". Default value: 752.               original is a .tif file with clipping path and without background.              originalJPG is with clipping path and with background.              originalPNG is without clipping path and without background.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method privatestore_id_main_image_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `privatestore_id_main_image_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/privatestore/{id}/main/image', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def privatestore_productgroup_name_get(self, name, **kwargs):  # noqa: E501
        """Gets a first product for a given product group name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_productgroup_name_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the product group (required)
        :return: MediaStoreAPIFeaturesProductsFeatureProductIdListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.privatestore_productgroup_name_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.privatestore_productgroup_name_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def privatestore_productgroup_name_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """Gets a first product for a given product group name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privatestore_productgroup_name_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the product group (required)
        :return: MediaStoreAPIFeaturesProductsFeatureProductIdListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method privatestore_productgroup_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `privatestore_productgroup_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/privatestore/productgroup/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MediaStoreAPIFeaturesProductsFeatureProductIdListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
