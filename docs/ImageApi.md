# swagger_client.ImageApi

All URIs are relative to *https://mediastore.tradesolution.no/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_upload_put**](ImageApi.md#image_upload_put) | **PUT** /image/upload | Upload an image to MediaStore.
[**image_upload_to_genericstore_put**](ImageApi.md#image_upload_to_genericstore_put) | **PUT** /image/uploadToGenericstore | Uploads an image to the users generic store.
[**image_upload_to_privatestore_put**](ImageApi.md#image_upload_to_privatestore_put) | **PUT** /image/uploadToPrivatestore | Upload an image to users private store.

# **image_upload_put**
> image_upload_put(body=body)

Upload an image to MediaStore.

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
api_instance = swagger_client.ImageApi(swagger_client.ApiClient(configuration))
body = swagger_client.MediaStoreAPIFeaturesImageFeaturesImageUploadRequest() # MediaStoreAPIFeaturesImageFeaturesImageUploadRequest | The image data and metadata. (optional)

try:
    # Upload an image to MediaStore.
    api_instance.image_upload_put(body=body)
except ApiException as e:
    print("Exception when calling ImageApi->image_upload_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaStoreAPIFeaturesImageFeaturesImageUploadRequest**](MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.md)| The image data and metadata. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_upload_to_genericstore_put**
> image_upload_to_genericstore_put(body=body)

Uploads an image to the users generic store.

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
api_instance = swagger_client.ImageApi(swagger_client.ApiClient(configuration))
body = swagger_client.MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest() # MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest | The image data and metadata. (optional)

try:
    # Uploads an image to the users generic store.
    api_instance.image_upload_to_genericstore_put(body=body)
except ApiException as e:
    print("Exception when calling ImageApi->image_upload_to_genericstore_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest**](MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.md)| The image data and metadata. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_upload_to_privatestore_put**
> image_upload_to_privatestore_put(body=body)

Upload an image to users private store.

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
api_instance = swagger_client.ImageApi(swagger_client.ApiClient(configuration))
body = swagger_client.MediaStoreAPIFeaturesImageFeaturesUploadToPrivateStoreRequest() # MediaStoreAPIFeaturesImageFeaturesUploadToPrivateStoreRequest | The image data and metadata. (optional)

try:
    # Upload an image to users private store.
    api_instance.image_upload_to_privatestore_put(body=body)
except ApiException as e:
    print("Exception when calling ImageApi->image_upload_to_privatestore_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaStoreAPIFeaturesImageFeaturesUploadToPrivateStoreRequest**](MediaStoreAPIFeaturesImageFeaturesUploadToPrivateStoreRequest.md)| The image data and metadata. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

