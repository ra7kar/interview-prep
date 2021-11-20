

.PHONY: test install

install:
	python3 -m pip install -r requirements.txt --user

test: install
	pytest