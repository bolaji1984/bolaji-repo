import csv
import argparse

def filter_rows(input_file: str, output_file: str, delimiter: str = "\t") -> None:
    """Filter rows based on column 2.

    Reads *input_file* expecting rows separated by *delimiter* and retains the
    first occurrence of each unique value in column 2. Rows whose column 2
    contains the substring ``PHAGE`` are excluded entirely.

    Parameters
    ----------
    input_file: str
        Path to the input text file.
    output_file: str
        Path where the filtered file will be written.
    delimiter: str, optional
        Delimiter used to split columns, default is tab.
    """
    seen = set()
    with open(input_file, newline="") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile, delimiter=delimiter)
        writer = csv.writer(outfile, delimiter=delimiter)
        for row in reader:
            if len(row) < 2:
                # Skip rows without at least two columns
                continue
            col2 = row[1]
            if "PHAGE" in col2:
                continue
            if col2 in seen:
                continue
            seen.add(col2)
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Remove duplicate rows based on column 2 and exclude rows containing"
            " 'PHAGE' in column 2."
        )
    )
    parser.add_argument("input_file", help="path to the input text file")
    parser.add_argument("output_file", help="path to write the filtered output")
    parser.add_argument(
        "--delimiter",
        default="\t",
        help="column delimiter in the file; default is tab",
    )
    args = parser.parse_args()
    filter_rows(args.input_file, args.output_file, args.delimiter)


if __name__ == "__main__":
    main()
