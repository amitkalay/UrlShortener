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
