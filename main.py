import re


class ProductList:

    def __init__(self):
        self.products = []
        # This regex pattern is used to validate the product input
        # The pattern is as follows:
        # ^               -> Anchors the match at the start of the string
        # [A-Za-z]{4}     -> Matches exactly 4 characters that are either uppercase (A-Z) or lowercase (a-z)
        # -               -> Matches the hyphen character literally
        # [2-5]           -> Matches the first digit, which must be between 2 and 5 (inclusive)
        # [0-9]{2}        -> Matches the next two digits, each of which can be any digit from 0 to 9
        # $               -> Anchors the match at the end of the string
        # This means the product must be in the format: 'NAME-XXX', where 'NAME' is 4 letters, and 'XXX' is a number between 200 and 500.
        self.product_regex = re.compile(r"^[A-Za-z]{4}-[2-5][0-9]{2}$")

    def run(self):
        self.print_message(
            "Skriv in produkter. Avsluta med att skriva 'exit'\n", "cyan"
        )

        while True:
            input_product = self.get_user_input(
                "Ange produkt (FORMAT: NAMN-XXX, t.ex. ABCD-400): "
            )

            if self.is_exit_command(input_product):
                break

            if not input_product:
                self.print_error("Fel: Produktnamnet får inte vara tomt.")
                continue

            if self.is_valid_product(input_product):
                self.add_product(input_product)

        self.display_sorted_products()

    def get_user_input(self, prompt):
        return input(prompt).strip()

    def is_valid_product(self, input_product):
        if not self.product_regex.match(input_product):
            self.print_error(
                "Fel: Ogiltigt format. Exempel på korrekt format: ABCD-250."
            )
            return False
        return True

    def is_exit_command(self, input_product):
        return input_product.lower() == "exit"

    def add_product(self, product):
        self.products.append(product.upper())

    def display_sorted_products(self):
        self.products.sort()
        self.print_message("\nDu angav följande produkter (sorterade):", "green")
        for product in self.products:
            self.print_message(f"* {product}", "green")

    def print_message(self, message, color):
        colors = {
            "cyan": "\033[96m",  # Light cyan color
            "green": "\033[92m",  # Light green color
            "red": "\033[91m",  # Light red color
            "reset": "\033[0m",  # Resets the color to the default terminal color
        }

        # Print the message with the color applied
        # If the provided 'color' is found in the dictionary, use the corresponding ANSI code
        # Otherwise, default to the reset code (no color)
        print(f"{colors.get(color, colors['reset'])}{message}{colors['reset']}")

    def print_error(self, message):
        self.print_message(message, "red")


# Main execution
if __name__ == "__main__":
    product_list = ProductList()
    product_list.run()


# ---------------------------------
# Test Cases for Product Validation
# ---------------------------------
# ✅ Valid cases:
#   ABCD-200   -> ✅ Valid (4 letters, 3 digits between 200-500)
#   XYZW-450   -> ✅ Valid (4 letters, 3 digits between 200-500)
# ❌ Invalid cases:
#   ABCDE-200  -> ❌ Too many letters
#   XYZ-199    -> ❌ Number below 200
#   A1B2-300   -> ❌ Name contains numbers
#   ABC-4000   -> ❌ Number too long
#   --         -> ❌ Invalid format
