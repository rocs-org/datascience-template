install:
	poetry install

install-kernel:
	poetry run python -m ipykernel install --user --name $(name) --display-name "Python ($(name))"

test:
	poetry run pytest

watch:
	poetry run pytest -f --color=yes