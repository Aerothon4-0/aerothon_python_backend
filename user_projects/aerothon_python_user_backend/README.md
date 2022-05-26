# aerothon_python_user_backend
Python back-end for user website


Install the dependencies and setting environment variables:

```bash
pip install -r requirements.txt
```


To migrate database

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

Initialize data:

```bash
flask initialize-data
```

Running locally:

```bash
flask run
```

Running in production:

```bash
bash start.sh
```

### 'sudo chmod 700 ./start.py' To give root permision to pytho script



### Author

Alan Alby

