# import libraries
import pandas as pd
import glob
import argparse
from pathlib import Path


# creating a user-defined function to read csv files
def file_reader(filename):
    """This function reads csv files, extracts the filename from the path and creates a new column with the filename"""
    header = True  # header is set to true to include the header name from the file
    for file in filename:
        df = pd.read_csv(file, chunksize=50, index_col=None, header=0)  # read csv files
        file_name = Path(
            file
        ).name  # using Path from Pathlib to extract the filename into a new variable
        for chunk in df:  # for loop to save chunks into csv file as its processed
            chunk["filename"] = file_name
            yield chunk.to_csv(index=False, header=header)
            header = False  # to avoid new headers with each for iteration


# Error Handling code to check if column names match in files
# if statement to check if column names are the same for input files
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Combine two or more csv files into one csv file"
    )  # description
    parser.add_argument(
        nargs="+", help="csv input files location", dest="input"
    )  # input from console as list
    args = parser.parse_args()  # parsing argument
    input_files = args.input  # instantiating input as variable

    # result
    for m in file_reader(input_files):
        print(m, end="")
