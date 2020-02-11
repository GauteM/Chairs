f = open("reservations")

rad = {}
for reservation in f:
    name, number = reservation.split(",")
    try:
        chairs_per_person = 50 / int(number)
    except ValueError:
        rad[number.strip('\n')] = name
        pass
    except ZeroDivisionError:
        rad[number.strip('\n')] = name
        pass 
    print("{} will get {} chairs per person".format(name, chairs_per_person))
print(rad)
