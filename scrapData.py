# CVM Result Scrapper
import requests
from bs4 import BeautifulSoup
import json
import time

base_url = "https://ums.cvmu.ac.in/GenerateResultHTML/2143/"
start = '5211001'
end = '5211060'

output = []

for i in range(int(start), int(end)+1):
    time.sleep(1) # To avoid getting blocked by the server
    page = requests.get(base_url + str(i) + ".html")
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Parsing logic
    print("Parsing data for " + str(i) + ".html")
    seat_no = soup.find_all(class_="background1")[1].find_all("td")[1].get_text()
    student_name = soup.find_all(class_="background1")[4].find_all("td")[1].get_text()
    enrollment_no = soup.find_all(class_="background1")[6].find_all("td")[1].get_text()
    subject_grades = {}
    table_rows = soup.find("table", id="mytbl").find_all("tr")[1:]
    for row in table_rows:
        course_code = row.find_all("td")[0].get_text()
        course_name = row.find_all("td")[1].get_text()
        gp = row.find_all("td")[3].get_text()
        subject_grades[course_name] = gp
    sgpa = soup.find_all(class_="background1")[9].find_all("td")[0].get_text().split(":")[1].strip()
    cgpa = soup.find_all(class_="background1")[10].find_all("td")[0].get_text().split(":")[1].strip()

    # append all the values
    output.append({
        "student_name": student_name,
        "subjects": subject_grades,
        "sgpa": sgpa,
        "cgpa": cgpa
    })
    with open("result_data.json", "w") as jsonfile:
        json.dump(output, jsonfile, indent=4)


print("Sorting data...")
with open("result_data.json", "r") as jsonfile:
    data = json.load(jsonfile)
sorted_data = sorted(data, key=lambda x: float(x["sgpa"]), reverse=True)
for i, student in enumerate(sorted_data):
    student["rank"] = i + 1

print("Writing sorted data to result_data.json")
with open("result_data.json", "w") as jsonfile:
    json.dump(sorted_data, jsonfile, indent=4)

print("Writing result to result.md")

