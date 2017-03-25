.PHONY: docs

PYTHON = python

install:
	cat requirements/*.txt > requirements.txt
	pip install -r requirements.txt

	$(PYTHON) setup.py install

run:
	$(PYTHON) -m spockpy

docs:
	cd docs && make html

tests:
	# $(PYTHON) setup.py tests

clean:
	$(PYTHON) setup.py clean

all:
	make install docs tests clean