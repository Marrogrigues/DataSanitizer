import re
import argparse
import shutil

def sanitize_log(input_file, output_file, backup):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\+?(\d[\d-. ]+)?(\([\d-. ]+\))?[0-9\d-. ]+\d'
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
    count_email, count_phone, count_ip = 0, 0, 0

    if backup:
        shutil.copy(input_file, f"{input_file}.bak")
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            sanitized_line = line
            sanitized_line, n = re.subn(email_pattern, 'ANONYMIZED_EMAIL', sanitized_line)
            count_email += n
            sanitized_line, n = re.subn(phone_pattern, 'ANONYMIZED_PHONE', sanitized_line)
            count_phone += n
            sanitized_line, n = re.subn(ip_pattern, 'ANONYMIZED_IP', sanitized_line)
            count_ip += n
            
            outfile.write(sanitized_line)

    print(f"Sanitization complete. Sanitized log saved to {output_file}.")
    print(f"Emails sanitized: {count_email}")
    print(f"Phone numbers sanitized: {count_phone}")
    print(f"IP addresses sanitized: {count_ip}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sanitize sensitive data in log files.')
    parser.add_argument('--input', type=str, required=True, help='Path to the input log file.')
    parser.add_argument('--output', type=str, required=True, help='Path to the output log file.')
    parser.add_argument('--backup', action='store_true', help='Create a backup of the original log file.')

    args = parser.parse_args()
    
    sanitize_log(args.input, args.output, args.backup)
