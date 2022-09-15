# Simple https status code checker exercise

# use urllib.request to get data from URL
# write function to receive URL
# return a response


import urllib.request as urllib


def main(url):
    print("Checking connectivity..\n")

    response = urllib.urlopen(url)
    print(f"Connected to", url, "successfully!\n")
    print(f"Response code:", response.getcode())


print("\nThis program is a website HTTP Status Code checker. \nFormat example: https://www.google.com\n")
url_input = input("Input URL of the site you want to check: ")

main(url_input)