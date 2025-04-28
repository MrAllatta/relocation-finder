"""
CLI script to scrape and filter rental listings from StreetEasy.
"""
import argparse

from rental_scraper.scrape_streeteasy import fetch_listings, parse_listings, filter_listings
from utils.helpers import setup_logging

def main():
    """
    Entry point for the rental scraper CLI.
    """
    parser = argparse.ArgumentParser(
        description='Scrape and filter rental listings from StreetEasy.'
    )
    parser.add_argument(
        '--output', required=True, help='Path to output rentals CSV.'
    )
    parser.add_argument(
        '--bedrooms', type=int, default=3, help='Minimum number of bedrooms.'
    )
    parser.add_argument(
        '--bathrooms', type=int, default=2, help='Minimum number of bathrooms.'
    )
    parser.add_argument(
        '--max-price', type=float, default=5000.0, help='Maximum rental price.'
    )
    parser.add_argument(
        '--laundry', action='store_true', help='Require in-unit laundry.'
    )
    args = parser.parse_args()
    setup_logging()

    # TODO: define StreetEasy URL template or input source
    url = ''  # Placeholder for listings URL
    # Fetch listings page
    html = fetch_listings(url)
    # Parse into DataFrame
    df = parse_listings(html)
    # Filter listings based on criteria
    filtered = filter_listings(
        df, args.bedrooms, args.bathrooms, args.max_price, args.laundry
    )
    # Save to CSV
    # TODO: implement save to CSV
    # filtered.to_csv(args.output, index=False)
    pass

if __name__ == '__main__':
    main()