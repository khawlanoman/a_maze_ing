PYTHON = python3
POETRY = poetry

run: install
		@$(POETRY) run $(PYTHON) a_maze_ing.py || true

install:
	@pip install $(POETRY)
	@$(POETRY) install

clean: fclean
	rm -rf __pycache__

fclean:
	rm -rf maze.txt poetry.lock src/__pycache__ src/mazegen/__pycache__

debug:
	python3 -m pdb -tui a_maze_ing.py
lint:
	${POETRY} run flake8 .
	${POETRY} run mypy . \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs


.PHONY: install run clean fclean
