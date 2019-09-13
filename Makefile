# Copyright (C) 2019 Thomas Hellström <rel@xed.se>
# 
# This file is part of ez-gecos.
# 
# ez-gecos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# ez-gecos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with ez-gecos.  If not, see <http://www.gnu.org/licenses/>.

.phony: noop build clean publish install-dev bump-patch bump-minor bump-major

noop:


build:
	@python setup.py bdist_wheel

clean:
	@[ -d build ] && rm -rf build
	@[ -d dist ] && rm -rf dist
	
publish:
	@twine upload dist/*

install-dev:
	@pipenv install --dev

bump-patch:
	@bump patch

bump-minor:
	@bump minor

bump-major:
	@bump major

