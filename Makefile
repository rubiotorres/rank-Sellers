export PYTHONPATH=$(PWD)

clear:
	@printf "Limpando arquivos temporários... "
	@rm -rf dist/
	@rm -rf build/
	@rm -rfd *.egg-info
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.log' -delete
	@echo "OK"

requirements:
	@pip install -r requirements.txt

env-create: env-destroy
	@printf "Criando ambiente virtual... "
	@virtualenv -q -p python3.8 venv
	@echo "$(SUCCESS)"

env-destroy:
	@printf "Destruindo ambiente virtual... "
	@rm -rfd venv
	@rm -rfd migrations
	@echo "$(SUCCESS)"

docker-up:
	@docker-compose --log-level ERROR up -d

docker-down:
	@docker-compose down

system-packages:
	@printf "Instalando 'pip' e 'virtualenv'... "
	@curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	@python3 -q get-pip.py 1> /dev/null --user
	@pip install -q -U pip
	@pip install -q virtualenv --user
	@rm get-pip.py
	@echo "$(SUCCESS)"

packages: env-create
	@printf "Instalando bibliotecas... "
	@venv/bin/pip install -q --no-cache-dir -r requirements.txt
	@echo "$(SUCCESS)"

install: clear system-packages packages
	@echo "============================================"
	@echo "All ready for development"
	@echo ""
	@echo "Type to activate the environment:"
	@echo ""
	@echo "source venv/bin/activate"
	@echo "============================================"

coverage:
	@python -m pytest -x ./tests --cov --cov-report=term-missing --cov-report=xml

run-worker:
	@python ./src/main.py
