# Data

## Source

The data comes from the CelesTrak Satellite Catalog (SATCAT).

* Main page: https://celestrak.org/satcat/
* Raw CSV used here: https://celestrak.org/pub/satcat.csv
* Column documentation: https://celestrak.org/satcat/satcat-format.php

SATCAT is a public catalogue of every object that the US Space Force has tracked
in orbit since Sputnik in 1957. CelesTrak publishes it for free and updates it
daily.

## Download date

The file in this folder was downloaded on **24 September 2026** and is saved as
`satcat_2026-09-24.csv`. It has 70,793 rows, one row per tracked object.

The CSV files are not committed to git because they are quite large and anyone
can download a fresh copy. To get the data again, run:

```bash
python scripts/download_satcat.py
```

That saves a new file with today's date in the name. If you use a newer file,
the exact numbers in the notebook will change a little because new objects get
launched and old ones fall back to Earth.

## Columns

| Column | What it means |
| --- | --- |
| OBJECT_NAME | Name of the object, for example "ISS (ZARYA)" |
| OBJECT_ID | International designator, for example 1998-067A |
| NORAD_CAT_ID | Catalogue number given by NORAD |
| OBJECT_TYPE | PAY (payload), R/B (rocket body), DEB (debris), UNK (unknown) |
| OPS_STATUS_CODE | Operational status, only filled in for payloads |
| OWNER | Country or organisation that owns the object |
| LAUNCH_DATE | Date of launch |
| LAUNCH_SITE | Code of the launch site, for example AFETR |
| DECAY_DATE | Date the object came back into the atmosphere, empty if still in orbit |
| PERIOD | Time for one orbit in minutes |
| INCLINATION | Angle of the orbit against the equator in degrees |
| APOGEE | Highest point of the orbit in km |
| PERIGEE | Lowest point of the orbit in km |
| RCS | Radar cross section in square metres, roughly how big the object looks on radar |
| DATA_STATUS_CODE | Says if the orbit data is incomplete |
| ORBIT_CENTER | Which body the object orbits, EA means Earth |
| ORBIT_TYPE | ORB, LAN, IMP, DOC or R/T |

`OBJECT_TYPE` is the column I try to predict.

## Licence and terms

CelesTrak data is free to use. See https://celestrak.org/ for their terms.
