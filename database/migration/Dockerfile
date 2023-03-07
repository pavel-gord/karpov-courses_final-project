FROM python:3.11

COPY requirements.txt requirements.txt
COPY fill_db.py fill_db.py

RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python3", "fill_db.py"]