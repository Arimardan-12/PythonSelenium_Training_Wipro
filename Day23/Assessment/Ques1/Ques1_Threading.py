
import requests
import threading
import time

urls = [
    "https://www.mozilla.org",
    "https://www.apple.com",
    "https://www.wikipedia.org",
    "https://stackoverflow.com"
]

# Add browser-like header (important for real websites)
headers = {
    "User-Agent": "Mozilla/5.0"
}

def downloadfiles(url, index):
    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            filename = f"site_{index}.txt"   # FIXED filename
            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)

            print(f"Downloaded: {filename}")
        else:
            print(f"Failed {url} - Status {response.status_code}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")


# ---------------- SEQUENTIAL ----------------
starttime = time.time()

for i, url in enumerate(urls):
    downloadfiles(url, i+1)

sequentialtime = time.time() - starttime
print(f"\nSequential download time: {sequentialtime:.2f} seconds")


# ---------------- THREADING ----------------
threads = []
starttime1 = time.time()

for i, url in enumerate(urls):
    thread = threading.Thread(target=downloadfiles, args=(url, i+1))
    threads.append(thread)
    thread.start()

# IMPORTANT → wait for all threads to finish
for thread in threads:
    thread.join()

threadingtime = time.time() - starttime1
print(f"\nThreading download time: {threadingtime:.2f} seconds")
