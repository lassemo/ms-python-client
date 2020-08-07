# MediaStoreAPIFeaturesImageFeaturesUploadToGenericStoreRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Image file name. | 
**file_content** | **str** | Image file content.  Format: Base64 encoded byte array. | 
**title** | **str** | A Title of the image | [optional] 
**description** | **str** | A descriptive text of the image | [optional] 
**internal_id** | **str** | An internal Id for the image | [optional] 
**product_group_id** | **str** | Obsolete (use MediaGroupID).A product group/category identification | [optional] 
**product_group_name** | **str** | Obsolete (use MediaGroupName). A product group/category friendly name. This is the string that will show to users for product groups. E.g. \&quot;Banana\&quot; | [optional] 
**media_group_id** | **str** | A media group/category identification. If this field is filled it will override ProductGroupID | [optional] 
**media_group_name** | **str** | A product group/category friendly name. This is the string that will show to users for product groups. E.g. \&quot;Banana\&quot; . If this field is filled it will override any value in ProductGroupName | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

