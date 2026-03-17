import pandas as pd

def save_csv(data):

    try:

        if not data:
            print("No data to save")
            return

        df = pd.DataFrame(data)

        df.drop_duplicates(inplace=True)

        df.to_csv(
            "data/output.csv",
            index=False
        )

        print("Data saved successfully")

    except Exception as e:
        print("Saving CSV failed:", e)
        raise