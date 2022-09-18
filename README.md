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
```
cd BackEnd-CRM/
mkvirtualenv -a . --python=python3.8 crm
```