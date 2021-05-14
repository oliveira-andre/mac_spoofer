install_dependencies:
	pip3 install -r requirements.txt

run: install_dependencies
	sudo python3 init.py
