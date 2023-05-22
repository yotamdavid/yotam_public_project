import os
import hashlib
import multiprocessing

def calculate_md5(file_path):
    with open(file_path, 'rb') as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
        return file_hash.hexdigest()

def worker(file_path):
    md5_hash = calculate_md5(file_path)
    return (file_path, md5_hash)

def calculate_md5_for_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return None

    file_list = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            file_list.append(file_path)

    with multiprocessing.Pool() as pool:
        result = pool.map(worker, file_list)

    return result

if __name__ == '__main__':
    directory_path = "C:\\Users\yotam\PycharmProjects\pythonProject1"  # Replace with the path to your directory
    file_list = calculate_md5_for_directory(directory_path)

    if file_list is not None:
        for i, (file_path, md5_hash) in enumerate(file_list, start=1):
            print(f"{i},{file_path},{md5_hash}")