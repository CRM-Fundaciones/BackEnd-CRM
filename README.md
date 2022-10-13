# BackEnd-CRM
Postgres con Django framework integrado con Heroku

## Download the repository

```sh
git clone https://github.com/CRM-Fundaciones/BackEnd-CRM.git
```

## Install virtualenvwrapper

1. Install package:
```
sudo pip install virtualenvwrapper
```
2. Configure .bashrc (windows/linux) or .zshrc (MacOS), open and add:
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
3. Reload startup file
```sh
source ~/.bashrc # Or ~/.zshrc
```


### Create an enviroment

1. Add deadsnakes:
```
sudo add-apt-repository ppa:deadsnakes/ppa
```

2. Install python3.8:
```
sudo apt install python3.8 python3.8-dev
```

3. Install distutils:
```
sudo apt install python3.8-distutils
```

4. Create the enviroment
```
cd BackEnd-CRM/
mkvirtualenv -a . --python=python3.8 crm
deactivate
```

5. Add to ~/Envs/crm/bin/postactivate:
```
export PYTHONPATH=[/path/to/repo]BackEnd-CRM
```

### Install the requieremnts

```
workon crm
pip install -r requirements.txt
```
