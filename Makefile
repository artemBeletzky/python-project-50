install:
	poetry install

brain-games:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/*.whl

lint:
	poetry run flake8