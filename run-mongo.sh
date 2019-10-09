docker run -d -p 27017:27017 -v ~/data:/data/db --name mongo mongo
docker run -it --rm -env mongo_ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mongo) -v $PWD:/directory jeremycollinsmpi/legalnlp:cpu /bin/bash

# inside container
# mongo $mongo_ip/mydb