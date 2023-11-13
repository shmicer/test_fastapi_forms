FROM mongo

COPY test_collection.json /test_collection.json
CMD mongoimport --host mongo_db --db test_collection --collection test_collection --type json --file /test_collection.json --jsonArray