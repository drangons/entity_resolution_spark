Refers file for solr instance.

It implements the schema for a resturant dataset.

step 1 : I reads the data from postgresql instance mentioned in dataimport file.

Step 2 : perform q-gram generation for movie names to handle spell errors. 

Step3 : implements jaro-winkler spell suggestion based on index for genre column

Step4 : stores index and allow querying 
