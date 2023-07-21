import csv

#field names

fields = ["Customer", "Issue", "point_contact"]


filename = "future_cfd.csv"

rows = [ ["customer1","Issue1", "point_of_contact1"]]


with open(filename, "w") as csvfile:

    csvwriter = csv.writer(csvfile)

    # writing the fields

    csvwriter.writerow(fields)

    # witing the data rows

    csvwriter.writerows(rows)




