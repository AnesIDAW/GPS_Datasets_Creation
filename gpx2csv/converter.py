import xml.etree.ElementTree as ET
import csv
from datetime import datetime
import argparse
from pathlib import Path

def gpx_to_csv(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()
    ns = {'default': 'http://www.topografix.com/GPX/1/1'}

    output = []
    for trkpt in root.findall('.//default:trkpt', ns):
        lat = trkpt.get('lat')
        lon = trkpt.get('lon')
        ele = trkpt.findtext('default:ele', '0', ns)
        timestamp = trkpt.findtext('default:time', None, ns)

        if timestamp:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            date_str = dt.strftime('%Y-%m-%d')
            time_str = dt.strftime('%H:%M:%S')
            excel_time = (dt - datetime(1899, 12, 30)).total_seconds() / 86400
        else:
            date_str = ''
            time_str = ''
            excel_time = ''

        output.append([lat, lon, ele, '0', excel_time, date_str, time_str])

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(output)

def main():
    parser = argparse.ArgumentParser(description="Convert GPX to CSV for GPS simulation datasets.")
    parser.add_argument("input", type=Path, help="Input GPX file path")
    parser.add_argument("output", type=Path, help="Output CSV file path")
    args = parser.parse_args()
    gpx_to_csv(args.input, args.output)

if __name__ == "__main__":
    main()

