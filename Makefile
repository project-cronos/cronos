SHELL := /bin/bash


.PHONY: all
all: dev

.PHONY: clean
clean:
	rm -rf ./venv

.PHONY: dev
dev:
	pip install -r requirements.txt
	pre-commit install


.PHONY: env
env:
	python3 -m venv ./venv

.PHONY: source
source:
	source ./venv/bin/activate
