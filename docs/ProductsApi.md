# swagger_client.ProductsApi

All URIs are relative to *https://mediastore.tradesolution.no/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_get**](ProductsApi.md#products_get) | **GET** /products | Gets a list of all the product Ids the user can view.
[**products_getmodifiedgtins_get**](ProductsApi.md#products_getmodifiedgtins_get) | **GET** /products/getmodifiedgtins | Gets a list of gtins that has been modified on given date.
[**products_id_angle_get**](ProductsApi.md#products_id_angle_get) | **GET** /products/{id}/{angle} | Gets the metadata available for a single image
[**products_id_angle_image_get**](ProductsApi.md#products_id_angle_image_get) | **GET** /products/{id}/{angle}/image | Gets the binary file for a single image
[**products_id_badge_angle_get**](ProductsApi.md#products_id_badge_angle_get) | **GET** /products/{id}/badge/{angle} | Gets the metadata available for a single badge image (Method is not supported anymore)
[**products_id_badge_angle_image_get**](ProductsApi.md#products_id_badge_angle_image_get) | **GET** /products/{id}/badge/{angle}/image | 
[**products_id_badge_get**](ProductsApi.md#products_id_badge_get) | **GET** /products/{id}/badge | Gets a list of badge images for a given id (Method is not supported anymore)
[**products_id_badge_main_get**](ProductsApi.md#products_id_badge_main_get) | **GET** /products/{id}/badge/main | Gets the metadata available for the main badge image (Method is not supported anymore)
[**products_id_badge_main_image_get**](ProductsApi.md#products_id_badge_main_image_get) | **GET** /products/{id}/badge/main/image | Gets the binary file for the main badge image of a product (Method is not supported anymore)
[**products_id_enriched_angle_get**](ProductsApi.md#products_id_enriched_angle_get) | **GET** /products/{id}/enriched/{angle} | Gets the metadata available for a single enriched image
[**products_id_enriched_angle_image_get**](ProductsApi.md#products_id_enriched_angle_image_get) | **GET** /products/{id}/enriched/{angle}/image | Gets the binary file for a single enriched image
[**products_id_enriched_get**](ProductsApi.md#products_id_enriched_get) | **GET** /products/{id}/enriched | Gets a list of enriched images for a given id
[**products_id_enriched_main_get**](ProductsApi.md#products_id_enriched_main_get) | **GET** /products/{id}/enriched/main | Gets the metadata available for the main enriched image
[**products_id_enriched_main_image_get**](ProductsApi.md#products_id_enriched_main_image_get) | **GET** /products/{id}/enriched/main/image | Gets the binary file for the main enriched image of a product
[**products_id_foodservice_packaging_get**](ProductsApi.md#products_id_foodservice_packaging_get) | **GET** /products/{id}/foodservice/{packaging} | Gets the metadata available for a servering single image
[**products_id_foodservice_packaging_image_get**](ProductsApi.md#products_id_foodservice_packaging_image_get) | **GET** /products/{id}/foodservice/{packaging}/image | Gets the binary file for a single servering image
[**products_id_get**](ProductsApi.md#products_id_get) | **GET** /products/{id} | Gets a list of images for a given id
[**products_id_main_get**](ProductsApi.md#products_id_main_get) | **GET** /products/{id}/main | Gets the metadata available for the main image of a product
[**products_id_main_image_get**](ProductsApi.md#products_id_main_image_get) | **GET** /products/{id}/main/image | Gets the binary file for the main image of a product
[**products_id_recommended_get**](ProductsApi.md#products_id_recommended_get) | **GET** /products/{id}/recommended | Gets the metadata available for the suppliers recommended image of a product. If no recommended image is set on the product, then the main image on the product will be delivered
[**products_id_recommended_image_get**](ProductsApi.md#products_id_recommended_image_get) | **GET** /products/{id}/recommended/image | Gets the binary file for the suppliers recommended image of a product. If no recommended image is set on the product, then the main image on the product will be delivered
[**products_id_space_angle_get**](ProductsApi.md#products_id_space_angle_get) | **GET** /products/{id}/space/{angle} | Gets the metadata available for a single image in space format
[**products_id_space_angle_image_get**](ProductsApi.md#products_id_space_angle_image_get) | **GET** /products/{id}/space/{angle}/image | Gets the binary file for an image in space format
[**products_id_space_get**](ProductsApi.md#products_id_space_get) | **GET** /products/{id}/space | Gets the list of the images avaliable in space format for a given id.
[**products_id_space_main_get**](ProductsApi.md#products_id_space_main_get) | **GET** /products/{id}/space/main | Gets the metadata available for the main image of a product in space format
[**products_id_space_main_image_get**](ProductsApi.md#products_id_space_main_image_get) | **GET** /products/{id}/space/main/image | Gets the binary file for the main image of a product in space format
[**products_imageset_id_valid_from_valid_to_post**](ProductsApi.md#products_imageset_id_valid_from_valid_to_post) | **POST** /products/{imagesetID}/{validFrom}/{validTo} | Change the from and to date for an imageset
[**products_modified_get**](ProductsApi.md#products_modified_get) | **GET** /products/modified | Gets a list of products that has been modified between two given dates. Both dates are inclusive.

# **products_get**
> MediaStoreAPIFeaturesProductsFeatureProductIdListResponse products_get()

Gets a list of all the product Ids the user can view.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of all the product Ids the user can view.
    api_response = api_instance.products_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MediaStoreAPIFeaturesProductsFeatureProductIdListResponse**](MediaStoreAPIFeaturesProductsFeatureProductIdListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_getmodifiedgtins_get**
> MediaStoreAPIFeaturesProductsFeatureProductIdListResponse products_getmodifiedgtins_get(_date=_date)

Gets a list of gtins that has been modified on given date.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20T19:20:30+01:00' # datetime | Format: YYYY-MM-DD. Default value: today (optional)

try:
    # Gets a list of gtins that has been modified on given date.
    api_response = api_instance.products_getmodifiedgtins_get(_date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_getmodifiedgtins_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**| Format: YYYY-MM-DD. Default value: today | [optional] 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureProductIdListResponse**](MediaStoreAPIFeaturesProductsFeatureProductIdListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_angle_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse products_id_angle_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, mediatype=mediatype)

Gets the metadata available for a single image

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/{angle}</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
angle = 'angle_example' # str | Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
original_only = false # bool | Return original images only, ignore campaign images. Default value: false (optional) (default to false)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the metadata available for a single image
    api_response = api_instance.products_id_angle_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, mediatype=mediatype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_angle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **angle** | **str**| Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N | 
 **variant** | **int**| Variant number. Default value: 0 | [optional] [default to 0]
 **specific_date** | **datetime**| Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today | [optional] 
 **in_sales** | **bool**| Return products that are currently in sales only. Default value: false | [optional] [default to false]
 **original_only** | **bool**| Return original images only, ignore campaign images. Default value: false | [optional] [default to false]
 **mediatype** | **str**| Valid types are A for image and G for graphic illustration. Default are all mediatypes. | [optional] 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureImageResponse**](MediaStoreAPIFeaturesProductsFeatureImageResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_angle_image_get**
> products_id_angle_image_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, size=size, mediatype=mediatype)

Gets the binary file for a single image

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/{angle}/image</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
angle = 'angle_example' # str | Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
original_only = false # bool | Return original images only, ignore campaign images. Default value: false (optional) (default to false)
size = '752' # str | Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \"original\", \"originalJPG\" og \"originalPNG\". Default value: 752.                original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. (optional) (default to 752)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the binary file for a single image
    api_instance.products_id_angle_image_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, size=size, mediatype=mediatype)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_angle_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **angle** | **str**| Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N | 
 **variant** | **int**| Variant number. Default value: 0 | [optional] [default to 0]
 **specific_date** | **datetime**| Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today | [optional] 
 **in_sales** | **bool**| Return products that are currently in sales only. Default value: false | [optional] [default to false]
 **original_only** | **bool**| Return original images only, ignore campaign images. Default value: false | [optional] [default to false]
 **size** | **str**| Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \&quot;original\&quot;, \&quot;originalJPG\&quot; og \&quot;originalPNG\&quot;. Default value: 752.                original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. | [optional] [default to 752]
 **mediatype** | **str**| Valid types are A for image and G for graphic illustration. Default are all mediatypes. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_badge_angle_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse products_id_badge_angle_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, mediatype=mediatype)

Gets the metadata available for a single badge image (Method is not supported anymore)

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/{angle}</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
angle = 'angle_example' # str | Valid angles: 1LZ, 1CZ, 1RZ
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the metadata available for a single badge image (Method is not supported anymore)
    api_response = api_instance.products_id_badge_angle_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, mediatype=mediatype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_badge_angle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **angle** | **str**| Valid angles: 1LZ, 1CZ, 1RZ | 
 **variant** | **int**| Variant number. Default value: 0 | [optional] [default to 0]
 **specific_date** | **datetime**| Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today | [optional] 
 **in_sales** | **bool**| Return products that are currently in sales only. Default value: false | [optional] [default to false]
 **mediatype** | **str**| Valid types are A for image and G for graphic illustration. Default are all mediatypes. | [optional] 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureImageResponse**](MediaStoreAPIFeaturesProductsFeatureImageResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_badge_angle_image_get**
> products_id_badge_angle_image_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, size=size, mediatype=mediatype)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
angle = 'angle_example' # str | 
variant = 0 # int |  (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
in_sales = false # bool |  (optional) (default to false)
original_only = false # bool |  (optional) (default to false)
size = 'size_example' # str |  (optional)
mediatype = '' # str |  (optional)

try:
    api_instance.products_id_badge_angle_image_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, size=size, mediatype=mediatype)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_badge_angle_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **angle** | **str**|  | 
 **variant** | **int**|  | [optional] [default to 0]
 **specific_date** | **datetime**|  | [optional] 
 **in_sales** | **bool**|  | [optional] [default to false]
 **original_only** | **bool**|  | [optional] [default to false]
 **size** | **str**|  | [optional] 
 **mediatype** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_badge_get**
> MediaStoreAPIFeaturesProductsFeatureProductResponse products_id_badge_get(id)

Gets a list of badge images for a given id (Method is not supported anymore)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN

try:
    # Gets a list of badge images for a given id (Method is not supported anymore)
    api_response = api_instance.products_id_badge_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_badge_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureProductResponse**](MediaStoreAPIFeaturesProductsFeatureProductResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_badge_main_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse products_id_badge_main_get(id)

Gets the metadata available for the main badge image (Method is not supported anymore)

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/main</code></p>  <p>For code examples and more details on implementation see                <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN

try:
    # Gets the metadata available for the main badge image (Method is not supported anymore)
    api_response = api_instance.products_id_badge_main_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_badge_main_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureImageResponse**](MediaStoreAPIFeaturesProductsFeatureImageResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_badge_main_image_get**
> products_id_badge_main_image_get(id, size=size)

Gets the binary file for the main badge image of a product (Method is not supported anymore)

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/main/image</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
size = '752' # str | Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \"original\", \"originalJPG\" og \"originalPNG\". Default value: 752.               original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. (optional) (default to 752)

try:
    # Gets the binary file for the main badge image of a product (Method is not supported anymore)
    api_instance.products_id_badge_main_image_get(id, size=size)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_badge_main_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **size** | **str**| Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \&quot;original\&quot;, \&quot;originalJPG\&quot; og \&quot;originalPNG\&quot;. Default value: 752.               original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. | [optional] [default to 752]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_enriched_angle_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse products_id_enriched_angle_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, mediatype=mediatype)

Gets the metadata available for a single enriched image

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/{angle}</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
angle = 'angle_example' # str | Valid angles: 1LX, 1CX, 1RX
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the metadata available for a single enriched image
    api_response = api_instance.products_id_enriched_angle_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, mediatype=mediatype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_enriched_angle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **angle** | **str**| Valid angles: 1LX, 1CX, 1RX | 
 **variant** | **int**| Variant number. Default value: 0 | [optional] [default to 0]
 **specific_date** | **datetime**| Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today | [optional] 
 **in_sales** | **bool**| Return products that are currently in sales only. Default value: false | [optional] [default to false]
 **mediatype** | **str**| Valid types are A for image and G for graphic illustration. Default are all mediatypes. | [optional] 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureImageResponse**](MediaStoreAPIFeaturesProductsFeatureImageResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_enriched_angle_image_get**
> products_id_enriched_angle_image_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, size=size, mediatype=mediatype)

Gets the binary file for a single enriched image

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/{angle}/image</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
angle = 'angle_example' # str | Valid angles: 1LX, 1CX, 1RX
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
original_only = false # bool | Return original images only, ignore campaign images. Default value: false (optional) (default to false)
size = '752' # str | Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \"original\", \"originalJPG\" og \"originalPNG\". Default value: 752.               original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. (optional) (default to 752)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the binary file for a single enriched image
    api_instance.products_id_enriched_angle_image_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, size=size, mediatype=mediatype)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_enriched_angle_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **angle** | **str**| Valid angles: 1LX, 1CX, 1RX | 
 **variant** | **int**| Variant number. Default value: 0 | [optional] [default to 0]
 **specific_date** | **datetime**| Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today | [optional] 
 **in_sales** | **bool**| Return products that are currently in sales only. Default value: false | [optional] [default to false]
 **original_only** | **bool**| Return original images only, ignore campaign images. Default value: false | [optional] [default to false]
 **size** | **str**| Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \&quot;original\&quot;, \&quot;originalJPG\&quot; og \&quot;originalPNG\&quot;. Default value: 752.               original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. | [optional] [default to 752]
 **mediatype** | **str**| Valid types are A for image and G for graphic illustration. Default are all mediatypes. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_enriched_get**
> MediaStoreAPIFeaturesProductsFeatureProductResponse products_id_enriched_get(id)

Gets a list of enriched images for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN

try:
    # Gets a list of enriched images for a given id
    api_response = api_instance.products_id_enriched_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_enriched_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureProductResponse**](MediaStoreAPIFeaturesProductsFeatureProductResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_enriched_main_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse products_id_enriched_main_get(id)

Gets the metadata available for the main enriched image

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/main</code></p>  <p>For code examples and more details on implementation see                <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN

try:
    # Gets the metadata available for the main enriched image
    api_response = api_instance.products_id_enriched_main_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_enriched_main_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureImageResponse**](MediaStoreAPIFeaturesProductsFeatureImageResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_enriched_main_image_get**
> products_id_enriched_main_image_get(id, size=size)

Gets the binary file for the main enriched image of a product

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/main/image</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
size = '752' # str | Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \"original\", \"originalJPG\" og \"originalPNG\". Default value: 752.               original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. (optional) (default to 752)

try:
    # Gets the binary file for the main enriched image of a product
    api_instance.products_id_enriched_main_image_get(id, size=size)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_enriched_main_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **size** | **str**| Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \&quot;original\&quot;, \&quot;originalJPG\&quot; og \&quot;originalPNG\&quot;. Default value: 752.               original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. | [optional] [default to 752]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_foodservice_packaging_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse products_id_foodservice_packaging_get(id, packaging, packaging_variant=packaging_variant, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, mediatype=mediatype)

Gets the metadata available for a servering single image

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/{angle}</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
packaging = 'packaging_example' # str | Valid packagings are 1, 0, B, C, G.
packaging_variant = 0 # int | Packaging Variant. Default value: 0 (optional) (default to 0)
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
original_only = false # bool | Return original images only, ignore campaign images. Default value: false (optional) (default to false)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the metadata available for a servering single image
    api_response = api_instance.products_id_foodservice_packaging_get(id, packaging, packaging_variant=packaging_variant, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, mediatype=mediatype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_foodservice_packaging_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **packaging** | **str**| Valid packagings are 1, 0, B, C, G. | 
 **packaging_variant** | **int**| Packaging Variant. Default value: 0 | [optional] [default to 0]
 **variant** | **int**| Variant number. Default value: 0 | [optional] [default to 0]
 **specific_date** | **datetime**| Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today | [optional] 
 **in_sales** | **bool**| Return products that are currently in sales only. Default value: false | [optional] [default to false]
 **original_only** | **bool**| Return original images only, ignore campaign images. Default value: false | [optional] [default to false]
 **mediatype** | **str**| Valid types are A for image and G for graphic illustration. Default are all mediatypes. | [optional] 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureImageResponse**](MediaStoreAPIFeaturesProductsFeatureImageResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_foodservice_packaging_image_get**
> products_id_foodservice_packaging_image_get(id, packaging, packaging_variant=packaging_variant, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, size=size, mediatype=mediatype)

Gets the binary file for a single servering image

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/{angle}/image</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
packaging = 'packaging_example' # str | Valid packagings are 1, 0, B, C, G.
packaging_variant = 0 # int | Packaging Variant. Default value: 0 (optional) (default to 0)
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
original_only = false # bool | Return original images only, ignore campaign images. Default value: false (optional) (default to false)
size = '752' # str | Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \"original\", \"originalJPG\" og \"originalPNG\". Default value: 752.                original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. (optional) (default to 752)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the binary file for a single servering image
    api_instance.products_id_foodservice_packaging_image_get(id, packaging, packaging_variant=packaging_variant, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, size=size, mediatype=mediatype)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_foodservice_packaging_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **packaging** | **str**| Valid packagings are 1, 0, B, C, G. | 
 **packaging_variant** | **int**| Packaging Variant. Default value: 0 | [optional] [default to 0]
 **variant** | **int**| Variant number. Default value: 0 | [optional] [default to 0]
 **specific_date** | **datetime**| Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today | [optional] 
 **in_sales** | **bool**| Return products that are currently in sales only. Default value: false | [optional] [default to false]
 **original_only** | **bool**| Return original images only, ignore campaign images. Default value: false | [optional] [default to false]
 **size** | **str**| Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \&quot;original\&quot;, \&quot;originalJPG\&quot; og \&quot;originalPNG\&quot;. Default value: 752.                original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. | [optional] [default to 752]
 **mediatype** | **str**| Valid types are A for image and G for graphic illustration. Default are all mediatypes. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_get**
> MediaStoreAPIFeaturesProductsFeatureProductResponse products_id_get(id)

Gets a list of images for a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 789 # int | GTIN

try:
    # Gets a list of images for a given id
    api_response = api_instance.products_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| GTIN | 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureProductResponse**](MediaStoreAPIFeaturesProductsFeatureProductResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_main_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse products_id_main_get(id)

Gets the metadata available for the main image of a product

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/main</code></p>  <p>For code examples and more details on implementation see                <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN

try:
    # Gets the metadata available for the main image of a product
    api_response = api_instance.products_id_main_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_main_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureImageResponse**](MediaStoreAPIFeaturesProductsFeatureImageResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_main_image_get**
> products_id_main_image_get(id, size=size, internal_id=internal_id, product_group_id=product_group_id)

Gets the binary file for the main image of a product

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/main/image</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
size = '752' # str | Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \"original\", \"originalJPG\" og \"originalPNG\". Default value: 752.                original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. (optional) (default to 752)
internal_id = 'internal_id_example' # str | Internal id for fallback to generic store (optional)
product_group_id = 'product_group_id_example' # str | Product group id for fallback to generic store (optional)

try:
    # Gets the binary file for the main image of a product
    api_instance.products_id_main_image_get(id, size=size, internal_id=internal_id, product_group_id=product_group_id)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_main_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **size** | **str**| Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \&quot;original\&quot;, \&quot;originalJPG\&quot; og \&quot;originalPNG\&quot;. Default value: 752.                original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. | [optional] [default to 752]
 **internal_id** | **str**| Internal id for fallback to generic store | [optional] 
 **product_group_id** | **str**| Product group id for fallback to generic store | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_recommended_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse products_id_recommended_get(id)

Gets the metadata available for the suppliers recommended image of a product. If no recommended image is set on the product, then the main image on the product will be delivered

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/main</code></p>  <p>For code examples and more details on implementation see                <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN

try:
    # Gets the metadata available for the suppliers recommended image of a product. If no recommended image is set on the product, then the main image on the product will be delivered
    api_response = api_instance.products_id_recommended_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_recommended_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureImageResponse**](MediaStoreAPIFeaturesProductsFeatureImageResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_recommended_image_get**
> products_id_recommended_image_get(id, size=size, internal_id=internal_id, product_group_id=product_group_id)

Gets the binary file for the suppliers recommended image of a product. If no recommended image is set on the product, then the main image on the product will be delivered

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/main/image</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
size = '752' # str | Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \"original\", \"originalJPG\" og \"originalPNG\". Default value: 752.                original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. (optional) (default to 752)
internal_id = 'internal_id_example' # str | Internal id for fallback to generic store (optional)
product_group_id = 'product_group_id_example' # str | Product group id for fallback to generic store (optional)

try:
    # Gets the binary file for the suppliers recommended image of a product. If no recommended image is set on the product, then the main image on the product will be delivered
    api_instance.products_id_recommended_image_get(id, size=size, internal_id=internal_id, product_group_id=product_group_id)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_recommended_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **size** | **str**| Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \&quot;original\&quot;, \&quot;originalJPG\&quot; og \&quot;originalPNG\&quot;. Default value: 752.                original is a .tif file with clipping path and without background.               originalJPG is with clipping path and with background.               originalPNG is without clipping path and without background. | [optional] [default to 752]
 **internal_id** | **str**| Internal id for fallback to generic store | [optional] 
 **product_group_id** | **str**| Product group id for fallback to generic store | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_space_angle_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse products_id_space_angle_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, mediatype=mediatype)

Gets the metadata available for a single image in space format

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/space/{angle}</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
angle = 'angle_example' # str | Valid space angles: 1N, 2N, 3N
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the metadata available for a single image in space format
    api_response = api_instance.products_id_space_angle_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, mediatype=mediatype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_space_angle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **angle** | **str**| Valid space angles: 1N, 2N, 3N | 
 **variant** | **int**| Variant number. Default value: 0 | [optional] [default to 0]
 **specific_date** | **datetime**| Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today | [optional] 
 **in_sales** | **bool**| Return products that are currently in sales only. Default value: false | [optional] [default to false]
 **mediatype** | **str**| Valid types are A for image and G for graphic illustration. Default are all mediatypes. | [optional] 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureImageResponse**](MediaStoreAPIFeaturesProductsFeatureImageResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_space_angle_image_get**
> products_id_space_angle_image_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, mediatype=mediatype)

Gets the binary file for an image in space format

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/space/{angle}/image</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
angle = 'angle_example' # str | Valid space angles: 1N, 2N, 3N
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the binary file for an image in space format
    api_instance.products_id_space_angle_image_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, mediatype=mediatype)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_space_angle_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **angle** | **str**| Valid space angles: 1N, 2N, 3N | 
 **variant** | **int**| Variant number. Default value: 0 | [optional] [default to 0]
 **specific_date** | **datetime**| Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today | [optional] 
 **in_sales** | **bool**| Return products that are currently in sales only. Default value: false | [optional] [default to false]
 **mediatype** | **str**| Valid types are A for image and G for graphic illustration. Default are all mediatypes. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_space_get**
> MediaStoreAPIFeaturesProductsFeatureProductResponse products_id_space_get(id)

Gets the list of the images avaliable in space format for a given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN

try:
    # Gets the list of the images avaliable in space format for a given id.
    api_response = api_instance.products_id_space_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_space_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureProductResponse**](MediaStoreAPIFeaturesProductsFeatureProductResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_space_main_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse products_id_space_main_get(id)

Gets the metadata available for the main image of a product in space format

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/space/main</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN

try:
    # Gets the metadata available for the main image of a product in space format
    api_response = api_instance.products_id_space_main_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_space_main_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureImageResponse**](MediaStoreAPIFeaturesProductsFeatureImageResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_id_space_main_image_get**
> products_id_space_main_image_get(id)

Gets the binary file for the main image of a product in space format

<p>For the CDN version of all calls, you need to first request a CDN token (See /products/gettoken) and a userHash (See /products/getUserHash)                and the URL Host needs to be https://tradesolutions.akamaized.net/api/.               The CDN operation URL looks similar to the normal API version of the operation with the exception of a hash being added to the URL.                The response object of all standard API calls returns an attribute called \"CDNUrl\" which exposes the CDN version of the call (provided that               the user has CDN access).                               The request will also need to include a few request headers; Cache-control with the value no-cache, the CDN token; \"__token__\" (from /products/gettoken), and a host header; host (with the value tradesolutions.akamaized.net).</p>  <p>CDNUrl example: <code>/products/kjlsdf231lkjdagfdfg/{id}/space/main/image</code></p>  <p>For code examples and more details on implementation see <a href=\"http://www.tradesolution.no/wp-content/uploads/2017/01/Implementation-examples-Mediastore-API-and-CDN-okt-2016.pdf\">usage examples</a>.</p>  <p></p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN

try:
    # Gets the binary file for the main image of a product in space format
    api_instance.products_id_space_main_image_get(id)
except ApiException as e:
    print("Exception when calling ProductsApi->products_id_space_main_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_imageset_id_valid_from_valid_to_post**
> products_imageset_id_valid_from_valid_to_post(imageset_id, valid_from, valid_to)

Change the from and to date for an imageset

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
imageset_id = 56 # int | 
valid_from = '2013-10-20T19:20:30+01:00' # datetime | 
valid_to = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    # Change the from and to date for an imageset
    api_instance.products_imageset_id_valid_from_valid_to_post(imageset_id, valid_from, valid_to)
except ApiException as e:
    print("Exception when calling ProductsApi->products_imageset_id_valid_from_valid_to_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageset_id** | **int**|  | 
 **valid_from** | **datetime**|  | 
 **valid_to** | **datetime**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_modified_get**
> MediaStoreAPIFeaturesProductsFeatureSearchResultResponse products_modified_get(_from=_from, to=to)

Gets a list of products that has been modified between two given dates. Both dates are inclusive.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Bearer
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ProductsApi(swagger_client.ApiClient(configuration))
_from = '2013-10-20T19:20:30+01:00' # datetime | Format: YYYY-MM-DD. Default value: today (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Format: YYYY-MM-DD. Default value: today (optional)

try:
    # Gets a list of products that has been modified between two given dates. Both dates are inclusive.
    api_response = api_instance.products_modified_get(_from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_modified_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Format: YYYY-MM-DD. Default value: today | [optional] 
 **to** | **datetime**| Format: YYYY-MM-DD. Default value: today | [optional] 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureSearchResultResponse**](MediaStoreAPIFeaturesProductsFeatureSearchResultResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

