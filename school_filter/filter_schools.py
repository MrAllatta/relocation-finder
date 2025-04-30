"""
Module for loading and filtering NYC school datasets based on quality and demographics.
"""
import pandas as pd
import requests

# --- CONFIGURATION ---
SCHOOL_QUALITY_BASE_URL = "https://data.cityofnewyork.us/resource/dnpx-dfnc.json"
SCHOOL_DEMOGRAPHICS_BASE_URL = "https://data.cityofnewyork.us/resource/vmmu-wj3w.json"
APP_TOKEN = None  # Optional: Add your Socrata app token if you have one

# --- GENERIC QUERY BUILDER ---
def build_soql_query(select_fields=None, where_clause=None, limit=5000, offset=0, order_by=None):
    params = {}
    if select_fields:
        params['$select'] = ','.join(select_fields)
    if where_clause:
        params['$where'] = where_clause
    if limit:
        params['$limit'] = limit
    if offset:
        params['$offset'] = offset
    if order_by:
        params['$order'] = order_by
    return params

# --- DATA FETCHER ---
def fetch_data(base_url, params):
    headers = {}
    if APP_TOKEN:
        headers['X-App-Token'] = APP_TOKEN

    response = requests.get(base_url, params=params, headers=headers)
    response.raise_for_status()
    return pd.DataFrame(response.json())

# --- JOINER ---
def join_quality_and_demographics(quality_df, demographics_df):
    # Normalize DBN fields if necessary
    return pd.merge(quality_df, demographics_df, left_on='dbn', right_on='dbn', how='left')

# --- MAIN PIPELINE ---
def main():
    # 1. Query School Quality Data
    quality_select_fields = [
        "dbn", "school_name", "metric_display_name", "metric_value", 
        "metric_score", "school_year", "report_year", "school_type"
    ]
    quality_where = "report_year=2023"  # Adjust to latest year available
    quality_params = build_soql_query(
        select_fields=quality_select_fields,
        where_clause=quality_where,
        limit=5000
    )
    quality_df = fetch_data(SCHOOL_QUALITY_BASE_URL, quality_params)
    print(f"Fetched {len(quality_df)} school quality records.")

    # 2. Query School Demographics Data
    demographics_select_fields = [
        "dbn", "school_name", "borough", "grade_span_min", "grade_span_max", 
        "enrollment", "ell_percent", "sped_percent", "asian_percent", 
        "black_percent", "hispanic_percent", "white_percent", "poverty_percent"
    ]
    demographics_where = "report_year=2023"
    demographics_params = build_soql_query(
        select_fields=demographics_select_fields,
        where_clause=demographics_where,
        limit=5000
    )
    demographics_df = fetch_data(SCHOOL_DEMOGRAPHICS_BASE_URL, demographics_params)
    print(f"Fetched {len(demographics_df)} school demographic records.")

    # 3. Join
    combined_df = join_quality_and_demographics(quality_df, demographics_df)
    print(f"Combined dataset has {combined_df.shape[0]} rows and {combined_df.shape[1]} columns.")

    # 4. Save for exploration
    combined_df.to_csv("combined_school_data.csv", index=False)
    print("Saved combined_school_data.csv.")

    return combined_df

if __name__ == "__main__":
    final_df = main()


def load_school_data(csv_path: str) -> pd.DataFrame:
    """
    Load school quality and demographic data from a CSV file.

    Args:
        csv_path: Path to the school data CSV.

    Returns:
        Pandas DataFrame containing school data.
    """
    # TODO: implement CSV loading logic
    pass

def filter_schools(
    df: pd.DataFrame,
    min_quality: float,
    demographic_criteria: dict
) -> pd.DataFrame:
    """
    Filter schools based on quality score and demographic criteria.

    Args:
        df: DataFrame of schools.
        min_quality: Minimum quality score to filter schools.
        demographic_criteria: Dictionary of demographic thresholds.

    Returns:
        DataFrame of filtered schools.
    """
    # TODO: implement filtering logic based on criteria
    pass
