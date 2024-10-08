import pandas as pd


class JsonToCsvConverter:
    def __init__(self, json_file_path: str, csv_file_path: str):
        self.json_file_path = json_file_path
        self.csv_file_path = csv_file_path

    def convert(self) -> None:
        """
        Reads a JSON file from the specified path, converts it to a DataFrame,
        and exports it to a CSV file at the specified path.
        """
        json_dataframe: pd.DataFrame = pd.read_json(self.json_file_path)

        json_dataframe.to_csv(self.csv_file_path, index=False)


if __name__ == "__main__":
    json_file_path = "/home/jessica/desafio_tecnico/docs/base.json"
    csv_file_path = "/home/jessica/desafio_tecnico/docs/base.csv"
    converter = JsonToCsvConverter(json_file_path, csv_file_path)
    converter.convert()


