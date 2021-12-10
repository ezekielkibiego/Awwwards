# Awwwards

### 10th Dec. 2021

## Author  
  
[Ezekiel Kibiego](https://github.com/ezekielkibiego)  
  
# Description  


##  Live Link  
 
 https://awwwardsmega.herokuapp.com/
  
## Screenshots 

<img src="static/images/Screenshot (1).png">
<img src="static/images/Screenshot (3).png">
<img src="static/images/Screenshot (2).png">
<img src="static/images/Screenshot (4).png">
<img src="static/images/Screenshot (5).png">
<img src="static/images/Screenshot (6).png">
 
 
## User Story  
  


  
## Setup and Installation  
  
##### Clone the repository:  
 ```bash 
 git@github.com:ezekielkibiego/Awwwards.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Awwwards 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual 
- source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django==3.2.7](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs  
  
## Support and Contact Information 

To make a contribution to the code used or for any queries feel free to contact me via my email addresses ezekiel.nyambane@student.moringaschool.com or kibiezekiel@gmail.com

## License

### MIT LICENCE

#### Copyright (c) 2021 **Ezekiel Kibiego** ~ Moringa School

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.