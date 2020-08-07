# swagger_client.GenericStoreApi

All URIs are relative to *https://mediastore.tradesolution.no/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**genericstore_id_get**](GenericStoreApi.md#genericstore_id_get) | **GET** /genericstore/{id} | Gets a list of images for a given id (internalID, mediaGroupID or mediaGroupName)
[**genericstore_id_image_get**](GenericStoreApi.md#genericstore_id_image_get) | **GET** /genericstore/{id}/image | Gets the binary file for single image.
[**genericstore_internalid_id_get**](GenericStoreApi.md#genericstore_internalid_id_get) | **GET** /genericstore/internalid/{id} | Gets a list of images for a given internal id
[**genericstore_mediagroup_id_get**](GenericStoreApi.md#genericstore_mediagroup_id_get) | **GET** /genericstore/mediagroup/{id} | Gets a list of images for a given media group id
[**genericstore_mediagroupname_name_get**](GenericStoreApi.md#genericstore_mediagroupname_name_get) | **GET** /genericstore/mediagroupname/{name} | Gets a list of images for a given media group name
[**genericstore_productgroup_id_get**](GenericStoreApi.md#genericstore_productgroup_id_get) | **GET** /genericstore/productgroup/{id} | Obsolete (use /genericstore/mediagroup/id). Gets a list of images for a given product group id
[**genericstore_productgroupname_name_get**](GenericStoreApi.md#genericstore_productgroupname_name_get) | **GET** /genericstore/productgroupname/{name} | Obsolete (use /genericstore/mediagroupname). Gets a list of images for a given product group name

# **genericstore_id_get**
> MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse genericstore_id_get(id)

Gets a list of images for a given id (internalID, mediaGroupID or mediaGroupName)

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
api_instance = swagger_client.GenericStoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier.

try:
    # Gets a list of images for a given id (internalID, mediaGroupID or mediaGroupName)
    api_response = api_instance.genericstore_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericStoreApi->genericstore_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier. | 

### Return type

[**MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse**](MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genericstore_id_image_get**
> genericstore_id_image_get(id, size=size)

Gets the binary file for single image.

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
api_instance = swagger_client.GenericStoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier (medieID).
size = '752' # str | Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000 and \"original\". Default value: 752 (optional) (default to 752)

try:
    # Gets the binary file for single image.
    api_instance.genericstore_id_image_get(id, size=size)
except ApiException as e:
    print("Exception when calling GenericStoreApi->genericstore_id_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier (medieID). | 
 **size** | **str**| Valid sizes are: 100, 188, 376, 752, 2000, 2400, 3000 and \&quot;original\&quot;. Default value: 752 | [optional] [default to 752]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genericstore_internalid_id_get**
> MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse genericstore_internalid_id_get(id)

Gets a list of images for a given internal id

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
api_instance = swagger_client.GenericStoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier.

try:
    # Gets a list of images for a given internal id
    api_response = api_instance.genericstore_internalid_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericStoreApi->genericstore_internalid_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier. | 

### Return type

[**MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse**](MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genericstore_mediagroup_id_get**
> MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse genericstore_mediagroup_id_get(id)

Gets a list of images for a given media group id

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
api_instance = swagger_client.GenericStoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier.

try:
    # Gets a list of images for a given media group id
    api_response = api_instance.genericstore_mediagroup_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericStoreApi->genericstore_mediagroup_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier. | 

### Return type

[**MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse**](MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genericstore_mediagroupname_name_get**
> MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse genericstore_mediagroupname_name_get(name)

Gets a list of images for a given media group name

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
api_instance = swagger_client.GenericStoreApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The product group name to search for

try:
    # Gets a list of images for a given media group name
    api_response = api_instance.genericstore_mediagroupname_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericStoreApi->genericstore_mediagroupname_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The product group name to search for | 

### Return type

[**MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse**](MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genericstore_productgroup_id_get**
> MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse genericstore_productgroup_id_get(id)

Obsolete (use /genericstore/mediagroup/id). Gets a list of images for a given product group id

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
api_instance = swagger_client.GenericStoreApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The identifier.

try:
    # Obsolete (use /genericstore/mediagroup/id). Gets a list of images for a given product group id
    api_response = api_instance.genericstore_productgroup_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericStoreApi->genericstore_productgroup_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier. | 

### Return type

[**MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse**](MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genericstore_productgroupname_name_get**
> MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse genericstore_productgroupname_name_get(name)

Obsolete (use /genericstore/mediagroupname). Gets a list of images for a given product group name

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
api_instance = swagger_client.GenericStoreApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The product group name to search for

try:
    # Obsolete (use /genericstore/mediagroupname). Gets a list of images for a given product group name
    api_response = api_instance.genericstore_productgroupname_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericStoreApi->genericstore_productgroupname_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The product group name to search for | 

### Return type

[**MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse**](MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

