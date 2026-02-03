import json
import pandas as pd
with open ("data.json") as f:
    users = json.load(f)
columns = ["User Id", "User Name", "Book Title", "Book Price", "Book Id"]
final_columns_data = []

for user in users:
    for book in user.get("books", []):
        if user.get("user_id","") and book.get("book_id",""):
             final_columns_data.append([
                user.get("user_id","-"),
                user.get("user_name","-"),
                book.get("book_title","-"),
                book.get("book_price","-"),
                book.get("book_id","-")
            ])
       

df = pd.DataFrame(final_columns_data, columns = columns)
df.to_csv("output.csv", index=False)