import pandas as pd
import json
import os
CSV_FILE = "products.csv"
JSON_FILE = "products.json"
def init_csv():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["Product ID", "Product Name", "Category", "Price", "Stock"])
        df.to_csv(CSV_FILE, index=False)
def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock: "))
    df = pd.read_csv(CSV_FILE)
    if pid in df["Product ID"].astype(str).values:
        print(f"Error: Product ID {pid} already exists!")
        return
    new_data = pd.DataFrame(
        [{"Product ID": pid, "Product Name": name, "Category": category, "Price": price, "Stock": stock}])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    print("Product added successfully to products.csv!")

def display_products():
    try:
        df = pd.read_csv(CSV_FILE)
        if df.empty:
            print("No products found!")
        else:
            print("\n--- Product List ---")
            print(df.to_string(index=False))
    except FileNotFoundError:
        print("products.csv not found!")

def update_product():
    pid = input("Enter Product ID to update: ")
    try:
        df = pd.read_csv(CSV_FILE)
        if pid not in df["Product ID"].astype(str).values:
            print(f"Error: Product ID {pid} not found!")
            return
        new_price = float(input("Enter new Price: "))
        new_stock = int(input("Enter new Stock: "))
        df.loc[df["Product ID"].astype(str) == pid, "Price"] = new_price
        df.loc[df["Product ID"].astype(str) == pid, "Stock"] = new_stock
        df.to_csv(CSV_FILE, index=False)
        print("Product updated successfully!")
    except FileNotFoundError:
        print("products.csv not found!")
def delete_product():
    pid = input("Enter Product ID to delete: ")
    try:
        df = pd.read_csv(CSV_FILE)
        if pid not in df["Product ID"].astype(str).values:
            print(f"Error: Product ID {pid} not found!")
            return

        df = df[df["Product ID"].astype(str) != pid]
        df.to_csv(CSV_FILE, index=False)
        print("Product deleted successfully!")
    except FileNotFoundError:
        print("products.csv not found!")

def export_to_json():
    try:
        df = pd.read_csv(CSV_FILE)
        df.to_json(JSON_FILE, orient="records", indent=4)
        print(f"Exported to {JSON_FILE} successfully!")
    except FileNotFoundError:
        print("products.csv not found! Cannot export.")

def display_json():
    try:
        with open(JSON_FILE, "r") as f:
            data = json.load(f)
            print("\n--- Products JSON ---")
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("products.json not found! Please export first (Option 5).")
init_csv()
while True:
    print("\n--- PRODUCT INVENTORY MANAGEMENT SYSTEM ---")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Export to JSON")
    print("6. Display JSON")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        add_product()
    elif choice == '2':
        display_products()
    elif choice == '3':
        update_product()
    elif choice == '4':
        delete_product()
    elif choice == '5':
        export_to_json()
    elif choice == '6':
        display_json()
    elif choice == '7':
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice! Please enter 1-7.")