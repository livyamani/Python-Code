import csv
import json
import xml.etree.ElementTree as ET
import logging
import os

# Create and configure logger
logging.basicConfig(filename="file_processing.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    filemode='a',  # Append mode
                    level=logging.DEBUG)  # Set logging level to DEBUG

# Creating an object
logger = logging.getLogger()

# Define logging functions
def log_error(message):
    logger.error(message)
    print(f"Error: {message}")

def log_info(message):
    logger.info(message)
    print(message)

def process_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            log_info(f"CSV Headers: {headers}")

            rows = [row for row in csv_reader]
            log_info("Processing CSV content:")
            for row in rows:
                log_info(row)

            # Summing numeric columns
            numeric_sums = [sum(float(col) for col in row if col.replace('.', '', 1).isdigit()) for row in rows]
            log_info(f"Sums of numeric values per row: {numeric_sums}")

    except FileNotFoundError as e:
        log_error(f"FileNotFoundError: {e}")
    except PermissionError as e:
        log_error(f"PermissionError: {e}")
    except Exception as e:
        log_error(f"Error processing CSV: {e}")

def process_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            log_info("Processing JSON content:")
            log_info(json.dumps(data, indent=4))

    except FileNotFoundError as e:
        log_error(f"FileNotFoundError: {e}")
    except PermissionError as e:
        log_error(f"PermissionError: {e}")
    except json.JSONDecodeError as e:
        log_error(f"JSONDecodeError: {e}")
    except Exception as e:
        log_error(f"Error processing JSON: {e}")

def process_xml(file_path):
    try:
        # Parse the XML file using ElementTree
        tree = ET.parse(file_path)
        root = tree.getroot()

        log_info("Processing XML content:")
        
        # Recursively print all elements and their text
        def print_element(element, indent=0):
            # Print the current element tag and text
            log_info("  " * indent + f"Tag: {element.tag}, Attributes: {element.attrib}")
            if element.text and element.text.strip():
                log_info("  " * indent + f"Text: {element.text.strip()}")

            # Recursively print children elements
            for child in element:
                print_element(child, indent + 1)

        # Call the function on the root to print the entire XML tree
        print_element(root)

    except FileNotFoundError as e:
        log_error(f"FileNotFoundError: {e}")
    except PermissionError as e:
        log_error(f"PermissionError: {e}")
    except ET.ParseError as e:
        log_error(f"ParseError: {e}")
    except Exception as e:
        log_error(f"Error processing XML: {e}")

def determine_file_type(file_path):
    if file_path.endswith('.csv'):
        process_csv(file_path)
    elif file_path.endswith('.json'):
        process_json(file_path)
    elif file_path.endswith('.xml'):
        process_xml(file_path)
    else:
        log_error(f"Unsupported file format: {file_path}")

def main():
    file_path = input("Enter the file path (CSV, JSON, XML): ").strip()
    log_info(f"Received file path: {file_path}")

    if os.path.exists(file_path):
        log_info("File exists, processing...")
        determine_file_type(file_path)
    else:
        log_error(f"File not found: {file_path}")

if __name__ == "__main__":
    main()
