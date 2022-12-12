
from typing import Dict, Any

def flatten_json(json: Dict[str, Any]) -> Dict[str, Any]:
    flattened_json = {}

    def flatten_helper(json: Dict[str, Any], prefix: str):
        for key, value in json.items():
            # if it's a dict, join with comma
            if isinstance(value, list):
                if isinstance(value[0], dict):
                    flatten_helper(value[0], f"{prefix}{key}.0.")
                else:
                    flattened_json[f"{prefix}{key}"] = ",".join(value)

            elif isinstance(value, dict):
                flatten_helper(value, f"{prefix}{key}.")
            else:
                flattened_json[f"{prefix}{key}"] = value

    flatten_helper(json, "")

    return flattened_json

the_json = {
  "business_status" : "OPERATIONAL",
  "geometry" : {
    "location" : {
      "lat" : 42.3512887,
      "lng" : -71.06154099999999
    },
  }
}

# the_json = """{
#          "business_status" : "OPERATIONAL",
#          "geometry" : {
#             "location" : {
#                "lat" : 42.3512887,
#                "lng" : -71.06154099999999
#             },
#             "viewport" : {
#                "northeast" : {
#                   "lat" : 42.35258582989272,
#                   "lng" : -71.06006172010727
#                },
#                "southwest" : {
#                   "lat" : 42.34988617010728,
#                   "lng" : -71.06276137989271
#                }
#             }
#          },
#          "icon" : "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
#          "icon_background_color" : "#7B9EB0",
#          "icon_mask_base_uri" : "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
#          "name" : "Z&Z Accounting Services LLC",
#          "opening_hours" : {
#             "open_now" : false
#          },
#          "photos" : [
#             {
#                "height" : 578,
              
#                "photo_reference" : "AW30NDz1t-zOngrC2BWO9ehZf9v8GkBqZupiYHD37Oq0xscEf7SzyIWhD5BD7MZbl3D7ofr26--lpG9jATDs-2SQCPXxTggoEIapvbqTb4UM1Nvo3M_nlLt5T8rv9k3YHp8f0YI0xzdxmA9xYUX4JEtpoPpUwbqB8HAGFjVfxyYZLWcJeFs8",
#                "width" : 868
#             }
#          ],
#          "place_id" : "ChIJW301Inh644kR8_KmV2hJeWU",
#          "plus_code" : {
#             "compound_code" : "9W2Q+G9 Boston, Massachusetts, USA",
#             "global_code" : "87JC9W2Q+G9"
#          },
#          "rating" : 4,
#          "reference" : "ChIJW301Inh644kR8_KmV2hJeWU",
#          "scope" : "GOOGLE",
#          "types" : [ "accounting", "finance", "point_of_interest", "establishment" ],
#          "user_ratings_total" : 5,
#          "vicinity" : "65 Harrison Ave Ste 502, Boston"
#       }"""

# import json

# the_json = json.loads(the_json)

# flattened_json = flatten_json(the_json)

# # convert flattened_json back to a json string
# flattened_json = json.dumps(flattened_json)

# print(flattened_json)  # Output: { "business_status" : "OPERATIONAL", "geometry.location.lat" : 42.3512887, "geometry.location.lng" : -71.06154099999999 }
