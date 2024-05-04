import pandas as pd
import requests
import io
import os

data = {
    "ACB": {
        "url": 'https://docs.google.com/spreadsheets/d/1f0yyd3792jumsv5IwTixOyWy7K44f2GPvRk0JHTmygQ/edit#gid=0'
    }
}

class StockData:
    def __init__(self, name):
        global data
        self.name = name
        self.url = data[name]["url"]
        self.data = None

    def download(self):
        # Convert the Google Sheet view URL to an XLSX export URL
        xlsx_export_url = self.url.replace('/edit#gid=', '/export?format=xlsx&gid=')
        
        # Fetch the Excel data using requests
        response = requests.get(xlsx_export_url)
        assert response.status_code == 200, 'Failed to download the data'
        
        # Load the data into a pandas DataFrame
        self.data = pd.read_excel(io.BytesIO(response.content))
        
        # Save the data after download
        self.save_data()

    def save_data(self):
        # Ensure the 'data' directory exists
        os.makedirs('data', exist_ok=True)
        
        # Save the DataFrame to an Excel file named "{self.name}.xlsx" in the "data" directory
        file_path = f'data/{self.name}.xlsx'
        self.data.to_excel(file_path, index=False)
        print(f'Data saved to {file_path}')

    def get_data(self):
        return self.data

if __name__ == '__main__':
    # Create a StockData object
    name = "ACB"
    stock_data = StockData(name)
    # Download the data
    stock_data.download()
    # Access the downloaded data
    data_frame = stock_data.get_data()
    print(data_frame)