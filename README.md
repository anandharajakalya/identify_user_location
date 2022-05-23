## IDENTIFY USER LOCATION

#### PROBLEM STATETMENT:
Given user tower data , identify the user's place of stay and work.Also, 
identify the address of the specific user's place of work or stay


#### METHOD

##### Datagathering
Cell tower data - Mock user geolocation data is created 
OSM - Openstreet map data is scraped and metadata such as building,name,street,postcode and geometry of the building is extracted

##### Datapreprocessing
User's geolocation data (mock data) is preprocessed and binned to categorize morning and evening.The occurences of each user's location at the bins is used to find the user's work or resient location.

##### Algorithm
Point in Polygon Algorithm is used to identify if the geolocation coordinate of the user falls inside the geometry of the building

#### Techniques involved
Data Scraping,exploration and manipulating,PIP algorithm

#### Languages and tools used
Python, QGIS


##### Results 
The snippets of the results are shown below

###### Residential and Industrial building categorization on a map
![This is an image](https://www.linkpicture.com/q/industrialandresidential.png)

###### User location inside and outside of residential building (Blue circle dots are user locations)
![This is an image](https://www.linkpicture.com/q/pointlyinandoutresidential.png)

###### User location identified inside a industrial building (Blue circle dots are user locations)
![This is an image](https://www.linkpicture.com/q/pointlyinginsideindustrial.png)

###### Snapshot of the results in the database(CSV)
![This is an image](https://www.linkpicture.com/q/snapshotofresults.png)



