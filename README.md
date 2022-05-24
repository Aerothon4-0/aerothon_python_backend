# aerothon_python_backend
Python back-end for core project



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

Running locally:

```bash
flask run
```

Running in production:

```bash
bash start.sh
```


### Author

Alan Alby

