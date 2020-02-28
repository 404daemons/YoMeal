MongoDB Service
======

Prerequisite
------ 
Run mongod service before using this service.
https://docs.mongodb.com/manual/tutorial/manage-mongodb-processes/#start-mongod-processes


Services
------

#### URL: `/activity`

**Method:** POST

**Description:** Add the activity or activities for user.

**Payload:**
```json
{
	"items": [{
			"phone_no": 1234567890,
			"item": "food_item_1",
			"calorie": 10,
			"protein": 10,
			"sugar": 10
		},
		{
			"phone_no": 1234567890,
			"item": "food_item_2",
			"calorie": 20,
			"protein": 20,
			"sugar": 20
		},
        {
			"phone_no": 1234567890,
			"item": "food_item_N",
			"calorie": 100,
			"protein": 100,
			"sugar": 100
		}
	]
}
```

**Response:** 
```json
{
    "data": [],
    "message": "Total 3 activities added successfully.",
    "status": 200
}
```



#### URL: `/activity/<int:phone_no>`

**Method:** GET

**Description:** Get the all activities between start_date and end_date for given phone no. If date payload is not passed, it will return for all activities.  

**Request Args:**
* phone_no: int

**Payload:**

```json
{
    "start_date": "2020-01-01 15:23:45",	
    "end_date": "2020-01-05"
}
```
Date Format: `"%Y-%m-%d %H:%M:%S"` or `"%Y-%m-%d"`

**Response:** 
```json
{
    "data": "[{\"_id\": {\"$oid\": \"5e4b7462d350f079a74d5f38\"}, \"phone_no\": 2, \"item\": \"Rice\", \"calorie\": 0.0, \"protein\": 100.0, \"sugar\": 0.0, \"recorded_at\": {\"$date\": 1582003236580}}]",
    "message": "User#2 fetched 1 activities.",
    "status": 200
}
```
#### URL: `/activity/<int:phone_no>/<value>`

**Method:** GET

**Description:** Get total number of protein or calorie or sugar intake for all activity between start_date and end_date __date are optional param__ . If date param is not passed, it will return for all activities.  

**Request Args:**

* phone_no: int
* value: string (e.g. 'protein', 'calorie', 'sugar')

**Payload:**
```json
{
    "start_date": "2020-01-01 15:23:45",
    "end_date": "2020-01-05"
}
```
Date Format: `"%Y-%m-%d %H:%M:%S"` or `"%Y-%m-%d"`

**Response:**
```json
{
    "data": {
        "details": [
            {
                "_id": {
                    "day": 15,
                    "month": 2,
                    "year": 2020
                },
                "activities": [
                    {
                        "calorie": 10,
                        "item": "Apple",
                        "protein": 10,
                        "sugar": 0
                    },
                    {
                        "calorie": 10,
                        "item": "Banana",
                        "protein": 10,
                        "sugar": 0
                    }
                ],
                "count": 2,
                "food_items": [
                    "Apple",
                    "Banana"
                ],
                "total_calorie": 20,
                "total_protein": 20
            }
        ],
        "end_date": "Sun, 16 Feb 2020 23:59:59 GMT",
        "phone_no": 1
    },
    "message": "Success",
    "status": 200
}
```
