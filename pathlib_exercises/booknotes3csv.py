from pathlib import Path

temperature_readings  = [67, 68, 56, 67, 70, 55]

file_path = Path.home() / "temperature.txt"
with file_path.open(mode="w", encoding= "utf-8") as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:]:
        file.write(f",{temp}")

with file_path.open(mode="r", encoding= "utf-8") as file:
    text = file.read()
    #print(text)

file.close()

temperatures = text.split(",")
for i in range(len(temperatures)):
    temperatures[i] = int(temperatures[i])
    #print(temperatures)

#OR
temperatures = [int(temp) for temp in text.split(",")]
#print(temperatures)

file_path.unlink()

#now the work starts with CSV module itself
import csv

daily_temperatures = [

    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],

]

file_path = Path.home() / "temperature.csv"
#with file_path.open(mode="w", encoding= "utf-8") as file:
#    writer = csv.writer(file)
#    for temp_list in daily_temperatures:
#        writer.writerow(temp_list)

#OR
#with file_path.open(mode="w", encoding= "utf-8") as file:
with file_path.open(mode="w", newline="", encoding= "utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(daily_temperatures)
    #cleaner

file = file_path.open(mode="r", encoding="utf-8")
reader = csv.reader(file)

#for row in reader:
#    print(row)

file.close()

reopened_daily_temperatures = []
with file_path.open(mode = "r", encoding= "utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        #goes through list of lists
        int_row = [int(value) for value in row]
        #^^^^^^^^^^ goes through every item in the list using list comprehension
        reopened_daily_temperatures.append(int_row)
        #^^^^^^^^put the coverteed str>int at the back of the list

#print(reopened_daily_temperatures)

file.close()
file_path.unlink()


#################################################################################
#csv.DictReader


text_to_paste = [

    ["name","department","salary"],
    ["Lee","Operations",75000.00],
    ["Jane","Engineering",85000.00],
    ["Diego","Sales",80000.00],

]

file_path = Path.home() / "employees.csv"


with file_path.open(mode="w", newline="", encoding= "utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(text_to_paste)


file = file_path.open(mode="r", encoding="utf-8")
reader = csv.DictReader(file)
for row in reader:
    print(row)

#print(reader.fieldnames)

def process_row(row):
    #print(type(row["salary"]))
    row["salary"] = float(row["salary"])
    #print(type(row["salary"]))
    return row

with file_path.open(mode='r', encoding= 'utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(process_row(row))




file.close()
file_path.unlink()


people = [

    {"name": "Veronica", "age": 29},
    {"name": "Audrey", "age": 32},
    {"name": "Sam", "age": 24},

]

file_path = Path.home() / "people.csv"
file = file_path.open(mode="w", newline="", encoding="utf-8")
writer = csv.DictWriter(file, fieldnames=["name", "age"])   #if we don't know the keys, we can run people[0].keys() because the first row of CSV is keys

writer.writeheader() #recommended method to use to instantiate the headers only
writer.writerows(people)
file.close()    #dont forget to close otherwise, wont be able to read later
with file_path.open(mode='r', encoding= 'utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

file.close()
file_path.unlink()