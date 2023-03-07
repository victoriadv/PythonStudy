from models import Plant, Employee, Salon

while True:
    print("1. Add Plant\n2. Gel all plants\n3. Add Employee\n4. Get all employees\n5. Update employee"
          "\n6. Update Plant\n7. Add Salon\n8. Get all salons\n9. Update salon\n")
    flag = int(input("Choose menu item: "))
    if flag == 1:
        name = input("Plant name: ")
        address = input("Plant address: ")
        plant = Plant(name, address)
        plant.save()
    elif flag == 2:
        Plant.get_all()
    elif flag == 3:
        name = input("Employee name: ")
        email = input("Employee email: ")
        type_place = input("Type of workplace: ")
        place_id = int(input("Workplace id: "))
        employee = Employee(name, email, type_place, place_id)
        employee.save()
    elif flag == 4:
        Employee.get_all()
        print("1. Get information about the employee's place of work\n2. Skip\n")
        new_flag = int(input("Choose menu item: "))
        if new_flag == 1:
            id = int(input("Input employee's id: "))
            Employee.get_info_about_work(id)
        elif new_flag == 2:
            continue
        else:
            print("Wrong input\n")
            continue
    elif flag == 5:
        try:
            id = int(input("Id which employee you want to update: "))
            employee = Employee.get_el_by_id(id)
            employee.update()
        except AttributeError:
            continue
    elif flag == 6:
        try:
            id = int(input("Id which plant you want to update: "))
            plant = Plant.get_el_by_id(id)
            plant.update()
        except AttributeError:
            continue
    elif flag == 7:
        name = input("Salon name: ")
        address = input("Salon address: ")
        salon = Salon(name, address)
        salon.save()
    elif flag == 8:
        Salon.get_all()
    elif flag == 9:
        try:
            id = int(input("Id which salon you want to update: "))
            salon = Salon.get_el_by_id(id)
            salon.update()
        except AttributeError:
            continue
    else:
        print("No this menu item\n")