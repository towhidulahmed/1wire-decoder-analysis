import csv
from typing import List, Tuple

def read_csv(file_path: str) -> List[Tuple[float, int]]:
    data = []
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            time, value = float(row[0]), int(row[1])
            data.append((time, value))
    return data

def decode_signal(data: List[Tuple[float, int]]) -> str:
    binary_data = ""
    low_pulse_start = None

    for i, (time, value) in enumerate(data):
        if value == 0 and low_pulse_start is None:
            low_pulse_start = time
        elif value == 1 and low_pulse_start is not None:
            pulse_duration = (time - low_pulse_start) * 1e6  # Convert to microseconds
            if 3 <= pulse_duration <= 7:
                binary_data += "1"
            elif pulse_duration > 11:
                binary_data += "0"
            low_pulse_start = None

    return binary_data

def binary_to_hex(binary_string: str) -> str:
    return hex(int(binary_string, 2))[2:].upper().zfill(2)  # Ensure 2 digits

def process_file(file_path: str) -> List[str]:
    data = read_csv(file_path)
    binary_data = decode_signal(data)
    
    chunk_size = 8
    hex_chunks = []
    for i in range(0, len(binary_data), chunk_size):
        chunk = binary_data[i:i+chunk_size]
        if len(chunk) == 8:
            reversed_chunk = chunk[::-1]
            hex_chunk = binary_to_hex(reversed_chunk)
            hex_chunks.append(hex_chunk)
    
    return hex_chunks

def find_pattern_positions(hex_chunks: List[str], pattern: str) -> List[int]:
    pattern_hex = ''.join([hex(ord(c))[2:].upper().zfill(2) for c in pattern])
    pattern_length = len(pattern_hex) // 2
    positions = []
    
    for i in range(len(hex_chunks) - pattern_length + 1):
        if ''.join(hex_chunks[i:i+pattern_length]) == pattern_hex:
            positions.append(i)
    
    return positions

def compare_files(files: List[str]):
    all_hex_chunks = []
    for file in files:
        hex_chunks = process_file(file)
        all_hex_chunks.append(hex_chunks)
        print(f"\nFile: {file}")
        print(f"Total bytes: {len(hex_chunks)}")
        
        pattern = "V1004261"
        positions = find_pattern_positions(hex_chunks, pattern)
        print(f"Positions of '{pattern}': {positions}")

    # Compare similarities
    min_length = min(len(chunks) for chunks in all_hex_chunks)
    
    print("\nComparing similarities:")
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            similarities = sum(all_hex_chunks[i][k] == all_hex_chunks[j][k] for k in range(min_length))
            similarity_percentage = (similarities / min_length) * 100
            print(f"{files[i]} vs {files[j]}:")
            print(f"  Similar bytes: {similarities}")
            print(f"  Similarity percentage: {similarity_percentage:.2f}%")

    print("\nUnique hex codes in each file:")
    for i, file in enumerate(files):
        unique_hex = set(all_hex_chunks[i]) - set.union(*[set(chunks) for j, chunks in enumerate(all_hex_chunks) if j != i])
        print(f"{file}: {', '.join(unique_hex)}")

def main():
    files = ["data/sample_csvs/t1.csv", "data/sample_csvs/t4.csv"] #select files to decode and compare bytes
    compare_files(files)

if __name__ == "__main__":
    main()