PYTHON = python3
PIP = pip
POETRY = poetry

run: install
	$(POETRY) run $(PYTHON) main.py

install:
	$(POETRY) install

clean: fclean
	rm -rf __pycache__

fclean:
	rm -rf maze.txt poetry.lock src/__pycache__

.PHONY: install run
