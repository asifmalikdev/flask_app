import json
import pandas as pd
with open("data.json") as w:
    data = json.load(w)
#print(data)
columns =  ["User Id", "User Name", "Book Id", "Book Title", "Book Price"]
final_data = []
for user in data:
    for book in user.get("books"):
        final_data.append([
            user.get("user_id","-"),
            user.get("user_name","-"),
            book.get("book_id","NILL"),
            book.get("book_title","Nill"),
            book.get("book_price","-")
        ])

df = pd.DataFrame(final_data, columns = columns)
df.to_csv("final_data.csv")