import csv
import datetime
from Bio.Seq import Seq

def process_sequence(sequence_lines, position, ps_result_list, run_type):
    sequence = ''.join(sequence_lines).strip()  # Strip newline characters
    sequence = Seq(sequence)

    pam_positions = []

    # Check for PAM positions across the entire sequence
    pam = ['GG', 'AG', 'CG', 'TG']
    for i in range(len(sequence) - 1):
        current_subsequence = sequence[i:i+2]
        if current_subsequence in pam:
            pam_positions.append((current_subsequence, i))
            print(f"{current_subsequence} found at position {i} in the sequence.")

    for pam, position in pam_positions:
        # Calculate the protospacer sequence (20 bases before the PAM)
        protospacer_start = max(0, position - 20)  # Ensure not to go beyond the beginning of the sequence
        protospacer = sequence[protospacer_start:position]

        # If the protospacer doesn't start with a G, make it start with a G to promote transcription
        if protospacer[0] != "G":
            protospacer = 'G' + protospacer[1:]

        # Store rsid-result pairs with PAM positions, corresponding protospacers, and run type
        # The position number is the number before the PAM begins, after the PS ends
        if run_type == 'reverse':
            adjusted_position = len(sequence) - position
        else:
            adjusted_position = position

        ps_result_list.append((adjusted_position, protospacer, run_type))

        print(f"Protospacer at position {adjusted_position} in {run_type} run: {protospacer}")

def reverse_complement_sequence(sequence_lines, position, ps_result_list):
    # Reverse complement the entire sequence at once
    reversed_sequence = Seq(''.join(sequence_lines).strip()).reverse_complement()

    # Process the reversed sequence with adjusted positions
    process_sequence([str(reversed_sequence)], position, ps_result_list, run_type='reverse')

# Initialize a list to store result pairs
ps_result_list = []
position = []

file_path = '/Users/koppikarps/Python Development/saturation_mutagenesis_be/test.txt'

try:
    with open(file_path, 'r') as file:
        sequence_lines = [line.strip() for line in file]  # Strip newline characters

        for line in sequence_lines:
            print(line)

        print("Processing forward sequence...")
        process_sequence(sequence_lines, position, ps_result_list, run_type='forward')

        print("Processing reverse complement sequence...")
        reverse_complement_sequence(sequence_lines, position, ps_result_list)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Export results to a CSV file
dt_today = datetime.date.today()
output_file = f'test.saturation_mutagenesis_protospacers.{dt_today}.csv'
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['position', 'protospacer', 'run_type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for position, protospacer, run_type in ps_result_list:
        writer.writerow({
            'position': position,
            'protospacer': protospacer,
            'run_type': run_type,
        })

print(f"Results exported to '{output_file}'")
