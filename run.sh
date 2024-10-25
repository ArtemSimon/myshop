
docker build -t sf_myshop .
docker run --rm -ti --name myshop -p 8000:8000 sf_myshop
