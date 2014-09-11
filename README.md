## Liverpool CityBike API (unofficial)

[![Build Status](https://travis-ci.org/paulfurley/liverpool-city-bike-api.svg?branch=master)](https://travis-ci.org/paulfurley/liverpool-city-bike-api)

Liverpool CityBike is a marvellous bike-hiring scheme.

The website displays the realtime locations of bikes in the city.

Unfortunately it's not what you'd call "mobile optimised" (112 requests / 1.3MB
to load the map) so it is basically unusable on a mobile data connection.

This is an attempt to build a realtime API that others can build against in
the hope that we can build an improved mobile website and native Android &
iPhone apps

## API example

[http://citybike-api.paulfurley.com/1/locations.json](http://citybike-api.paulfurley.com/1/locations.json)
```
{
  "lastRefreshed": "2014-06-10T10:30:00Z",
  "lastChanged": "2014-06-10T10:17:13Z",
  "locations": [{
      "locationName": "Pier Head Ferry Terminal",
      "latitude": 53.4051319444,
      "longitude": -2.9971558333,
      "availableBikes": 3,
      "availableLocks": 7
  }]
}
```
