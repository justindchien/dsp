import csv
with open ("emails.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for email in emails:
        writer.writerow([email])
