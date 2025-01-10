import json


def count_of_products(file_path):

    with open(file_path, 'r') as file:
        data = json.load(file)


    if 'productList' not in data:
        print(f"Key 'productList' not found in the JSON data")
        return {}


    product_count = {}


    for product in data['productList']:
        merchant = product['merchant']
        if merchant in product_count:
            product_count[merchant] += 1
        else:
            product_count[merchant] = 1

    return product_count


def main():
    file_path = 'search_result.json'
    product_count = count_of_products(file_path)

    if product_count:

        print(json.dumps(product_count, indent=4))
    else:
        print("No products found ")


if __name__ == "__main__":
    main()
