import json

md = open("result.md", "w")

systemHasPandoc = False
metatags = r'''
---
geometry: "left=2.54cm,right=2.54cm,top=3cm,bottom=3cm"
output: pdf_document
fontsize: 12pt
colorlinks: true
papersize: a4
stretch: 1.5
header-includes: |
    \usepackage{setspace}
    \usepackage{fancyhdr}
    \usepackage[most]{tcolorbox}
    \usepackage{cascadia-code}
    \pagestyle{fancy}
    \fancyfoot[R]{\thepage}
---
'''

header = '''
### Sem-5 Result Jan 2024

> Scrapper link:
[https://github.com/blucin/result-scraper-cvmu](https://github.com/blucin/result-scraper-cvmu)

### Overall Result

| Rank | Name | SGPA | CGPA |
| --- | --- | --- | --- |
'''

if systemHasPandoc:
    md.write(metatags)
md.write(header)

# data is already sorted by rank
with open("result_data.json", "r") as jsonfile:
    data = json.load(jsonfile)
    for student in data:
        rank = student["rank"]
        name = student["student_name"]
        sgpa = student["sgpa"]
        cgpa = student["cgpa"]
        # write to markdown file
        md.write("| " + str(rank) + " | " + name + " | " + sgpa + " | " + cgpa + " |\n")

footer = '''
> Note: subject wise grades are not included in this table. JSON file contains all the data.
'''
md.write(footer)
md.close()