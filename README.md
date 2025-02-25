
# Sustainable Software Engineering (CS4415) - Group 12 
We are comparing MySQL and SQLite in the context of sustainability, this comparison will focus on energy consumption, using  **[EnergiBridge](https://github.com/tdurieux/EnergiBridge)** to measure and analyze the energy usage of both databases in a local testing environment.

## Setup
`(This project has been developed and tested on Ubuntu 22.04 and requires Python 3)`
- Clone this repo: `git clone https://github.com/HuibSprangers-leiden/course_sustainableSE && cd course_sustainableSE`

- Install Python packages:
	```
	# Create virtual environment (optional)
	# python -m venv .venv && source .venv/bin/activate
	pip install -r requirements.txt
	```
- Download the database [here](https://www.kaggle.com/datasets/terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database?resource=download) and put `olist.sqlite` into `./convert_sqlite_to_sql/`
- Then run: 
	```
	python convert_sqlite_to_sql/convert_sqlite_to_sql.py
	```

- Install `pyEnergiBridge`:
	```
	mkdir ./bin && cd ./bin && git clone https://github.com/luiscruz/pyEnergiBridge.git && cd pyEnergiBridge
	pip install .
	cd ../../
	```

- Install and build `EnergiBridge`: 
	```
	cd ./bin && git clone https://github.com/tdurieux/EnergiBridge && cd EnergiBridge
	sudo groupadd msr
	sudo chgrp -R msr /dev/cpu/*/msr
	sudo chmod g+r /dev/cpu/*/msr
	sudo chmod 666 /dev/cpu/*/msr
	sudo apt install cargo -y
	cargo build -r
	sudo setcap cap_sys_rawio=ep target/release/energibridge
	cd ../../
	```

- Install and setup MySQL:
	```
	sudo apt install mysql-server -y
	sudo systemctl start mysql
	sudo systemctl enable mysql
	sudo mysql -e "CREATE DATABASE IF NOT EXISTS \`olist_e-commerce\`; CREATE USER IF NOT EXISTS 'user_CS4575'@'localhost' IDENTIFIED BY 'password_CS4575'; GRANT ALL PRIVILEGES ON \`olist_e-commerce\`.* TO 'user_CS4575'@'localhost'; FLUSH PRIVILEGES;"
	mysql -u user_CS4575 -p'password_CS4575' -e "USE \`olist_e-commerce\`; SOURCE ./convert_sqlite_to_sql/olist_mysql_100_entries.sql;"
	```
## Run experiments
- ```
	python script_sqlite.py
	```
	measurements are saved in `results_sqlite.csv`
- ```
	python script_mysql.py
	```
	measurements are saved in `results_mysql.csv`
