# UrlShortener
An HTTP-based microservice to manage short urls

Setup instructions:  
1. Download python with its default setup instructions (I used version 3.7.4) 
2. Download Pycharm  
3. Run pip install flask  
4. Run pip install flask-restful  
5. Install mongoDB (https://docs.mongodb.com/v3.2/tutorial/install-mongodb-on-windows/)  
6. Run pip install mongoengine  
7. To run the service thru Pycharm, go to api.py and click the green arrow in the sidebar.  
8. If you wish to start it in the command line, enter ```python api.py``` in the terminal  
9. To run all unit test, right-click the tests directory in Pycharm and select Run Unittests in Tests  
10. Download Postman for your desktop and import the TinyURL.postman_collection.json there. You should be all ready to go from there!  
11. Use MongoDb compass to see and verify that the URLs are getting persisted. Create a database called ```tinyurl_db``` and collections inside that called all_urls and short_url_access  
 
Assumptions:  
1. TinyUrl collisions NEVER happen. There are a total of 62^10 possible tinyUrls, so even if we make millions of URLs, the chances of collisions are very small  
2. The in-memory cache simulated by the LongUrl's url_cache variable is large enough to hold the tinyUrls of interest to users and should return the full URLs most of the time. In a real system, I would use something like Redis instead.  

Design/Architecture Decisions:  
1. Used Python + Flask for quick, easy development, and fantastic documentation.
2. I used MongoDB as I wanted a noSQL database for its better scalability and schema flexibility compared to SQL DBs. It also has great Python drivers like mongoengine, which I used in this project.  
3. When looking for a full URL based on a shortUrl, I first try to retreive it from the cache, failing which I do a database query.
4. In my db schema, I decided to allow for the same short URL to be stored many times because I use the count of these URLs and their timestamps to grab the number of times it was accessed in the 24-hour/1-week/all-time period.

API Contract Instructions:  
Import the TinyUrl.postman_collection.json into POSTMAN and play around with the service from there! You can also use POSTMAN to generate the corresponding cURL commands for the service. i.e. the healthcheck endpoint can be accessed by  
``` 
GET /healthcheck HTTP/1.1
Host: localhost:5000
User-Agent: PostmanRuntime/7.18.0
Accept: */*
Cache-Control: no-cache
Postman-Token: db8d911f-c10f-4ab6-9785-91e9b09dd6d6,6cf1ed08-376a-4fe0-b277-6f6247d631b2
Host: localhost:5000
Accept-Encoding: gzip, deflate
Connection: keep-alive
cache-control: no-cache
```
