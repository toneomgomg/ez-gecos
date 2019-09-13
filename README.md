# ez-gecos (v0.1.0)
Tiny package to parse the GECOS field.

![GPLv3](https://img.shields.io/github/license/thohell/ez-gecos)
![v0.1.0)

- [v0.1.0)
- [Installation](#installation)
  - [PyPi](#pypi)
  - [Github](#github)
  - [From source](#from-source)
- [Usage](#usage)
- [Links](#links)
- [License](#license)

## Version

ez-gecos is only tested on Python 3.7

## Installation
Simply install using pip (or pipenv).

### PyPi
```
pip install ez-gecos
```
### Github
```
pip install git+https://github.com/thohell/ez-gecos.git
```

### From source
```
git clone https://github.com/thohell/ez-gecos.git
pip install ./ez-gecos
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

## Links
* ez-gecos on [Github](https://github.com/thohell/ez-gecos)
* ez-gecos on [PyPi](https://pypi.org/)

## License

ez-gecos: [GPLv3](LICENSE)