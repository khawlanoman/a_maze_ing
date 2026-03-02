PYTHON = python3

run:
	@$(PYTHON) main.py || true

clean: fclean
	rm -rf __pycache__

fclean:
	rm -rf maze.txt poetry.lock src/__pycache__

.PHONY: install run
