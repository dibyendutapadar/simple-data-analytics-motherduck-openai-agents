# Schema Narrative description
This table captures detailed trip-level records from High Volume For-Hire Services in New York City. Each row reflects a single ride request, covering the dispatch base, timestamps across the request to dropoff lifecycle, geographic pickup and dropoff zones, distance and duration, fare components, taxes, surcharges, tips, and driver earnings. It supports analyses of demand timing, operational delays, routing behavior, cost structure, accessibility service performance, and shared ride dynamics across large-scale rideshare operators.

# Schema description with datatypes and format notes
- hvfhs_license_num: STRING. Identifier for the licensed high volume service company responsible for the trip.
- dispatching_base_num: STRING. Base that dispatched the trip.
- originating_base_num: STRING. Base that first received the trip request.
- request_datetime: TIMESTAMP in yyyy-MM-dd HH:mm:ss. When the rider requested a trip.
- on_scene_datetime: TIMESTAMP in yyyy-MM-dd HH:mm:ss. When the driver arrived at the pickup location.
- pickup_datetime: TIMESTAMP in yyyy-MM-dd HH:mm:ss. When the passenger was picked up.
- dropoff_datetime: TIMESTAMP in yyyy-MM-dd HH:mm:ss. When the passenger was dropped off.
- PULocationID: INTEGER. TLC zone identifier where the trip began.
- DOLocationID: INTEGER. TLC zone identifier where the trip ended.
- trip_miles: DOUBLE. Distance traveled in miles.
- trip_time: INTEGER or BIGINT (seconds). Duration between pickup and dropoff.
- base_passenger_fare: DOUBLE. Core fare charged before taxes, surcharges, tolls, or tips.
- tolls: DOUBLE. Monetary tolls incurred during the trip.
- bcf: DOUBLE. Estimated carbon footprint metric for the trip.
- sales_tax: DOUBLE. Dollar value of sales tax applied to the ride.
- congestion_surcharge: DOUBLE. Congestion fee applied in designated zones.
- airport_fee: DOUBLE. Surcharge for airport pickup or dropoff.
- tips: DOUBLE. Gratuity paid by the passenger.
- driver_pay: DOUBLE. Amount paid to the driver for this completed trip.
- shared_request_flag: STRING (Y or N). Indicates whether the rider asked for a shared ride.
- shared_match_flag: STRING (Y or N). Indicates whether the trip was matched with other passengers.
- access_a_ride_flag: STRING (Y or N). Flag for Access-A-Ride paratransit service.
- wav_request_flag: STRING (Y or N). Indicates whether a wheelchair accessible vehicle was requested.
- wav_match_flag: STRING (Y or N). Indicates whether the trip was fulfilled with a wheelchair accessible vehicle.