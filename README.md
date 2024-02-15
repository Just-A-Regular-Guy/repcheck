# RepCheck

Repcheck is a Python script that checks the reputation of IP addresses using the VirusTotal API. It reads a list of IP addresses from a file, sends a request to the VirusTotal API for each IP address, and writes the results to a CSV file.

## Prerequisites

- Python 3.x
- The `requests` package (can be installed with `pip install requests`)
- A text file containing a list of IP addresses, one per line
- A VirusTotal API key (you can get one for free by signing up at https://www.virustotal.com/)

## Usage

1. Clone this repository:
git clone https://github.com/Just-A-Regular-Guy/repcheck

2. Change to the directory containing the script:
cd repcheck

3. Run the script, passing the filename of your IP address list as an argument:
python3 repcheck.py <filename>

Replace `<filename>` with the name of your text file containing the IP addresses.

4. The script will output a CSV file named `out_ips.csv`, containing the IP addresses and their corresponding reputation scores.

## License

This project is licensed - see the https://github.com/Just-A-Regular-Guy/repcheck/edit/main/LICENSE file for details.
