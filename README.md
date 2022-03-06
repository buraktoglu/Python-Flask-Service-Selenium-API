# Python-Flask-Service-Selenium-API

Project Milestones is explained in detail as in the following note page. 

Please visit: https://www.evernote.com/shard/s432/sh/4ec29a8c-cb03-0458-dc49-4976b1a189b1/a48090f740c475e66214eb58def3642d

Step 1: Install Python environment and Selenium, Flask libraries if not installed in your local workspace.

Step 2: Run the CarFilteringService.py. Please make sure your Python environment is setted up, and python interpreter works.

Step 3: In CommandPrompt outputs as in the following image. Service will be running on http://localhost:5000/ or http://127.0.0.1:5000/ as default in Flask lib. Port number can be modified in source code.

![runningPort](https://user-images.githubusercontent.com/52565454/156944311-c04ab2cd-7aeb-48ad-bc56-7382b1a04507.jpg)

Step 4: Requests can be send with a web browser or Postman alike RequestSender middlewares. 

Valid Request as case study demands:

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
