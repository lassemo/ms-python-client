# swagger_client.CDNApi

All URIs are relative to *https://mediastore.tradesolution.no/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cdn_purgeurls_post**](CDNApi.md#cdn_purgeurls_post) | **POST** /cdn/purgeurls | Post a list of strings to purged from the CDN.  Returns an estimate for how long it takes to do the purge operation.

# **cdn_purgeurls_post**
> cdn_purgeurls_post(body=body)

Post a list of strings to purged from the CDN.  Returns an estimate for how long it takes to do the purge operation.

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
api_instance = swagger_client.CDNApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | An array of full urls with query parameters to purge (optional)

try:
    # Post a list of strings to purged from the CDN.  Returns an estimate for how long it takes to do the purge operation.
    api_instance.cdn_purgeurls_post(body=body)
except ApiException as e:
    print("Exception when calling CDNApi->cdn_purgeurls_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| An array of full urls with query parameters to purge | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

