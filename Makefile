PYTHON = python3
POETRY = poetry

run: install
	@$(POETRY) run $(PYTHON) a_maze_ing.py || true

install:
	@$(POETRY) install

clean: fclean
	rm -rf __pycache__

fclean:
	rm -rf maze.txt poetry.lock src/__pycache__ src/mazegen/__pycache__

.PHONY: install run clean fclean
