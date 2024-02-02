import csv

# Initialize empty lists to store ABE and CBE editable protospacers
abe_editable_protospacers = []
cbe_editable_protospacers = []

# Read the CSV file
file_path = '/Users/koppikarps/Python Development/saturation_mutagenesis_be/APOEexon4.saturation_mutagenesis_protospacers.2024-02-02.csv'
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        protospacer = row['protospacer']
        position = int(row['position'])  # Convert position to integer
        run_type = row['run_type']

        # Check if the protospacer is 20 characters long
        # Possible efficient edit window determined from  https://doi.org/10.1038/s41587-019-0193-0 Figure 5b
        # Checks for possible edit at position 4/5/6 and if a like base pair is directly adjacent
        if len(protospacer) == 20:
            fifth_char = protospacer[4]

            # Check the 5th character to determine ABE or CBE editable
            if fifth_char == 'C':
                # Filter out protospacers with the same character immediately to the left or right
                if protospacer[3] != 'C' and protospacer[5] != 'C':
                    cbe_editable_protospacers.append({'protospacer': protospacer, 'position': position, 'run_type': run_type, 'edit_pos': 5})
            elif fifth_char == 'A':
                # Filter out protospacers with the same character immediately to the left or right
                if protospacer[3] != 'A' and protospacer[5] != 'A':
                    abe_editable_protospacers.append({'protospacer': protospacer, 'position': position, 'run_type': run_type, 'edit_pos': 5})

            fourth_char = protospacer[3]

            # Check the 4th character to determine ABE or CBE editable
            if fourth_char == 'C':
                # Filter out protospacers with the same character immediately to the left or right
                if protospacer[2] != 'C' and protospacer[4] != 'C':
                    cbe_editable_protospacers.append({'protospacer': protospacer, 'position': position, 'run_type': run_type, 'edit_pos': 4})
            elif fourth_char == 'A':
                # Filter out protospacers with the same character immediately to the left or right
                if protospacer[2] != 'A' and protospacer[4] != 'A':
                    abe_editable_protospacers.append({'protospacer': protospacer, 'position': position, 'run_type': run_type, 'edit_pos': 4})

            sixth_char = protospacer[5]

            # Check the 5th character to determine ABE or CBE editable
            if sixth_char == 'C':
                # Filter out protospacers with the same character immediately to the left or right
                if protospacer[4] != 'C' and protospacer[6] != 'C':
                    cbe_editable_protospacers.append({'protospacer': protospacer, 'position': position, 'run_type': run_type, 'edit_pos': 6})
            elif sixth_char == 'A':
                # Filter out protospacers with the same character immediately to the left or right
                if protospacer[4] != 'A' and protospacer[6] != 'A':
                    abe_editable_protospacers.append({'protospacer': protospacer, 'position': position, 'run_type': run_type, 'edit_pos': 6})


# Write the results to two separate CSV files
abe_file_path = 'abe_editable_protospacers_APOEexon4.csv'
cbe_file_path = 'cbe_editable_protospacers_APOEexon4.csv'

# Function to write rows with headers
def write_csv(file_path, data, headers):
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(data)

# Write ABE editable protospacers to CSV
abe_headers = ['protospacer', 'position', 'run_type', 'edit_pos']
write_csv(abe_file_path, abe_editable_protospacers, abe_headers)

# Write CBE editable protospacers to CSV
cbe_headers = ['protospacer', 'position', 'run_type', 'edit_pos']
write_csv(cbe_file_path, cbe_editable_protospacers, cbe_headers)

