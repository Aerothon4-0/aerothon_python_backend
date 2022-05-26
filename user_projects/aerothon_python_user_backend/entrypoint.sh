
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

flask initialize-data

echo "flask run started"
flask run --host=0.0.0.0 --port=${APP_PORT}