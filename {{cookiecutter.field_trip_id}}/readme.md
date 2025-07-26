## field_trip_id : {{cookiecutter.field_trip_id}}
## project_name  : {{cookiecutter.project_name}}
## Institution   : {{cookiecutter.institution}}
## start_date    : {{cookiecutter.start_date}}
## end_date      : {{cookiecutter.end_date}}
## custodian     : {{cookiecutter.custodian}}
## email         : {{cookiecutter.email}}
## time_zone     : {{cookiecutter.time_zone}}



## Directory Structure

```
{{cookiecutter.field_trip_id}}/
├── 00_metadata/          # Directory containing metadata for the trip
│   └── camerabars.csv    # Holds the names and serial numbers of cameras
│   └──opdata.csv         # Holds the metadata about each deployment
├── 01_fielddata/         # holds raw BRUV videos and voyage data
│   └── BRUV_memory_cards # Holds all downloads of BRUV memory cards
│   └── GPS_tracks        # Holds all gps tracks for the vessel
│   └── Log_sheets        # Holds pictures of daily log sheets
├── 02_staging/           # Holds videos that are waiting to be QC
├── 03_Deployments/       # Holds videos that are renamed and ready for analysis
├── 04_eventmeasure/      # Holds files associated with EventMeasure
│   └── calibration/      # Directory containing calibration files
│           └── pre/      # Pre trip calibration files
│           └── post/     # Post trip calibration files
├── 05_reports/           # Holds processing reports
├── docs/                 # Project documentation (this file)
├── fieldtrip.yml         # Field trip configuration file
├── gopro_config.yml      # Specific configuration files for gopro
├── import.yml            # Template file for SDCards
└── readme.md             # Project instructions
```

## Description

This project template provides a structured starting point for your field trip project. Below is an overview of the actual directory structure and the purpose of each folder/file.

---

Feel free to modify this structure to fit your project's needs!
