from ReportSlunkSFDem import convert_nordics_file, convert_to_csv, reportsdm, csv_to_xls

list_files = ["convert_nordics_file", "convert_to_csv.py", "reportsdm.py", "csv_to_xls.py"]

for files in list_files:
    try:
        files
        print(files+" ok")
    except:
        print(files+"Error")

