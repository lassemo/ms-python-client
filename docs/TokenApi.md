# swagger_client.TokenApi

All URIs are relative to *https://mediastore.tradesolution.no/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_getapitoken_get**](TokenApi.md#products_getapitoken_get) | **GET** /products/getapitoken | Method that returns a CDN accesstoken for a user for all endpoints.
[**products_gettoken_get**](TokenApi.md#products_gettoken_get) | **GET** /products/gettoken | Method that returns a CDN accesstoken for a user for the /products endpoint.
[**products_getuserhash_get**](TokenApi.md#products_getuserhash_get) | **GET** /products/getuserhash | Get the user part of CDN-url.

# **products_getapitoken_get**
> str products_getapitoken_get()

Method that returns a CDN accesstoken for a user for all endpoints.

<p>This operation returns an access token to be included in all requests made to the CDN. This token is provided given that the caller               is authorized to access the Tradesolution CDN.</p>  <p>The token is valid for 7 days.</p>

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
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))

try:
    # Method that returns a CDN accesstoken for a user for all endpoints.
    api_response = api_instance.products_getapitoken_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->products_getapitoken_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_gettoken_get**
> str products_gettoken_get()

Method that returns a CDN accesstoken for a user for the /products endpoint.

<p>This operation returns an access token to be included in all requests made to the CDN. This token is provided given that the caller               is authorized to access the Tradesolution CDN.</p>  <p>The token is valid for 7 days.</p>

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
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))

try:
    # Method that returns a CDN accesstoken for a user for the /products endpoint.
    api_response = api_instance.products_gettoken_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->products_gettoken_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_getuserhash_get**
> str products_getuserhash_get()

Get the user part of CDN-url.

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
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))

try:
    # Get the user part of CDN-url.
    api_response = api_instance.products_getuserhash_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->products_getuserhash_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

