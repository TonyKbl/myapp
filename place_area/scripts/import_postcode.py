import pandas as pd
from django.contrib.auth.models import User
from place_area.models import PostCode

def run():
    # Read CSV file into a DataFrame
    print("Importing File")
    csv_file_path = 'ukpostcodes.csv'
    df = pd.read_csv(csv_file_path)

    # Iterate through the DataFrame and create model instances
    for index, row in df.iterrows():
        # print(row, index)
        # Create or get the Category instance
        i = PostCode.objects.get_or_create(
            id=row['id'],
            postcode=row['postcode'],
            lat=row['latitude'],
            lon=row['longitude']
        )



print("CSV data has been loaded into the Django database.")