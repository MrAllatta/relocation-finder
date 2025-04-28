"""
CLI script to geocode rental addresses using Nominatim.
"""
import argparse

import pandas as pd
from geocoder.geocode_addresses import bulk_geocode
from utils.helpers import setup_logging

def main():
    """
    Entry point for the geocoding CLI.
    """
    parser = argparse.ArgumentParser(
        description='Geocode rental addresses using Nominatim.'
    )
    parser.add_argument(
        '--input', required=True, help='Path to input rentals CSV with address column.'
    )
    parser.add_argument(
        '--output', required=True, help='Path to output CSV with geocoded coordinates.'
    )
    args = parser.parse_args()
    setup_logging()

    # Load rentals with address column
    df = pd.read_csv(args.input)
    # Perform bulk geocoding
    geocoded_df = bulk_geocode(df['address'].tolist())
    # Merge geocoded coordinates back to original
    # TODO: implement merging logic
    # result = df.merge(geocoded_df, on='address')
    # Save to CSV
    # result.to_csv(args.output, index=False)
    pass

if __name__ == '__main__':
    main()