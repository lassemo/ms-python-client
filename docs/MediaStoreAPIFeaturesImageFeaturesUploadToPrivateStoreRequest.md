# MediaStoreAPIFeaturesImageFeaturesUploadToPrivateStoreRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gtin** | **int** | Global Trade Item Number | 
**image_set_id** | **int** | Imageset ID. Needs to be set if you want to upload the image to an existing imageset | [optional] 
**epd_number** | **int** | Private EPD number/ID. OBSOLUTE. | [optional] 
**product_name** | **str** | The product name. | 
**product_properties** | **str** | The products properties. | [optional] 
**product_description** | **str** | The products descriptive text. | [optional] 
**package_level** | **str** | Package level.  Valid values are: basis, mellom1, mellom2 or pall | 
**available_from** | **datetime** | The date for when this product should be available in Mediastore.  Format: YYYY-MM-DD.  Default: Today. | [optional] 
**available_to** | **datetime** | The date for when this product should no longer be available in Mediastore.  Format: YYYY-MM-DD.  Default: No end date. | [optional] 
**launch_window_date** | **datetime** | The date for the Launch Window.  Format: YYYY-MM-DD.  Default: no date and no launch window specified. | [optional] 
**supplier** | **str** | The suppliers name. | [optional] 
**sales_date** | **datetime** | The date for when the product is available for sales.  Default: Today. | [optional] 
**angle_code** | **str** | The angle code for the image.  Valid angles: 1L, 1C, 1R, 1N, 2N, 3N, 7N, 8N, 9N | 
**media_type** | **str** | Media type. \&quot;A\&quot; for photo, \&quot;G\&quot; for graphic. Other types are not yet supported.  Default: A | [optional] 
**packaging** | **str** | Packaging type. \&quot;1\&quot; for in packaging. Other types are not yet supported.  Default: 1 | [optional] 
**variant** | **str** | The variant, if any. Default: 0 (base variant). | [optional] 
**campaign_from** | **datetime** | Campaign from date.  Must be specified if CampaignTo is.  Format: YYYY-MM-DD.  Default: Empty / no campaign. | [optional] 
**campaign_to** | **datetime** | Campaign to date.  Must be specified if CampaignFrom is.  Format: YYYY-MM-DD.  Default: Empty / no campaign. | [optional] 
**is_main_image** | **bool** | Whether this is the main image for the GTIN or not. | [optional] 
**product_group** | **str** | The product group/category for this product. | [optional] 
**product_sub_group** | **str** | The product sub group for this product. | [optional] 
**product_sub_group_level3** | **str** | The product sub sub group for this product.  Sub group level 3. | [optional] 
**filename** | **str** | Image file name. | 
**file_content** | **str** | Image file content.  Format: Base64 encoded byte array. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

