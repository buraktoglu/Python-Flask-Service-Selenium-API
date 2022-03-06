# Python-Flask-Service-Selenium-API

Project Milestones is explained in detail as in the following note page. 

Please visit: https://www.evernote.com/shard/s432/sh/4ec29a8c-cb03-0458-dc49-4976b1a189b1/a48090f740c475e66214eb58def3642d

Step 1: Install Python environment and Selenium, Flask libraries if not installed in your local workspace.

Step 2: Run the CarFilteringService.py. Please make sure your Python environment is setted up, and python interpreter works.

Step 3: In CommandPrompt outputs as in the following image. Service will be running on http://localhost:5000/ or http://127.0.0.1:5000/ as default in Flask lib. Port number can be modified in source code.

![runningPort](https://user-images.githubusercontent.com/52565454/156944311-c04ab2cd-7aeb-48ad-bc56-7382b1a04507.jpg)

Step 4: Requests can be send with a web browser or Postman alike RequestSender middlewares. 

Valid Request formats as case study demands: Requests in these formats will be responded 200(OK) by service.

http://localhost:5000/cars/list

http://localhost:5000/cars/list?brand=audi

http://localhost:5000/cars/list?year=2018

http://localhost:5000/cars/list?year=2018&year=2019

http://localhost:5000/cars/list?color=blue

http://localhost:5000/cars/list?color=blue&color=beige

http://localhost:5000/cars/list?color=blue&color=beige&color=black

http://localhost:5000/cars/list?trans=automatic

http://localhost:5000/cars/list?trans=automatic&trans=automanual

http://localhost:5000/cars/list?trans=automatic&trans=automanual&trans=cvt

http://localhost:5000/cars/list?brand=audi&year=2018&color=blue&trans=automanual

Invalid Request formats due to configurations of the website: Requests in these formats will be responded 400(Bad Request) by service.

http://localhost:5000/cars/list?brand=audi&brand=bmw

http://localhost:5000/cars/list?year=2018&year=2019&year=2020

Issues:

Issue 1: Sponsored Adverts in cars.com redirects the flow to another domain so selenium stops working. Please send the request to service again when Sponsored Adverts shows up int he browser.

Issue 2: Transmission and exterior color information does not included in main listing page. Thus, Selenium API needs to roundtrip between each car's advert URL's. This extends the response time of the service in a linear manner. A modified version of the service without demanding transmission and color information could be written and added to the project. This will be the game changer when time management taken into consideration.

Issue 3: SeleniumAPI_test.py file is not related with the project. This file is just a workspace for the guidelines of the project. Service will provide without need. 



