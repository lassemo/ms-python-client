# swagger_client.PrivateStoreApi

All URIs are relative to *https://mediastore.tradesolution.no/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privatestore_get**](PrivateStoreApi.md#privatestore_get) | **GET** /privatestore | Gets a list of all the product Ids the user can view.
[**privatestore_id_angle_get**](PrivateStoreApi.md#privatestore_id_angle_get) | **GET** /privatestore/{id}/{angle} | Gets the metadata available for a single image
[**privatestore_id_angle_image_get**](PrivateStoreApi.md#privatestore_id_angle_image_get) | **GET** /privatestore/{id}/{angle}/image | Gets the binary file for single image
[**privatestore_id_get**](PrivateStoreApi.md#privatestore_id_get) | **GET** /privatestore/{id} | Gets a list of images for a given GTIN id
[**privatestore_id_main_get**](PrivateStoreApi.md#privatestore_id_main_get) | **GET** /privatestore/{id}/main | Gets the metadata available for the main image of a product
[**privatestore_id_main_image_get**](PrivateStoreApi.md#privatestore_id_main_image_get) | **GET** /privatestore/{id}/main/image | Gets the binary file for the main image of a product
[**privatestore_productgroup_name_get**](PrivateStoreApi.md#privatestore_productgroup_name_get) | **GET** /privatestore/productgroup/{name} | Gets a first product for a given product group name

# **privatestore_get**
> MediaStoreAPIFeaturesProductsFeatureProductIdListResponse privatestore_get()

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
api_instance = swagger_client.PrivateStoreApi(swagger_client.ApiClient(configuration))

try:
    # Gets a list of all the product Ids the user can view.
    api_response = api_instance.privatestore_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateStoreApi->privatestore_get: %s\n" % e)
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

# **privatestore_id_angle_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse privatestore_id_angle_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, mediatype=mediatype)

Gets the metadata available for a single image

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
api_instance = swagger_client.PrivateStoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
angle = 'angle_example' # str | Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
original_only = false # bool | Return original images only, ignore campaign images. Default value: false (optional) (default to false)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the metadata available for a single image
    api_response = api_instance.privatestore_id_angle_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, mediatype=mediatype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateStoreApi->privatestore_id_angle_get: %s\n" % e)
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

# **privatestore_id_angle_image_get**
> privatestore_id_angle_image_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, size=size, mediatype=mediatype)

Gets the binary file for single image

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
api_instance = swagger_client.PrivateStoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
angle = 'angle_example' # str | Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N
variant = 0 # int | Variant number. Default value: 0 (optional) (default to 0)
specific_date = '2013-10-20T19:20:30+01:00' # datetime | Return result as they would be on a specific date. Format: YYYY-MM-DD. Default value: today (optional)
in_sales = false # bool | Return products that are currently in sales only. Default value: false (optional) (default to false)
original_only = false # bool | Return original images only, ignore campaign images. Default value: false (optional) (default to false)
size = '752' # str | Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000 and \"original\". Default value: 752 (optional) (default to 752)
mediatype = '' # str | Valid types are A for image and G for graphic illustration. Default are all mediatypes. (optional)

try:
    # Gets the binary file for single image
    api_instance.privatestore_id_angle_image_get(id, angle, variant=variant, specific_date=specific_date, in_sales=in_sales, original_only=original_only, size=size, mediatype=mediatype)
except ApiException as e:
    print("Exception when calling PrivateStoreApi->privatestore_id_angle_image_get: %s\n" % e)
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
 **size** | **str**| Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000 and \&quot;original\&quot;. Default value: 752 | [optional] [default to 752]
 **mediatype** | **str**| Valid types are A for image and G for graphic illustration. Default are all mediatypes. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **privatestore_id_get**
> MediaStoreAPIFeaturesProductsFeatureProductResponse privatestore_id_get(id, product_group_name=product_group_name)

Gets a list of images for a given GTIN id

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
api_instance = swagger_client.PrivateStoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
product_group_name = 'product_group_name_example' # str | Lookup first product with the product group name if GTIN fails (optional)

try:
    # Gets a list of images for a given GTIN id
    api_response = api_instance.privatestore_id_get(id, product_group_name=product_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateStoreApi->privatestore_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **product_group_name** | **str**| Lookup first product with the product group name if GTIN fails | [optional] 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureProductResponse**](MediaStoreAPIFeaturesProductsFeatureProductResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **privatestore_id_main_get**
> MediaStoreAPIFeaturesProductsFeatureImageResponse privatestore_id_main_get(id)

Gets the metadata available for the main image of a product

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
api_instance = swagger_client.PrivateStoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN

try:
    # Gets the metadata available for the main image of a product
    api_response = api_instance.privatestore_id_main_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateStoreApi->privatestore_id_main_get: %s\n" % e)
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

# **privatestore_id_main_image_get**
> privatestore_id_main_image_get(id, size=size)

Gets the binary file for the main image of a product

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
api_instance = swagger_client.PrivateStoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | GTIN
size = '752' # str | Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \"original\", \"originalJPG\" og \"originalPNG\". Default value: 752.               original is a .tif file with clipping path and without background.              originalJPG is with clipping path and with background.              originalPNG is without clipping path and without background. (optional) (default to 752)

try:
    # Gets the binary file for the main image of a product
    api_instance.privatestore_id_main_image_get(id, size=size)
except ApiException as e:
    print("Exception when calling PrivateStoreApi->privatestore_id_main_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| GTIN | 
 **size** | **str**| Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000, \&quot;original\&quot;, \&quot;originalJPG\&quot; og \&quot;originalPNG\&quot;. Default value: 752.               original is a .tif file with clipping path and without background.              originalJPG is with clipping path and with background.              originalPNG is without clipping path and without background. | [optional] [default to 752]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **privatestore_productgroup_name_get**
> MediaStoreAPIFeaturesProductsFeatureProductIdListResponse privatestore_productgroup_name_get(name)

Gets a first product for a given product group name

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
api_instance = swagger_client.PrivateStoreApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of the product group

try:
    # Gets a first product for a given product group name
    api_response = api_instance.privatestore_productgroup_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateStoreApi->privatestore_productgroup_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the product group | 

### Return type

[**MediaStoreAPIFeaturesProductsFeatureProductIdListResponse**](MediaStoreAPIFeaturesProductsFeatureProductIdListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

