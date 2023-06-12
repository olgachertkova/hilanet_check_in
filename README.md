**Overview**

This is the script that helps daily check in Hilanet make easier.
Just run it!

**Installation**
1. Create a new directory on your computer
   
2. Clone the repo in this directory

`   git clone https://github.com/olgachertkova/hilanet_check_in.git
`

3. Create virtual environment (if it is needed)
 
`cd hilanet_check_in
`

`python3 -m venv venv
`

`source venv/bin/activate
`

4. Install dependencies

`pip3 install -r requirements.txt
`

5. Install Chromium browser for script running

` playwright install chromium
`

**Usage:** 

Run script by command:

`pytest --user='[user_number]' --password='[user_password]' `