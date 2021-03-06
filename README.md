# Mediastore-Client
MediaStore API for MediaStore

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v2
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://mediastore.tradesolution.no/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CDNApi* | [**cdn_purgeurls_post**](docs/CDNApi.md#cdn_purgeurls_post) | **POST** /cdn/purgeurls | Post a list of strings to purged from the CDN.  Returns an estimate for how long it takes to do the purge operation.
*ExternalTaskApi* | [**external_task_get_image_medie_id_get**](docs/ExternalTaskApi.md#external_task_get_image_medie_id_get) | **GET** /ExternalTask/getImage/{medieID} | 
*ExternalTaskApi* | [**external_task_get_images_get**](docs/ExternalTaskApi.md#external_task_get_images_get) | **GET** /ExternalTask/getImages | 
*ExternalTaskApi* | [**external_task_get_images_order_number_get**](docs/ExternalTaskApi.md#external_task_get_images_order_number_get) | **GET** /ExternalTask/getImages/{orderNumber} | 
*ExternalTaskApi* | [**external_task_images_fetched_post**](docs/ExternalTaskApi.md#external_task_images_fetched_post) | **POST** /ExternalTask/imagesFetched | 
*ExternalTaskApi* | [**external_task_order_complete_order_number_post**](docs/ExternalTaskApi.md#external_task_order_complete_order_number_post) | **POST** /ExternalTask/orderComplete/{orderNumber} | 
*GenericStoreApi* | [**genericstore_id_get**](docs/GenericStoreApi.md#genericstore_id_get) | **GET** /genericstore/{id} | Gets a list of images for a given id (internalID, mediaGroupID or mediaGroupName)
*GenericStoreApi* | [**genericstore_id_image_get**](docs/GenericStoreApi.md#genericstore_id_image_get) | **GET** /genericstore/{id}/image | Gets the binary file for single image.
*GenericStoreApi* | [**genericstore_internalid_id_get**](docs/GenericStoreApi.md#genericstore_internalid_id_get) | **GET** /genericstore/internalid/{id} | Gets a list of images for a given internal id
*GenericStoreApi* | [**genericstore_mediagroup_id_get**](docs/GenericStoreApi.md#genericstore_mediagroup_id_get) | **GET** /genericstore/mediagroup/{id} | Gets a list of images for a given media group id
*GenericStoreApi* | [**genericstore_mediagroupname_name_get**](docs/GenericStoreApi.md#genericstore_mediagroupname_name_get) | **GET** /genericstore/mediagroupname/{name} | Gets a list of images for a given media group name
*GenericStoreApi* | [**genericstore_productgroup_id_get**](docs/GenericStoreApi.md#genericstore_productgroup_id_get) | **GET** /genericstore/productgroup/{id} | Obsolete (use /genericstore/mediagroup/id). Gets a list of images for a given product group id
*GenericStoreApi* | [**genericstore_productgroupname_name_get**](docs/GenericStoreApi.md#genericstore_productgroupname_name_get) | **GET** /genericstore/productgroupname/{name} | Obsolete (use /genericstore/mediagroupname). Gets a list of images for a given product group name
*ImageApi* | [**image_upload_put**](docs/ImageApi.md#image_upload_put) | **PUT** /image/upload | Upload an image to MediaStore.
*ImageApi* | [**image_upload_to_genericstore_put**](docs/ImageApi.md#image_upload_to_genericstore_put) | **PUT** /image/uploadToGenericstore | Uploads an image to the users generic store.
*ImageApi* | [**image_upload_to_privatestore_put**](docs/ImageApi.md#image_upload_to_privatestore_put) | **PUT** /image/uploadToPrivatestore | Upload an image to users private store.
*PrivateStoreApi* | [**privatestore_get**](docs/PrivateStoreApi.md#privatestore_get) | **GET** /privatestore | Gets a list of all the product Ids the user can view.
*PrivateStoreApi* | [**privatestore_id_angle_get**](docs/PrivateStoreApi.md#privatestore_id_angle_get) | **GET** /privatestore/{id}/{angle} | Gets the metadata available for a single image
*PrivateStoreApi* | [**privatestore_id_angle_image_get**](docs/PrivateStoreApi.md#privatestore_id_angle_image_get) | **GET** /privatestore/{id}/{angle}/image | Gets the binary file for single image
*PrivateStoreApi* | [**privatestore_id_get**](docs/PrivateStoreApi.md#privatestore_id_get) | **GET** /privatestore/{id} | Gets a list of images for a given GTIN id
*PrivateStoreApi* | [**privatestore_id_main_get**](docs/PrivateStoreApi.md#privatestore_id_main_get) | **GET** /privatestore/{id}/main | Gets the metadata available for the main image of a product
*PrivateStoreApi* | [**privatestore_id_main_image_get**](docs/PrivateStoreApi.md#privatestore_id_main_image_get) | **GET** /privatestore/{id}/main/image | Gets the binary file for the main image of a product
*PrivateStoreApi* | [**privatestore_productgroup_name_get**](docs/PrivateStoreApi.md#privatestore_productgroup_name_get) | **GET** /privatestore/productgroup/{name} | Gets a first product for a given product group name
*ProductsApi* | [**products_get**](docs/ProductsApi.md#products_get) | **GET** /products | Gets a list of all the product Ids the user can view.
*ProductsApi* | [**products_getmodifiedgtins_get**](docs/ProductsApi.md#products_getmodifiedgtins_get) | **GET** /products/getmodifiedgtins | Gets a list of gtins that has been modified on given date.
*ProductsApi* | [**products_id_angle_get**](docs/ProductsApi.md#products_id_angle_get) | **GET** /products/{id}/{angle} | Gets the metadata available for a single image
*ProductsApi* | [**products_id_angle_image_get**](docs/ProductsApi.md#products_id_angle_image_get) | **GET** /products/{id}/{angle}/image | Gets the binary file for a single image
*ProductsApi* | [**products_id_badge_angle_get**](docs/ProductsApi.md#products_id_badge_angle_get) | **GET** /products/{id}/badge/{angle} | Gets the metadata available for a single badge image (Method is not supported anymore)
*ProductsApi* | [**products_id_badge_angle_image_get**](docs/ProductsApi.md#products_id_badge_angle_image_get) | **GET** /products/{id}/badge/{angle}/image | 
*ProductsApi* | [**products_id_badge_get**](docs/ProductsApi.md#products_id_badge_get) | **GET** /products/{id}/badge | Gets a list of badge images for a given id (Method is not supported anymore)
*ProductsApi* | [**products_id_badge_main_get**](docs/ProductsApi.md#products_id_badge_main_get) | **GET** /products/{id}/badge/main | Gets the metadata available for the main badge image (Method is not supported anymore)
*ProductsApi* | [**products_id_badge_main_image_get**](docs/ProductsApi.md#products_id_badge_main_image_get) | **GET** /products/{id}/badge/main/image | Gets the binary file for the main badge image of a product (Method is not supported anymore)
*ProductsApi* | [**products_id_enriched_angle_get**](docs/ProductsApi.md#products_id_enriched_angle_get) | **GET** /products/{id}/enriched/{angle} | Gets the metadata available for a single enriched image
*ProductsApi* | [**products_id_enriched_angle_image_get**](docs/ProductsApi.md#products_id_enriched_angle_image_get) | **GET** /products/{id}/enriched/{angle}/image | Gets the binary file for a single enriched image
*ProductsApi* | [**products_id_enriched_get**](docs/ProductsApi.md#products_id_enriched_get) | **GET** /products/{id}/enriched | Gets a list of enriched images for a given id
*ProductsApi* | [**products_id_enriched_main_get**](docs/ProductsApi.md#products_id_enriched_main_get) | **GET** /products/{id}/enriched/main | Gets the metadata available for the main enriched image
*ProductsApi* | [**products_id_enriched_main_image_get**](docs/ProductsApi.md#products_id_enriched_main_image_get) | **GET** /products/{id}/enriched/main/image | Gets the binary file for the main enriched image of a product
*ProductsApi* | [**products_id_foodservice_packaging_get**](docs/ProductsApi.md#products_id_foodservice_packaging_get) | **GET** /products/{id}/foodservice/{packaging} | Gets the metadata available for a servering single image
*ProductsApi* | [**products_id_foodservice_packaging_image_get**](docs/ProductsApi.md#products_id_foodservice_packaging_image_get) | **GET** /products/{id}/foodservice/{packaging}/image | Gets the binary file for a single servering image
*ProductsApi* | [**products_id_get**](docs/ProductsApi.md#products_id_get) | **GET** /products/{id} | Gets a list of images for a given id
*ProductsApi* | [**products_id_main_get**](docs/ProductsApi.md#products_id_main_get) | **GET** /products/{id}/main | Gets the metadata available for the main image of a product
*ProductsApi* | [**products_id_main_image_get**](docs/ProductsApi.md#products_id_main_image_get) | **GET** /products/{id}/main/image | Gets the binary file for the main image of a product
*ProductsApi* | [**products_id_recommended_get**](docs/ProductsApi.md#products_id_recommended_get) | **GET** /products/{id}/recommended | Gets the metadata available for the suppliers recommended image of a product. If no recommended image is set on the product, then the main image on the product will be delivered
*ProductsApi* | [**products_id_recommended_image_get**](docs/ProductsApi.md#products_id_recommended_image_get) | **GET** /products/{id}/recommended/image | Gets the binary file for the suppliers recommended image of a product. If no recommended image is set on the product, then the main image on the product will be delivered
*ProductsApi* | [**products_id_space_angle_get**](docs/ProductsApi.md#products_id_space_angle_get) | **GET** /products/{id}/space/{angle} | Gets the metadata available for a single image in space format
*ProductsApi* | [**products_id_space_angle_image_get**](docs/ProductsApi.md#products_id_space_angle_image_get) | **GET** /products/{id}/space/{angle}/image | Gets the binary file for an image in space format
*ProductsApi* | [**products_id_space_get**](docs/ProductsApi.md#products_id_space_get) | **GET** /products/{id}/space | Gets the list of the images avaliable in space format for a given id.
*ProductsApi* | [**products_id_space_main_get**](docs/ProductsApi.md#products_id_space_main_get) | **GET** /products/{id}/space/main | Gets the metadata available for the main image of a product in space format
*ProductsApi* | [**products_id_space_main_image_get**](docs/ProductsApi.md#products_id_space_main_image_get) | **GET** /products/{id}/space/main/image | Gets the binary file for the main image of a product in space format
*ProductsApi* | [**products_imageset_id_valid_from_valid_to_post**](docs/ProductsApi.md#products_imageset_id_valid_from_valid_to_post) | **POST** /products/{imagesetID}/{validFrom}/{validTo} | Change the from and to date for an imageset
*ProductsApi* | [**products_modified_get**](docs/ProductsApi.md#products_modified_get) | **GET** /products/modified | Gets a list of products that has been modified between two given dates. Both dates are inclusive.
*TokenApi* | [**products_getapitoken_get**](docs/TokenApi.md#products_getapitoken_get) | **GET** /products/getapitoken | Method that returns a CDN accesstoken for a user for all endpoints.
*TokenApi* | [**products_gettoken_get**](docs/TokenApi.md#products_gettoken_get) | **GET** /products/gettoken | Method that returns a CDN accesstoken for a user for the /products endpoint.
*TokenApi* | [**products_getuserhash_get**](docs/TokenApi.md#products_getuserhash_get) | **GET** /products/getuserhash | Get the user part of CDN-url.

## Documentation For Models

 - [MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto](docs/MediaStoreAPIFeaturesExternalTaskFeatureExternalTaskDto.md)
 - [MediaStoreAPIFeaturesGenericStoreFeaturesGenericImageDto](docs/MediaStoreAPIFeaturesGenericStoreFeaturesGenericImageDto.md)
 - [MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse](docs/MediaStoreAPIFeaturesGenericStoreFeaturesGenericStoreResponse.md)
 - [MediaStoreAPIFeaturesImageFeaturesImageUploadRequest](docs/MediaStoreAPIFeaturesImageFeaturesImageUploadRequest.md)
 - [MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest](docs/MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest.md)
 - [MediaStoreAPIFeaturesImageFeaturesUploadToPrivateStoreRequest](docs/MediaStoreAPIFeaturesImageFeaturesUploadToPrivateStoreRequest.md)
 - [MediaStoreAPIFeaturesProductsFeatureImageDto](docs/MediaStoreAPIFeaturesProductsFeatureImageDto.md)
 - [MediaStoreAPIFeaturesProductsFeatureImageResponse](docs/MediaStoreAPIFeaturesProductsFeatureImageResponse.md)
 - [MediaStoreAPIFeaturesProductsFeatureProductDto](docs/MediaStoreAPIFeaturesProductsFeatureProductDto.md)
 - [MediaStoreAPIFeaturesProductsFeatureProductIdListResponse](docs/MediaStoreAPIFeaturesProductsFeatureProductIdListResponse.md)
 - [MediaStoreAPIFeaturesProductsFeatureProductResponse](docs/MediaStoreAPIFeaturesProductsFeatureProductResponse.md)
 - [MediaStoreAPIFeaturesProductsFeatureSearchResultDto](docs/MediaStoreAPIFeaturesProductsFeatureSearchResultDto.md)
 - [MediaStoreAPIFeaturesProductsFeatureSearchResultResponse](docs/MediaStoreAPIFeaturesProductsFeatureSearchResultResponse.md)

## Documentation For Authorization


## Bearer

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://gatekeeper.tradesolution.no/connect/authorize
- **Scopes**: 
 - ****: 


## Author


