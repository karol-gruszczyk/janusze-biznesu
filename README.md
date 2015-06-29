## Janusze Biznesu

A powerfull tool for predicting the stock exchange.

### Requirements
* python 3
* pip
* virtualenv
* python3-dev (python header files)
* lm-sensors (temperature sensors package)

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
