# Project 5 - Cloud DevOps Engineer Capstone Project

In this project, I chose the app of offering weather API for given city and chose green/blue deployment for my pipeline. 

## Repository

All code sits in here. 
https://github.com/misenli/CloudDevOpsProject5

## Directory structure
~~~
.
├── Dockerfile -- application container runtime
├── Jenkinsfile -- Pipeline file
├── Makefile
├── Pipfile -- pipfile for python package mngt. 
├── Pipfile.lock -- pipfile for python package mngt. 
├── README.md -- this file
├── infra -- infrastructure code
│   ├── app -- Kubernetes manifesto in Jenkins pipeline 
│   │   ├── deployment-blue.yml
│   │   ├── deployment-green.yml
│   │   ├── service-blue.yml
│   │   └── service-green.yml
│   └── bootstrap -- code for bootstrapping the AWS and Kubernetes infra
│       ├── Makefile 
│       ├── aws_infra.yml -- Cloudformation for AWS infra
│       ├── create.sh -- helper to create AWS infra
│       ├── eksctl_config.yml -- for creating EKS
│       ├── params.json -- Cloudformation for AWS infra
│       └── update.sh-- helper to update AWS infra
├── screen_shots -- for rublic 
│   ├── blue-green_deployment -- showing the blue-green deployment
│   │   ├── 01_greendeploy.png
│   │   ├── 02_greenservice.png
│   │   ├── 03_turnonblue.png
│   │   ├── 04_bluedeploy.png
│   │   └── 05_blueservice.png
│   └── linting -- showing the linting is working
│       ├── failed.png
│       └── success.png
├── src -- code for weather api app
    ├── app.py
    └── requirements.txt
~~~

## Weather service

You can get the current weather for the big city across the world. 

Example request
~~~
$ curl --location --request POST 'http://afd0457aa11b842588d79a0a32ffc35e-747779521.ap-northeast-1.elb.amazonaws.com:8000/weather/v1' \
--header 'Content-Type: text/plain' \
--data-raw 'Tokyo' # You can change the city name for whatever you like. 
~~~

Example response
~~~
test({"coord":{"lon":139.69,"lat":35.69},"weather":[{"id":803,"main":"Clouds","description":"broken
clouds","icon":"04n"}],"base":"stations","main":{"temp":25.45,"feels_like":26.82,"temp_min":24.44,"temp_max":26.11,"pressure":1013,"humidity":94},"visibility":10000,"wind":{"speed":6.7,"deg":210},"clouds":{"all":75},"dt":1595685974,"sys":{"type":1,"id":8074,"country":"JP","sunrise":1595619822,"sunset":1595670691},"timezone":32400,"id":1850144,"name":"Tokyo","cod":200})version:
1.0DEPLOY_COLOR:GREEN
~~~
The response includes the city's lat lon value, weather, temperature,
sunrise and sunset time, app version and Blue/Green environment.

  