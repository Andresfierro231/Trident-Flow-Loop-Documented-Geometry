.PHONY: all pdf generate test

all: pdf

pdf:
	python3 scripts/build.py

generate:
	python3 scripts/generate.py

test:
	python3 -m unittest discover -s tests -v
