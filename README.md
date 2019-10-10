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
 
Assumptions:  
1. TinyUrl collisions NEVER happen. There are a total of 62^10 possible tinyUrls, so even if we make millions of URLs, the chances of collisions are very small  
2. The in-memory cache simulated by the LongUrl's url_cache variable is large enough to hold the tinyUrls of interest to users and should return the full URLs most of the time. In a real system, I would use something like Redis instead.  

Design/Architecture Decisions:  
1. Used Python + Flask for quick, easy development, and fantastic documentation.
2. I used MongoDB as I wanted a noSQL database for its better scalability and schema flexibility compared to SQL DBs. It also has great Python drivers like mongoengine, which I used in this project.  
3. When looking for a full URL based on a shortUrl, I first try to retreive it from the cache, failing which I do a database query.
4. In my db schema, I decided to allow for the same short URL to be stored many times because I use the count of these URLs and their timestamps to grab the number of times it was accessed in the 24-hour/1-week/all-time period.

## API calls supported
### 1. Post Request: "/shorten"

- This takes a long URL and converts it into a tinyURL. Then it persists both URLs and the current timestamp into the DB and cache
- The tiny URL will be exactly 10 characters long, consisting of uppercase letter and lowercase letters
- example json payload: 
``` 
{
    "long_url": "someSuperDuperLongUrl"
}
```
- example good json response will contain what the long URL was shortened to: 
``` 
{
    "long_url": "someSuperDuperLongUrl"
    "short_url": "shorty"
}
```

### 2. Post Request: "/findlong"

- This takes a short URL and returns the corresponding long URL. It will try accessing the cache for this, failing which it will grab the data from the DB, persist that in the cache, and return the long URL

- example json payload: 
``` 
{
    "short_url": "gwe34f"
}
```

- example json response: 
``` 
{
    "short_url": "gwe34f",
    "long_url": "superDuperUltraIncrediblyLongURL
}
```

### 3. Post Request: "/stats"

- This takes a short URL and returns the number of times it has been accessed over 24 hours, a week and all-time
- example json payload: 
``` 
{
    "short_url": "gwe34f"
}
```

- example json response: 
``` 
{
    "short_url": "gwe34f",
    "day_accesses": 2,
    "week_accesses": 12,
    "all_time_accesses": 30
}
```
