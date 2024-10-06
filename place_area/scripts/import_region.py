import pandas as pd
from django.contrib.auth.models import User
from place_area.models import Region

def run():
    # Read CSV file into a DataFrame
    print("Importing File")
    csv_file_path = 'regions.txt'
    df = pd.read_csv(csv_file_path)

    # Iterate through the DataFrame and create model instances
    for index, row in df.iterrows():
        print(row, index)
        # Create or get the Category instance
        i = Region.objects.get_or_create(
            id=row['id'],
            region_name=row['region_name'],
            slug=row['slug']
        )



print("CSV data has been loaded into the Django database.")