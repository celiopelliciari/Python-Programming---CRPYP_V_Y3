#! /usr/bin/env python3

"""
This script imports a json data with Irish towns statistic and creates a csv file with just towns that start with 'G'
and their statistics; and other with towns that belongs to Counties that start with 'K'. Finally prints on terminal
all towns that start with 'N' and their statistics.

Uses clear variable names and concise loops for readability.

Uses simply error handling.
"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

from requests import get, exceptions
from json import load, JSONDecodeError
from csv import DictWriter
from pandas import DataFrame

# ============================================ #
# //         Download file function         // #
# ============================================ #


def download_file():
    """
    Download a json file from a static url.

    Saves the json file on the computer.
    """
    try:
        # Send a GET request to the URL
        response = get("https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CD176/JSON-stat/1.0/en")

        # Check if the request was successful (status code 200)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Define filename
        filename = "CSO.json"

        # Open the file in write binary mode
        with open(filename, "wb") as f:
            # Write the downloaded content to the file
            f.write(response.content)
            print(f"The download was successful. File saved as: {filename}")

    except exceptions.RequestException as e:  # Catch general request errors
        print(f"Error downloading file: {e}")
    except OSError as e:  # Catch potential file system errors
        raise OSError(f"Error saving file: {e}")

# ============================================ #
# //    Import JSON file to a dictionary    // #
# ============================================ #


def import_data():
    """
    Imports json file to a variable.
    """
    try:
        # Try to open json file in reding mode
        with open("CSO.json", "r") as f:
            # Import json data to a variable
            data = load(f)
            return data

    # Handling errors
    except FileNotFoundError:
        raise FileNotFoundError("Error: File 'CSO.json' not found.")
    except (JSONDecodeError, OSError) as e:
        raise OSError(f"Error processing JSON file: {e}")


# ============================================ #
# //           Data serialization           // #
# ============================================ #


class SERIALIZATION:
    def __init__(self, data):
        # Create empties variables
        self.label_number = []
        self.headline_label = {}
        self.serialized_name = []
        self.serialized_data = []
        self.final_data = []

        # Import input to a variable
        self.data = data

    # ============================================ #
    # //           Headline function            // #
    # ============================================ #
    def headline(self):
        """
        Creates a headline for the data table, including town names and column labels.
        """

        # Define first two columns (static)
        static_columns = ["town_name", "town_code"]

        # Get dynamic column labels from data
        dynamic_labels = [self.data["dataset"]["dimension"]["STATISTIC"]["category"]["label"][f"CD176C{i + 1}"] for i in
                          range(8)]

        # Combine static and dynamic columns
        self.headline_label = {column: [] for column in static_columns + dynamic_labels}

    # ============================================ #
    # //     Town name serialization function   // #
    # ============================================ #
    def name_serialization(self, letter):
        """
        Gets 'label' as dictionary.

        Gets towns that start with 'G'.
        or
        Gets towns that belongs Counties that start with 'K'.
        or
        Gets towns that start with 'N'.

        Sorted it into two different variables.
        """
        try:
            # Clean lists
            self.serialized_name = []
            self.label_number = []
            # Get the list of labels
            labels = self.data["dataset"]["dimension"]["C03198V03862"]["category"]["label"]
            if letter == "G":
                # Filter towns starting with 'G' using list comprehension
                self.serialized_name = [[key, value] for key, value in labels.items() if value[4] == "G"]
                self.label_number = [key for key, _ in self.serialized_name]
            elif letter == "K":
                # Filter towns that belongs Counties that start with 'k' using list comprehension
                self.serialized_name = [[key, value] for key, value in labels.items() if "Co. K" in value]
                self.label_number = [key for key, _ in self.serialized_name]
            elif letter == "N":
                # Filter towns starting with 'N' using list comprehension
                self.serialized_name = [[key, value] for key, value in labels.items() if value[4] == "N"]
                self.label_number = [key for key, _ in self.serialized_name]

        except (KeyError, TypeError, ValueError) as e:
            raise f"Error during name serialization: {e}"

    # ============================================ #
    # // Town statistics serialization function // #
    # ============================================ #
    def data_serialization(self):
        """
        Using index from 'label_number', gets all index that belongs to towns in 'serialized_name'.

        Gets all statistic that belongs to 'serialized_name' towns into 'serialized_data'.

        Uses 'for' loop to handle with 'append' function and control the output as an array.
        """
        try:
            # Clean serialized_data
            self.serialized_data = []
            # Get all indices from each data town
            indices = [[((int(i) - 1) * 8) + j for j in range(8)] for i in self.label_number]

            # Append elements to serialized_data using a loop for better control
            for i in range(len(indices)):
                inner_list = []
                for j in range(len(indices[i])):
                    inner_list.append(self.data["dataset"]["value"][indices[i][j]])
                self.serialized_data.append(inner_list)

        except (KeyError, TypeError, ValueError) as e:
            raise f"Error during data serialization: {e}"

    # ============================================ #
    # //          Concatenation function        // #
    # ============================================ #
    def concatenation(self):
        """
        Concatenates 'serialized_name' and 'serialized_data'.

        Creates a list of dictionaries that contains the column name as key and the index, name and statistic as value.
        """
        try:
            # Clean final_data
            self.final_data = []
            # Loop to concatenate town index, town name and all new data
            self.serialized_data = [name + data for name, data in zip(self.serialized_name, self.serialized_data)]

            # Loop to create a list of dicts with key equal to column name and value equal to column value
            for row in self.serialized_data:
                _dict = {}  # Create a new dictionary for each row inside the loop
                for j, key in enumerate(self.headline_label.keys()):
                    _dict[key] = row[j]  # Access data by index from row and key from headline_label

                self.final_data.append(_dict)
        except (KeyError, TypeError, ValueError) as e:
            raise f"Error during concatenation: {e}"

    # ============================================ #
    # //           Write CSV function           // #
    # ============================================ #
    def write_csv(self, filename):
        """
        Writes the 'final_data' to a CSV.
        """
        # Open the CSV file in write mode
        try:
            with open(filename, "w", newline="") as csvfile:
                # Create a csv writer object
                csv_writer = DictWriter(csvfile, fieldnames=self.headline_label.keys())
                # Write the header row (automatically inferred from fieldnames)
                csv_writer.writeheader()

                # Write each row in final_data to csv
                for row in self.final_data:
                    csv_writer.writerow(row)
            if filename == "letterG.csv":
                print(f"The serialization of cities starting with 'G' has been done, "
                      f"the {filename} has been created successfully.")
            elif filename == "letterK.csv":
                print(f"Serialization of towns that belongs to Counties that "
                      f"start with 'K' is done, {filename} was created successfully.")
        except (IOError, OSError) as e:  # Catch potential file I/O errors
            raise f"Error writing CSV file: {e}"

    # ============================================ #
    # //       Write on terminal function       // #
    # ============================================ #
    """
    Writes the 'final_data' to terminal.
    """
    def print_terminal(self):
        df = DataFrame(self.final_data)
        print("\n" + df.to_string())

# -------------------------------------------- #
# //               main function            // #
# -------------------------------------------- #


def main():
    download_file()

    s = SERIALIZATION(import_data())
    s.headline()
    # // G // #
    s.name_serialization("G")
    s.data_serialization()
    s.concatenation()
    s.write_csv("letterG.csv")
    # // K // #
    s.name_serialization("K")
    s.data_serialization()
    s.concatenation()
    s.write_csv("letterK.csv")
    # // N // #
    s.name_serialization("N")
    s.data_serialization()
    s.concatenation()
    s.print_terminal()


if __name__ == '__main__':
    main()
