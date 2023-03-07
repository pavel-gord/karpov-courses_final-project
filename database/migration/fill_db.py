import psycopg2
import os

conn = psycopg2.connect(database=os.environ.get('PG_DB'),
                        host=os.environ.get('HOST'),
                        user=os.environ.get('PG_USER'),
                        password=os.environ.get('PG_PASSWORD'),
                        port=os.environ.get('PORT'))

conn.autocommit = True
cursor = conn.cursor()

# PEAS TABLE---------------------------------------------------------------------------------------
# Create the peas table
cursor.execute("""
CREATE TABLE IF NOT EXISTS peas (
    st_id int NOT NULL,
    timest timestamp,
    correct boolean,
    subject text
);
""")

# And fill it with data
cursor.execute("""
COPY peas(st_id,timest,correct,subject)
FROM '/csv_data/peas.csv'
DELIMITER ','
CSV HEADER;
""")

# STUDS TABLE---------------------------------------------------------------------------------------
# Create the studs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS studs (
    st_id INT NOT NULL,
    test_grp text
);
""")

# And fill it with data
cursor.execute("""
COPY studs(st_id,test_grp)
FROM '/csv_data/studs.csv'
DELIMITER ','
CSV HEADER;
""")

# CHECK TABLE---------------------------------------------------------------------------------------
# Create the check table
cursor.execute("""
CREATE TABLE IF NOT EXISTS final_project_check (
    st_id int NOT NULL,
    sale_time timestamp,
    money int,
    subject text
);
""")

# And fill it with data
cursor.execute("""
COPY final_project_check(st_id,sale_time,money,subject)
FROM '/csv_data/final_project_check.csv'
DELIMITER ','
CSV HEADER;
""")

conn.commit()
conn.close()
