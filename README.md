# Restaurant Place picker

Powered By 
[![Python|Django](https://twilio-cms-prod.s3.amazonaws.com/images/django-dark.width-808.png)](https://www.djangoproject.com/)


    Restaurant Place picker Project Backend Section
- REST API
- High Performance
- Reliable

### Installation Steps

Restaurant Place picker Backend requires [Python](https://python.org/) v3.6+ & [Django](https://www.djangoproject.com/) v2.4 to run.

Install the dependencies and devDependencies and start the server.

###### Create a virtual environment

```sh
virtualenv --python=`which python3` virtenv
```
###### Activate the virtual environment
```sh
source virtenv/bin/activate
```
###### Clone this repository
```sh
git clone <repo_link_git>
```
###### Change Directory to the Folder
```sh
cd lunch_place_piker/
```
###### Install required libraries
```sh
pip install -r requirements.txt
```
###### Setup .ENV file & Refresh the Connected Database
(configure database accordingly from .env file)
```sh
./reset_models.sh
```
###### Run Server Locally in your system
```sh
python manage.py runserver
```

### Docker
Restaurant Place picker Backend is very easy to install and deploy in a Docker container.

First you have install the Docker in your machine, you can install docker in you machine using following link 
[![Docker Install]](https://docs.docker.com/engine/install/)

After that navigate to project directory and run


```sh
cd lunch_place_piker
docker-compose up
```
This will create the lunch_place_piker image and install the necessary dependencies. 

Once up Verify the deployment by navigating to your server address in your preferred browser.

For Localhost:
```sh
127.0.0.1:8000
```
For System IP: (e.g. 192.168.0.199)
```sh
192.168.0.199:8000
```

### API Guide

###### Atuhentication API's
![Authentication](https://i.ibb.co/0Qry71j/image-2021-06-07-T13-35-29-409-Z.png)

##### Restaurant API's
![Restaurant](https://i.ibb.co/RSd62B0/image-2021-06-07-T13-47-07-344-Z.png)

##### Create Food Items and set food manue for specific day
![Food Manu](https://i.ibb.co/F4P2sS2/image-2021-06-07-T13-52-32-035-Z.png)

##### Vote Cast and get the winner of the day
![Vote Cast | Winner](https://i.ibb.co/VJFH7bQ/image-2021-06-07-T13-56-55-315-Z.png)
