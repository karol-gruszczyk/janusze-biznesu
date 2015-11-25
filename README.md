## Janusze Biznesu

A powerfull tool for predicting the stock exchange.

### Requirements
* python 3.5
* pip
* virtualenv
* Packages  
`sudo apt-get install python3.5-dev lm-sensors build-essential gfortran libatlas-base-dev`

### Setup
```bash
git clone git@github.com:karol-gruszczyk/janusze-biznesu.git
cd janusze-biznesu
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
```

### Running
`./manage.py runserver`
