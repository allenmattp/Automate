#! python3
# censusProject.py - Tabulates pop and number of census tracts for each county

import openpyxl, pprint

# uncomment to create file
"""
print("Opening workbook ...")

wb = openpyxl.load_workbook("censuspopdata.xlsx")
sheet = wb.active                                       # only one worksheet

countyData = {}

# Fill in countyData with each county's pop and tracts
print("Reading rows ...")
for row in range(2, sheet.max_row + 1):                 # first row is header, wb index starts at 1
    # each row has data for one census tract
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value

    # make sure key for this state exists
    countyData.setdefault(state, {})
    # make sure key for county in this state exists
    countyData[state].setdefault(county, {"tracts": 0, "pop": 0})

    # each row represents one census tract
    countyData[state][county]["tracts"] += 1
    # increase the county pop by the pop in this census tract
    countyData[state][county]["pop"] += int(pop)

# Open a new file and write the contents of countyData to it

with open("census2010.py", "w") as f:
    f.write("allData = " + pprint.pformat(countyData))
    f.close()

print("Done.")
"""

# once census2010 created, import and call data for different counties
import census2010


print(census2010.allData["AK"]["Anchorage"])
print(census2010.allData["WA"]["King"])
print(census2010.allData["MN"]["Hennepin"])
print(census2010.allData["MA"]["Suffolk"])