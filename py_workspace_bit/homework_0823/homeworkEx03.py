line_counter = 0
header_list = []
person = []
person_male20 = []

with open("c:/temp/icu_stat.csv", "r") as person_data:
    while True:
        data = person_data.readline()
        if data == "":
            break
        if line_counter == 0:
            header_list = data.split(",")
        else:
            person = data.split(",")
            if person[1] == "남":
                if person[2].__contains__("2"):
                    person_male20.append(person)
        line_counter += 1

with open("c:/temp/male_20.csv", "w") as person_male20_File:
    for person in person_male20:
        person_male20_File.write(",".join(person) + "\n")
