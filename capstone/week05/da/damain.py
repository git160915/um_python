import sqlite3
import urllib.request, urllib.parse, urllib.error
import ssl

conn = sqlite3.connect('raw_content.sqlite')
cur = conn.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS raw_ev_population_data (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        vin TEXT,
        country TEXT,
        city TEXT,
        state TEXT,
        postal_code TEXT,
        model_year INTEGER,
        make TEXT,
        model TEXT,
        ev_type TEXT,
        cafv_eligibility TEXT,
        electric_range INTEGER,
        base_mrsp INTGER,
        legislative_district TEXT,
        dol_vehicle_id TEXT UNIQUE,
        vehicle_location TEXT,
        vehicle_utility TEXT,
        census_track_2020 TEXT
    );'''
)

# create the table before continuing by commiting to DB
conn.commit()


print("Please enter filename (including full path or URL) to load.")
print("Leave empty for default: https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD")
url_or_f_name = input("Enter information here: ")
if (len(url_or_f_name) < 1) :
    url_or_f_name = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"

isURL = False
if url_or_f_name.strip().lower().startswith("http") :
    isURL = True
    ssl_ctx = ssl.create_default_context()
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = ssl.CERT_NONE

try:
    if (isURL) :
        url_or_f_handle = urllib.request.urlopen(url_or_f_name, context=ssl_ctx)
    else :
        url_or_f_handle= open(url_or_f_name)
except:
    print("Erro: Could not locate file,", url_or_f_name)
    quit()

many = 0
count = -1
fail = 0

for data_csv_row in url_or_f_handle:
    # -1 : Header row
    if (count < 0) :
        count += 1
        continue

    data_csv_row_split = data_csv_row.decode().split(",")

    try:
        cur.execute('''INSERT OR IGNORE INTO raw_ev_population_data (
                vin,
                country,
                city,
                state,
                postal_code,
                model_year,
                make,
                model,
                ev_type,
                cafv_eligibility,
                electric_range,
                base_mrsp,
                legislative_district,
                dol_vehicle_id,
                vehicle_location,
                vehicle_utility,
                census_track_2020
            )
            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', 
            ( 
                data_csv_row_split[0],
                data_csv_row_split[1],
                data_csv_row_split[2],
                data_csv_row_split[3],
                data_csv_row_split[4],
                data_csv_row_split[5],
                data_csv_row_split[6],
                data_csv_row_split[7],
                data_csv_row_split[8],
                data_csv_row_split[9],
                data_csv_row_split[10],
                data_csv_row_split[11],
                data_csv_row_split[12],
                data_csv_row_split[13],
                data_csv_row_split[14],
                data_csv_row_split[15],
                data_csv_row_split[16]
            ))
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Error: Insert into table raw_ev_population_data failed at file line (including header if header exists)", count+2)
        fail += 1

    count += 1

    if fail >= 5 : break
    if count % 1000 == 0 :
        print("Loaded,", count, "records.")
        conn.commit()
    # if count % 100 == 0 : time.sleep(1)

conn.commit()
cur.close()
