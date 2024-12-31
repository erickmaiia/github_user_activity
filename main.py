import shlex
from cli import CLI


def main():
    cli = CLI()

    while True:
        # Lê o comando completo do usuário
        user_input = input(">>> ").strip()
        if user_input.lower() == "exit":
            print("Exiting. Goodbye!")
            exit()

        # Divide o comando em partes, mantendo argumentos entre aspas intactos

        try:
            args = shlex.split(user_input)
        except ValueError:
            print("Invalid input format. Please check your quotes and try again.")
            continue

        if not args:
            print("Invalid command. Please try again.")
            continue

        # Processa o comando
        user = args[0].lower()

        try:
            if user:
                cli.list_activity(user)
            else:
                print("Invalid command or arguments. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
