import dask.dataframe as dd

def load_data(file_path: str) -> dd.DataFrame:
    """
    Load large datasets using Dask for efficient processing.
    """
    df = dd.read_csv(file_path, dtype={'weight': 'object'})

    def process_weight(weight):
        try:
            if isinstance(weight, str):
                # Handle comma-separated values (e.g., '124, 131')
                if ',' in weight:
                    # Take the first value or compute an average
                    numbers = [float(num.strip()) for num in weight.split(',')]
                    return sum(numbers) / len(numbers)
                # Handle range values (e.g., '58-60')
                elif '-' in weight:
                    low, high = weight.split('-')
                    return (float(low) + float(high)) / 2
                else:
                    # Try to convert the value to float
                    return float(weight)
            return float(weight)
        except ValueError:
            # Handle the case where conversion fails, return NaN
            return float('nan')

    df['weight'] = df['weight'].apply(process_weight, meta=('weight', 'float64'))
    return df
