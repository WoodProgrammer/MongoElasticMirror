# Mongo Elastic Mirror (Not Production Grade) :snake: 


Tool Overview
---------------

MongoElasticMirror is a tool for mirroring  datas in MongoDB to elastic search concurently.This tool work with the capable  collections. Capable Collections are only accept the insert query to the collections. 

### Creating Capable Collections
Switch to the mongo console. 	
   
    >> use db_name
    >> db.createCollection("COLLECTION_NAME", {capped:true, size:SIZE})
    

You can create multiple capable collections for mirroring with ElasticSearch.

## Tailing 
Clone the projects 

    $ git clone  https://github.com/initack/MongoElasticMirror
    $ cd MongoElasticMirror
Install the Dependieces. 

    $ pip install -r requirements.txt
    
    
Start the tailing the collections on MongoDB :leaves: :leaves: :leaves:

<h3>

	$ python tail.py --db DB_NAME col1 col2 col3 --cols 
    
</h3>


# Mirroring 

For mirroring control your ElasticSearch instance health.

	$ curl localhost:9200
    
      {
        "name" : "ZfApsaa",
        "cluster_name" : "elasticsearch",
        "cluster_uuid" : "UUID",
        "version" : {
          "number" : "5.6.7",
          "build_hash" : "BUILD_HASH",
          "build_date" : "DATE",
          "build_snapshot" : false,
          "lucene_version" : "6.6.1"
        },
        "tagline" : "You Know, for Search"
      }
    
  
  If you have a <b>OK</b> message like shown as above your ElasticSearch instance is up .:clap::clap::clap::clap:
   
   
  So you can start to mirroring with start the <b>RABBITMQ </b> instance .
  
  ### Coming Soon of Docs. ###
   
  
      
      