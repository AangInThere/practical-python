# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(col) for col in select]
                headers = select


        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            if select:
                row = [row[i] for i in indices]
            if types:
                row = [type(element) for type, element in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
