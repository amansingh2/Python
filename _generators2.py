"""
Practical Example: Processing a Large File
This is where generators really shine.
A generator can read a file line by line without loading the entire file into memory.
"""

def func():
    def read_large_file(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                yield line.strip()

    # Assume 'large_data.txt' is a huge file
    # Let's simulate a large file for the example
    with open('large_data.txt', 'w') as f:
        for i in range(1000000):
            f.write(f"Line {i}\n")

    # Process the file using the generator
    line_generator = read_large_file('large_data.txt')

    # Now you can iterate over the lines efficiently
    first_10_lines = [next(line_generator) for _ in range(10)]
    print(first_10_lines)

"""
In this implementation, the read_large_file function becomes a generator. 
It yields one line at a time, making it highly memory-efficient for processing very large files.
"""

if __name__ == "__main__":
    func()