"""
CLI script to filter schools by quality and demographics.
"""
import argparse
import json

from school_filter.filter_schools import load_school_data, filter_schools
from utils.helpers import setup_logging

def main():
    """
    Entry point for the school filter CLI.
    """
    parser = argparse.ArgumentParser(
        description='Filter NYC schools by quality and demographics.'
    )
    parser.add_argument(
        '--data-path', required=True, help='Path to school data CSV file.'
    )
    parser.add_argument(
        '--min-quality', type=float, default=0.0, help='Minimum school quality score.'
    )
    parser.add_argument(
        '--demographics', type=str, default='{}',
        help='Demographic criteria as JSON string.'
    )
    parser.add_argument(
        '--output', required=True, help='Path to output filtered schools CSV.'
    )
    args = parser.parse_args()
    setup_logging()

    # Load school data
    df = load_school_data(args.data_path)
    # Parse demographic criteria
    demo_criteria = json.loads(args.demographics)
    # Filter schools
    filtered = filter_schools(df, args.min_quality, demo_criteria)
    # Save results
    # TODO: implement save to CSV
    # filtered.to_csv(args.output, index=False)
    pass

if __name__ == '__main__':
    main()