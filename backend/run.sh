source .env
export FLASK_APP=app.py
export FLASK_ENV=development

flask run --debug --host=0.0.0.0 --port=$((PORT))