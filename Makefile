PYTHON = python3
POETRY = poetry

run: install
	@$(PYTHON) a_maze_ing.py || true

install:
	pip install -e .

clean: fclean
	rm -rf __pycache__

fclean:
	rm -rf maze.txt poetry.lock src/__pycache__

.PHONY: install run
