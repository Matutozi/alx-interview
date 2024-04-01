#!/usr/bin/python3

"""TO write a script that reads line stdin line by line"""
def process_line(line):
  """
  Parses a line in the expected format and extracts relevant data.

  Args:
      line: The line to be processed.

  Returns:
      A tuple containing (status_code, file_size) if the format is valid, 
      otherwise None.
  """
  try:
    # Split the line based on spaces
    parts = line.split()
    # Check if there are 6 parts and the request method is GET
    if len(parts) == 6 and parts[2] == 'GET':
      # Extract status code and file size
      status_code = int(parts[4])
      file_size = int(parts[5])
      return status_code, file_size
  except (ValueError, IndexError):
    # Ignore lines with invalid format
    pass
  return None

def print_statistics(total_size, status_code_counts):
  """
  Prints the total file size and status code counts.

  Args:
      total_size: The total size of all processed files.
      status_code_counts: A dictionary mapping status codes to their counts.
  """
  print(f"Total file size: {total_size}")
  print("Number of lines by status code:")
  for code, count in sorted(status_code_counts.items()):
    print(f"{code}: {count}")

# Initialize variables
total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
  # Read lines until interrupted
  while True:
    line = input()
    data = process_line(line)
    if data:
      # Valid line, update stats
      status_code, file_size = data
      total_size += file_size
      status_code_counts[status_code] += 1
      line_count += 1
      if line_count % 10 == 0:
        # Print statistics every 10 lines
        print_statistics(total_size, status_code_counts)
        # Reset line count for next batch
        line_count = 0
except KeyboardInterrupt:
  # Print statistics on interrupt
  print_statistics(total_size, status_code_counts)

print("Processing finished.")