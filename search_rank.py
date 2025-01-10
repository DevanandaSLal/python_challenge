import requests
from bs4 import BeautifulSoup
import json


# fetch from the website
def fetch_data(keyword, site_url):
    search_url = f"{site_url}/ps/?q={keyword.replace(' ', '%20')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)  #sending req to the website

    if response.status_code != 200:  # if request failing
        raise Exception(f"Failed to load page. status code: {response.status_code}")

    return response.text


#get brand name
def extract_brands(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')  #parsing html


    brand_elements = soup.find_all('span',
                                   class_='Label-sc-15v1nk5-0 BrandName___StyledLabel2-sc-hssfrl-1 gJxZPQ keQNWn')


    brands = [brand.get_text(strip=True) for brand in brand_elements]

    return brands


# get the ranking
def find_brand_rankings(products, target_brands):
    rankings = {}

    for brand in target_brands:
        for position, product in enumerate(products[:100], start=1):

            if brand.lower() in product.lower() or ("l'oreal" in product.lower() and "paris" in product.lower()):
                rankings[brand] = position
                break
        else:
            rankings[brand] = None  # If not found, set as None

    return rankings



def main():
    site_url = "https://www.bigbasket.com"
    keywords = ["Hair fall shampoo", "Conditioner", "Shampoo"]  # keywords
    brands_to_check = ["Loreal", "Dove", "Tresemme"]  # brands

    results = []  #storing the final res

    for keyword in keywords:
        try:

            page_data = fetch_data(keyword, site_url)
            product_list = extract_brands(page_data)

            print(f"Products for '{keyword}': {product_list}")


            brand_rankings = find_brand_rankings(product_list, brands_to_check)


            results.append({"keyword": keyword, "results": brand_rankings})

        except Exception as error:
            print(f"Error searching for '{keyword}': {error}")
            results.append({"keyword": keyword, "results": {brand: None for brand in brands_to_check}})


    with open("output.json", "w") as file:
        json.dump(results, file, indent=4)

    print("Results saved to output.json")



if __name__ == "__main__":
    main()
