class Client:
    name="veerraju"
    phone="9999999"
    email="veer@gmail.com"


def main():
    firstClient=Client()
    print(firstClient.name)
    print(firstClient.phone)
    print(firstClient.email)
    firstClient.name="raju"
    firstClient.phone="8888"
    print(firstClient.name)
    print(firstClient.phone)
    print(firstClient.email)


main()
