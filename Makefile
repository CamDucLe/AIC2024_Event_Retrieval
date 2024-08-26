VENV := .venv
PYTHON := python3

setup_venv:
	@if [ ! -d ".venv" ]; then \
		echo "Creating virtual environment in $(VENV)"; \
		$(PYTHON) -m venv $(VENV); \
	else \
		echo "Virtual environment already exists. Name: $(VENV)"; \
	fi
	@chmod +x bash_script/setup_venv.sh
	@./bash_script/setup_venv.sh

pre-commit:
	@ $(MAKE) setup_venv
	@chmod +x bash_script/pre-commit.sh
	@./bash_script/pre-commit.sh
