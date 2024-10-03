import csv
import json
import xml.etree.ElementTree as ET

# Custom exception for unsupported file formats
class UnsupportedFileFormatError(Exception):
    """Custom exception for unsupported file formats."""
    pass

# Function to process CSV files
def process_csv(input_file, output_file, age_threshold):
    try:
        print(f"Opening CSV file")
        with open(input_file, mode='r', newline='') as infile:
            reader = csv.DictReader(infile)
            print(f"Filtering the rows > {age_threshold}.")

            with open(output_file, mode='w', newline='') as outfile:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                filtered_rows = 0

                for row in reader:
                    if int(row['Age']) > age_threshold:
                        writer.writerow(row)
                        filtered_rows += 1

        print(f"Filtered rows = {filtered_rows}")
        print(f"Output is in '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("------------------------------------------------------------------------------------")

# Function to process JSON files
def process_json(input_file, output_file, age_threshold):
    try:
        print(f"Opening JSON file")
        with open(input_file, mode='r') as infile:
            data = json.load(infile)
            print(f"Filtering the data > {age_threshold}.")
            
            filtered_data = [record for record in data if int(record['Age']) > age_threshold]

            with open(output_file, mode='w') as outfile:
                json.dump(filtered_data, outfile, indent=4)
        
        print(f"Filtered records = {len(filtered_data)} records.")
        print(f"Output written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("------------------------------------------------------------------------------------")

# Function to process XML files
def process_xml(input_file, output_file, age_threshold):
    try:
        print(f"Opening XML file")
        tree = ET.parse(input_file)
        root = tree.getroot()

        print(f"Filtering the data > {age_threshold}.")
        removed_count = 0
        for person in root.findall('person'):
            age = int(person.find('age').text)
            if age <= age_threshold:
                root.remove(person)
                removed_count += 1

        # Writing the filtered XML back to output
        tree.write(output_file)
        print(f"Removed elements = {removed_count}")
        print(f"Output written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("------------------------------------------------------------------------------------")

# Main function to determine the file format and process accordingly
def process_file(input_file, output_file, age_threshold, file_format):
    try:
        print(f"Starting file processing for format: {file_format.upper()}")
        if file_format == 'csv':
            process_csv(input_file, output_file, age_threshold)
        elif file_format == 'json':
            process_json(input_file, output_file, age_threshold)
        elif file_format == 'xml':
            process_xml(input_file, output_file, age_threshold)
        else:
            raise UnsupportedFileFormatError(f"Unsupported file format: {file_format}")

    except UnsupportedFileFormatError as e:
        print(e)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Get user input for file paths and age threshold
    csv_input = input("Enter the path for the CSV input file: ")
    csv_output = input("Enter the path for the CSV output file: ")
    
    json_input = input("Enter the path for the JSON input file: ")
    json_output = input("Enter the path for the JSON output file: ")

    xml_input = input("Enter the path for the XML input file: ")
    xml_output = input("Enter the path for the XML output file: ")

    # Get the age threshold from the user
    age_threshold = int(input("Enter the age threshold for filtering: "))

    # Process files with the user-defined age threshold
    process_file(csv_input, csv_output, age_threshold, file_format='csv')
    process_file(json_input, json_output, age_threshold, file_format='json')
    process_file(xml_input, xml_output, age_threshold, file_format='xml')
