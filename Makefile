PYTHON = python3
POETRY = poetry

run: 
	$(POETRY) run $(PYTHON) main.py

clean: fclean
	rm -rf __pycache__

fclean:
	rm -rf maze.txt poetry.lock src/__pycache__

.PHONY: install run
