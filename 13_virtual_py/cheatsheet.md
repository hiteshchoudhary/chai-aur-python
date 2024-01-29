# python virtual environment cheatsheet

## Create a new virtual environment
`python -m venv env_name`

## Install packages
`pip install package_name`

## Save installed packages to a file
`pip freeze > requirements.txt`
or 
`pip list --format=freeze > requirements.txt`

## Install packages from a file
`pip install -r requirements.txt`

## Deactivate the current virtual environment
`deactivate`



## In Linux or Mac, activate the new python environment
`source env_name/bin/activate`
## Or in Windows
`.\env_name\Scripts\activate`