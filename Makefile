.PHONY: all pdf generate test

all: pdf

pdf:
	python3 support/scripts/build.py

generate:
	python3 support/scripts/generate.py

test:
	python3 -m unittest discover -s support/tests -v
