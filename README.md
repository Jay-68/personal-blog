# Personal Blog

####  An Application for creating personal blogs

![Home page](flaskblog/static/main.png)
![alt text](flaskblog/static/account.png)

## Author
[James Ngari](https://github.com/Jay-68).

## Description
An application that allows users to create accounts and post new blogs. Users can also upload their own profile pictures and update their account details.

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the following external libraries provided in the requirements.txt file using pip
* Example:
    * **`pip install flask`**

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/Jay-68/personal-blog`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv virtual`**
    * **`source virtual/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
    * Create a file in your root directory called start.sh and store a generated SECRET key like so **`export SECRET_KEY="<your-key>"`**
    * On the same file write down the command **`python3 manage.py server`** 
* **Step 6** : On your terminal, run the following command, **`chmod a+x start.sh`**
    * You can now launch the application locally by running the command **`./start.sh`** 
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:5000/**.

## Known Bugs
* The like ad dislike buttons functionality error.

## Technologies Used
* Python 3.7.4
* Flask 1.1.1
* HTML
* CSS
* Bootstrap 4

## Support and contact details
You can provide feedback or raise any issues/ bugs through the following means:
* ngari.james.n@gmail.com

## Live Site link
You can view the live application by following this [link](https://frozen-temple-76576.herokuapp.com/).

## License
##### MIT license
