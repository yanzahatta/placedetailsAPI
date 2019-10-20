# Place Details API

this API can be used to search place details from a query using Google Maps API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. You can use this endpoint to access the API.

### Prerequisites
You will need [Google Maps API Key](https://console.cloud.google.com/apis/). 

### Endpoint

Get Place's Details
```
/search?key="YOUR_API_KEY"&query="PLACE_NAME"
```

Get Place's Google Maps URL
```
/url?key="YOUR_API_KEY"&query="PLACE_NAME"
```

Get Place's Address
```
/address?key="YOUR_API_KEY"&query="PLACE_NAME"
```

Get Place's Geometry
```
/geometry?key="YOUR_API_KEY"&query="PLACE_NAME"
```
