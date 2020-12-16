#!/bin/bash 
sudo apt update
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo mkdir /opt/ToDoListApp
sudo chown -R jenkins /opt/ToDoListApp
sudo systemctl daemon-reload
sudo systemctl stop ToDoListApp.service
sudo systemctl start ToDoListApp.service
