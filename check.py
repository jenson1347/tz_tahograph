from router.router import route


def main():

    while True:

        text = input("\nВведите сообщение: ")

        result = route(text)

        print("\nRESULT:")
        print(result)


main()