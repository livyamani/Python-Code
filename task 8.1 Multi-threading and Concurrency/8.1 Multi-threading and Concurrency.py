import threading
import time
import requests

# Valid URLs to fetch
file_links = [
    'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY',  
    'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv',  
    'https://jsonplaceholder.typicode.com/posts',
    'https://www.gutenberg.org/files/1342/1342-0.txt',  
]


fetched_files = []
resource_lock = threading.Lock()  

# Function to fetch content from a URL
def fetch_file(link):
    try:
        response = requests.get(link, timeout=10) 
        response.raise_for_status()  
        with resource_lock:  
            fetched_files.append(response.content)
        print(f'Download complete for {link}')
    except requests.RequestException as err:
        print(f"Failed to download {link}: {err}")

# Measure time for sequential fetching
def sequential_download():
    start = time.time()
    for link in file_links:
        fetch_file(link)
    end = time.time()
    print(f'Sequential download took {end - start:.2f} seconds')

# Multi-threaded fetching function
def concurrent_download():
    threads = []
    start = time.time()
    
    for link in file_links:
        thread = threading.Thread(target=fetch_file, args=(link,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    end = time.time()
    print(f'Concurrent download took {end - start:.2f} seconds')

if __name__ == "__main__":
    # Run sequential download
    print("Starting sequential download...")
    sequential_download()
    
    # Clear the list for the next test
    fetched_files.clear()

    print("-------------------------------------------------------------------------------------")
    # Run concurrent download
    print("Starting concurrent download...")
    concurrent_download()

    # Display the total number of files downloaded
    print(f"Number of files downloaded: {len(fetched_files)}")
