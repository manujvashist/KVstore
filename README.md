# KVstore

Build Instructions:
1) Clone the Repository and open a terminal inside it.
2) Run "docker-compose up -d" to start the build process.
3) Run "docker ps -a" to check the currently running containers and you should see 2 containers related to this:
    i) KVstore
    ii) Redis
4) Now the KVstore server will be running on port 5000 of your local machine, and can be accessed using HTTP requests.
5) Run.sh is the shell script to test the features from command line.
6)  i) To perform get(key), Use "sh run.sh get key".
    
   ii) To perform put(key,value), Use "sh run.sh put key 'Value' ".
    
   iii) to perform watch, use "sh run.sh watch".
  
  Design:
  
  Server side implementation is done in Django framework using Redis as key-value database.
  In Classes->RedisClass.py contains the helper functions to query the database.
  In Home-views.py contain the main server code which interacts with the client and the database.
  
Currently "watch" feature is not implemented but can be done by making the client side interface to ping continuously to a longpull function and update its state with every call. If between 2 calls any key value pair changes or get added it can be known from the current state if it is reflected to the active watchers or not and if not then it can be returned with the next call.

Note:
1) This is only a simple example and does not contain any authentication between user and server for the queries which can be     termed as security flaw as anyone with the api address can change the data.
To overcome this the standard procedure is to have a password or unique "access key" for each user so that only with that key passed as a parameter they can access the api.

2) Database is not password protected: Due to this any developer can change or have a look in the database.
