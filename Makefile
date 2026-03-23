# Comando para rodar um teste rápido
run:
	python3 main.py data/lista_1000_1.txt

# Comando para rodar todos os arquivos da pasta data (exemplo)
test-all:
	@for file in data/*.txt; do \
		python3 main.py $$file; \
	done

clean:
	rm -rf src/__pycache__ .pytest_cache
