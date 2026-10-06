# Example project data dictionary.
data_dictionary = {
    "customer_id": "Unique customer identifier",
    "order_id": "Unique transaction identifier",
    "order_date": "Transaction date",
    "product_category": "Product category",
    "revenue": "Order revenue",
    "quantity": "Units purchased",
    "customer_segment": "Business-defined customer segment",
}
for column, definition in data_dictionary.items():
    print(f"{column:20} -> {definition}")
