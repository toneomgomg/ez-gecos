# ez-gecos (v0.0.1)
Tiny package to parse the GECOS field.

![GPLv3](https://img.shields.io/github/license/thohell/ez-gecos)
![v0.0.1](https://img.shields.io/github/v/tag/thohell/ez-gecos)

- [Version](#version)
- [Installation](#installation)
  - [PyPi](#pypi)
    - [pip](#pip)
    - [pipenv](#pipenv)
  - [Github](#github)
    - [pip](#pip-1)
    - [pipenv](#pipenv-1)
- [Usage](#usage)
- [License](#license)

## Version

ez-gecos is only tested on Python 3.7

## Installation

### [PyPi](https://pypi.org/)
#### pip
```
pip install ez-gecos
```
#### pipenv
```
pipenv install ez-gecos
```
### [Github](https://github.com/thohell/ez-gecos)
#### pip
```
pip install git+https://github.com/thohell/ez-gecos.git
```
#### pipenv
```
pipenv install git+https://github.com/thohell/ez-gecos.git
```

## Usage

```python
from gecos import GECOS

# If username is not supplied, GECOS tries to parse the GECOS
# field of the username found in environment variable 'USER'
gecos = GECOS(username='someuser')
# or
gecos = GECOS()

# Full name from GECOS field or None.
print(gecos.full_name)

# Room from GECOS field or None.
print(gecos.room) 

# Work phone from GECOS field or None.
print(gecos.work_phone) 

# Home phone from GECOS field or None
print(gecos.home_phone) 

# Other from GECOS field or None.
# If there are more than one other, they are returned
# as a comma separated list.
print(gecos.other) 

# Full GECOS field or None
print(gecos.full)
# or
print(gecos)


# Returns email address from GECOS field or None. 
# The email address is parsed from 'other', and 
# returns first entry that looks like an email address.
print(gecos.email_address)
```

## License

ez-gecos: [GPLv3](LICENSE)