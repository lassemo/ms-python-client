# swagger_client.ExternalTaskApi

All URIs are relative to *https://mediastore.tradesolution.no/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_task_get_image_medie_id_get**](ExternalTaskApi.md#external_task_get_image_medie_id_get) | **GET** /ExternalTask/getImage/{medieID} | 
[**external_task_get_images_get**](ExternalTaskApi.md#external_task_get_images_get) | **GET** /ExternalTask/getImages | 
[**external_task_get_images_order_number_get**](ExternalTaskApi.md#external_task_get_images_order_number_get) | **GET** /ExternalTask/getImages/{orderNumber} | 
[**external_task_images_fetched_post**](ExternalTaskApi.md#external_task_images_fetched_post) | **POST** /ExternalTask/imagesFetched | 
[**external_task_order_complete_order_number_post**](ExternalTaskApi.md#external_task_order_complete_order_number_post) | **POST** /ExternalTask/orderComplete/{orderNumber} | 

# **external_task_get_image_medie_id_get**
> MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto external_task_get_image_medie_id_get(medie_id)



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
api_instance = swagger_client.ExternalTaskApi(swagger_client.ApiClient(configuration))
medie_id = 789 # int | 

try:
    api_response = api_instance.external_task_get_image_medie_id_get(medie_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalTaskApi->external_task_get_image_medie_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **medie_id** | **int**|  | 

### Return type

[**MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto**](MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_task_get_images_get**
> list[MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto] external_task_get_images_get()



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
api_instance = swagger_client.ExternalTaskApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.external_task_get_images_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalTaskApi->external_task_get_images_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto]**](MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_task_get_images_order_number_get**
> list[MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto] external_task_get_images_order_number_get(order_number)



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
api_instance = swagger_client.ExternalTaskApi(swagger_client.ApiClient(configuration))
order_number = 56 # int | 

try:
    api_response = api_instance.external_task_get_images_order_number_get(order_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalTaskApi->external_task_get_images_order_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_number** | **int**|  | 

### Return type

[**list[MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto]**](MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_task_images_fetched_post**
> external_task_images_fetched_post(body=body)



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
api_instance = swagger_client.ExternalTaskApi(swagger_client.ApiClient(configuration))
body = [56] # list[int] |  (optional)

try:
    api_instance.external_task_images_fetched_post(body=body)
except ApiException as e:
    print("Exception when calling ExternalTaskApi->external_task_images_fetched_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_task_order_complete_order_number_post**
> external_task_order_complete_order_number_post(order_number)



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
api_instance = swagger_client.ExternalTaskApi(swagger_client.ApiClient(configuration))
order_number = 56 # int | 

try:
    api_instance.external_task_order_complete_order_number_post(order_number)
except ApiException as e:
    print("Exception when calling ExternalTaskApi->external_task_order_complete_order_number_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_number** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

