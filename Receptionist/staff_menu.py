from staff_registration import Staff

class StaffMenu:

    @staticmethod
    def run():
        while True:
            print("\n*** Staff Menu ***")
            print("1. Register Staff")
            print("2. Find Staff")
            print("3. Update Staff")
            print("4. Back")

            choice = input("Select option: ")

            if choice == "1":
                Staff.register_staff()

            elif choice == "2":
                staff_id = input("Staff ID: ")
                staff = Staff.get_staff_by_staff_id(staff_id)
                if not staff:
                    print("Not found.")
                else:
                    print("Staff found")
                    print(staff)

            elif choice == "3":
                staff_id = input("Staff ID: ")
                staff = Staff.get_staff_by_staff_id(staff_id)

                if not staff:
                    print("Not found.")
                    continue

                print("Leave a blank to keep current value")
                
                updated = {
                    "name": input("Name: "),
                    "age": int(input("Age: ")),
                    "gender": input("Gender: "),
                    "contact": input("Contact: "),
                    "staff_id": staff_id
                }

                Staff.update_staff_details(updated)

            elif choice == "4":
                break

if __name__ == "__main__":
    StaffMenu.run()