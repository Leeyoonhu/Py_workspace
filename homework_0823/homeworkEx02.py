line_counter = 0
header_list = []
doctor = []
doctor_subject = []

with open("c:/temp/license.applier.csv", "r") as doctor_data:
    while True:
        data = doctor_data.readline()
        if data == "":
            break
        if line_counter == 0:
            header_list = data.split(",")
        else:
            doctor = data.split(",")
            if doctor[4].__contains__("의학총론"):
                doctor_subject.append(doctor)
        line_counter += 1

with open("c:/temp/intro_score.csv", "w") as doctor_subject_File:
    for doctor in doctor_subject:
        doctor_subject_File.write(",".join(doctor) + "\n")
