#!/bin/bash
cd /opt/ToDoListApp
sudo mkdir /projectname
sudo chown  -R /propjectname
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
