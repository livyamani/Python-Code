import csv
import logging

# Configure logging to display messages
logging.basicConfig(level=logging.DEBUG)

def read_and_process_csv(input_file, output_file):
    valid_rows = []  # List to hold valid data rows
    logging.debug(f'Reading data from {input_file}')
    
    try:
        with open(input_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                # Check if the row is empty
                if not row:  # If the row is empty
                    logging.warning('Encountered an empty row, skipping...')
                    continue

                try:
                    item = row[0]
                    sales = row[1].strip()  # Remove leading/trailing whitespace
                    
                    # Check if the sales value is empty
                    if not sales:
                        logging.warning(f'Row does not contain enough data: {row}')
                        continue
                    
                    # Try to convert sales to float
                    sales_value = float(sales)
                    valid_rows.append((item, sales_value))  # Store valid item and sales

                except ValueError as e:
                    logging.error(f'Invalid value in sales data: {row[1]} ({e})')

    except FileNotFoundError:
        logging.error(f'The file {input_file} was not found.')
        return
    
    # Write valid rows to the output CSV
    if valid_rows:
        logging.debug(f'Saving valid results to {output_file}')
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item', 'Sales'])  # Write header
            writer.writerows(valid_rows)  # Write valid data
    else:
        logging.error('No valid sales data to process.')

# Specify input and output file names
input_file = 'data.csv'       # Name of your input CSV file
output_file = 'valid_results.csv'  # Name of the output CSV file

# Call the function to process the CSV
read_and_process_csv(input_file, output_file)
