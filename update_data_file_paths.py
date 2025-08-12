import pandas as pd

# Read the CSV file
csv_filename = "train_split_01"
df = pd.read_csv(f"data/isic19/{csv_filename}.csv")

# Update the image column - remove /isic2019/ prefix and prepend the new base path
df["image"] = df["image"].str.replace("/isic2019/", "/scratch/talks/data/", regex=False)

# Update the old_image column - prepend the new base path
# df["old_image"] = "/scratch/talks/data/" + df["old_image"]

# Save the updated CSV file
df.to_csv(f"data/isic19/{csv_filename}.csv", index=False)

print(f"Successfully updated paths in {csv_filename}.csv")
print("First few rows after update:")
print(df[["image", "old_image"]].head())
