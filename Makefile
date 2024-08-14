.PHONY: init requirements run increase-patch


init:
	POETRY_VIRTUALENVS_IN_PROJECT=true env -u VIRTUAL_ENV poetry install --no-root
	pre-commit install

requirements:
	poetry export -f requirements.txt -o requirements.txt --without-hashes --without-urls
	poetry export -f requirements.txt -o dev-requirements.txt --with=dev --without-hashes --without-urls

run:
	uvicorn src.app:app --factory --reload --host 0.0.0.0 --port 80

increase-patch:
	python -c "from pathlib import Path; from src import __version__; Path('src/__init__.py').write_text(f'__version__ = {__version__[:2] + (__version__[2] + 1,)}\n')"
