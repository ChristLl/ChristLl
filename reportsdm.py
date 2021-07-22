#!/usr/bin/python3


import csv

# XSOARFILENAME = "./xsoar.csv" #Fichier généré dans XSOAR, non utilisé ici
SFFILENAME = "./sf.csv"  # Fichier généré dans XSOAR
SPLUNKFILENAME = "./splunk.csv"  # Fichier envoyé par Maxime chaque jour
FINALFILENAME = "./export_sdm.csv"  # Fichier que le script génere
SEVERITY_MAPPING = {"1": "LOW", "2": "MEDIUM", "3": "HIGH","4": "CRITICAL"}
SPLUNK_SEVERITY_MAPPING = {"4": "LOW", "3": "MEDIUM", "2": "HIGH","1": "CRITICAL"}

xsoar = []
sf = []
splunk = []
notable_id = ""

# xsoarfile = csv.DictReader(open(XSOARFILENAME), delimiter=',')

# Lit le fichier SFFILENAME et copy les données dans une list sf
sffile = csv.DictReader(open(SFFILENAME), delimiter=',')
for row in sffile:
    sf.append(
        {
            "XSOAR Id": row["XSOAR Id"],
            "SF Ticket Number": row["SF Ticket Number"],
            "Jira Ticket Id": row["Jira Ticket Id"],
            "Severity": row["Severity"],
            "Events Id Splunk": row["Events Id Splunk"],
            "Notable ID": row["Notable ID"]
        }
    )
print(len(sf))

# Fielnames contient les colonnes du nouveau fichier CSV FINALFILENAME
fieldnames = ["alert_time_utc", "alert_reference_id", "rule_name", "alert_arg_lastcomment", "alert_rule_type",
              "alert_notable_id", "SPLUNK Rule Priority","status_label", "XSOAR Id", "XSOAR Severity", "SF Ticket Number", "Jira Ticket Id", "Notable ID"]
# Creer le fichier FINALFILENAME puis ajoute les noms des colonnes
writer = csv.DictWriter(open(FINALFILENAME, 'w', newline=''), fieldnames=fieldnames)
writer.writeheader()

# Ouvre fichier SPLUNKFILENAME
splunkfile = csv.DictReader(open(SPLUNKFILENAME, newline=''), delimiter=',')
"alert_time_utc","reference_id","rule_name","arg_lastcomment","rule_type","rule_priority","event_id","status_label"
# Boucle sur toutes les lignes de la liste (provenant du fichier de Maxime)
for row in splunkfile:
    found = False
    for row3 in sf:
        if row3["Events Id Splunk"] == row["event_id"]:
            writer.writerow({"alert_time_utc": row["alert_time_utc"],
                             "alert_reference_id": row["reference_id"],
                             "rule_name": row["rule_name"],
                             "alert_arg_lastcomment": row["arg_lastcomment"],
                             "alert_rule_type": row["rule_type"],
                             "alert_notable_id": row["event_id"],
                             "SPLUNK Rule Priority": SPLUNK_SEVERITY_MAPPING[row["rule_priority"]],
                             "status_label": row["status_label"],
                             "XSOAR Severity": SEVERITY_MAPPING[row3["Severity"]],
                             "XSOAR Id": row3["XSOAR Id"],
                             "SF Ticket Number": row3["SF Ticket Number"],
                             "Jira Ticket Id": row3["Jira Ticket Id"],
                             "Notable ID": row3["Notable ID"]
                             })
            found = True
    if not found:
        writer.writerow({
            "alert_time_utc": row["alert_time_utc"],
            "alert_reference_id": row["reference_id"],
            "rule_name": row["rule_name"],
            "alert_arg_lastcomment": row["arg_lastcomment"],
            "alert_rule_type": row["rule_type"],
            "alert_notable_id": row["event_id"],
            "SPLUNK Rule Priority": SPLUNK_SEVERITY_MAPPING[row["rule_priority"]],
            "status_label": row["status_label"],
            "XSOAR Severity": "",
            "XSOAR Id": "",
            "SF Ticket Number": "",
            "Jira Ticket Id": "",
            "Notable ID": 0
        }),

print("Report sdm created")