@echo off

cd scripts

title Loading ...
set /p req_contents=<requeierments.txt

if %req_contents% == DONE start menu.py && exit

title Installing Packages ...

pip install -r requeierments.txt
echo DONE>requeierments.txt
start menu.py