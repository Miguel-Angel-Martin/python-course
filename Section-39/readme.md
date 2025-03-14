# CAPTON project.

[Sheety](https://dashboard.sheety.co/projects/67b82ee47c36d479f76d69cb/sheets/prices)

[Amadeus](https://developers.amadeus.com/)
[Amadeus Flight Offer Docs](https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference)
[Amadeus How to work with API keys and tokens guide](https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335)
[Amadeus Search for Airport Codes by City name](https://developers.amadeus.com/self-service/category/destination-experiences/api-doc/city-search/api-reference)
[Twilio Messaging (SMS or WhatsApp) API](https://www.twilio.com/docs/messaging/quickstart/python)

[IATA AIRPORTS LIST](https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_commercial_airports)


[API reference](https://developers.amadeus.com/self-service/category/flights/api-doc/airport-and-city-search/api-reference)

# Program Requirements

1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).

2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.

4. The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates. e.g.