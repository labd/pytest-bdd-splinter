.PHONY: install test upload docs


install:
	pip install -e .[docs,test]

test:
	py.test

retest:
	py.test -vvv --lf

clean:
	find . -name '*.pyc' -delete

runserver:
	FLASK_DEBUG=1 FLASK_APP=tests.server flask run

coverage:
	py.test --cov=pytest_bdd_splinter --cov-report=term-missing --cov-report=html

docs:
	$(MAKE) -C docs html

release:
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*
