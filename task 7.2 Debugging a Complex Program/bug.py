import csv
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def read_and_process_csv(input_file, output_file):
    valid_rows = []  # List to hold valid data rows
    logging.debug(f'Reading data from {input_file}')
    
    try:
        with open(input_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                item = row[0]
                sales = row[1]  # No stripping of whitespace
                
                # Check if the sales value is empty
                if sales == '':
                    logging.warning(f'Row does not contain enough data: {row}')
                    continue
                
                # Try to convert sales to float
                sales_value = float(sales)  # This will raise ValueError if sales is invalid
                valid_rows.append((item, sales_value))  # Store valid item and sales

    except FileNotFoundError:
        logging.error(f'The file {input_file} was not found.')
        return
    except Exception as e:
        logging.error(f'An error occurred: {e}')

    # Attempt to write valid rows to the output CSV
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item', 'Sales'])  # Write header
        writer.writerows(valid_rows)  # Write valid data

# Specify input and output file names
input_file = 'data.csv'  # Name of your input CSV file
output_file = 'valid_results.csv'  # Name of the output CSV file

# Call the function
read_and_process_csv(input_file, output_file)
