parking_data = [
    ("A1", "MH12 FM 9337", "2024-02-14 15:23:07", "None", 1),
    ("A2", "None", "None", "None", 0),
    ("A3", "None", "None", "None", 0),
    ("A4", "None", "None", "None", 0),
    ("A5", "None", "None", "None", 0)
]

print("************************************************************************")
print("{:<15} {:<15} {:<20} {:<15} {:<15}".format(
    "PARKING ID", "VEHICLE NO", "ENTRY TIME", "EXIT TIME", "PARKING STATUS"))
for parking_id, vehicle_no, entry_time, exit_time, parking_status in parking_data:
    print("'{:<15}' '{:<15}' '{:<20}' '{:<15}' {:<15}".format(data[0],data[1],data[2],data[3],data[4]))
print("************************************************************************")