# youtubedl-flaskapp

## requirements
docker
docker-compose

## description
This will serve a page from <ip>:5000 that has a field for youtube playlist and title of folder you wish to download playlist to. 
  
## modify the volume in docker-compose.yml - optional
By default it will use the repo root dir.
```
volumes:
  - <insert Absolute Path>:/data/scratch
```

## to run

```
# clone repo
git clone https://github.com/devOpsBeta/youtubedl-flaskapp.git

# run docker-compose
docker-compose up -d 

# view web app at <ip>:5000 or localhost:5000

```

