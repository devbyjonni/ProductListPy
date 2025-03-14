import unittest  # Make sure unittest is imported

from main import ProductList  # Import the ProductList class from main.py


class TestProductList(unittest.TestCase):

    def setUp(self):
        """This method runs before each test case"""
        self.product_list = ProductList()  # Create an instance of ProductList

    def test_add_product(self):
        """Test if a product is added correctly"""
        self.product_list.add_product("ABCD-200")
        self.assertIn("ABCD-200", self.product_list.products)

    def test_is_valid_product_valid(self):
        """Test if valid product is recognized as valid"""
        result = self.product_list.is_valid_product("ABCD-250")
        self.assertTrue(result)

    def test_is_valid_product_invalid(self):
        """Test if an invalid product format is recognized as invalid"""
        result = self.product_list.is_valid_product("ABCD-150")
        self.assertFalse(result)

    def test_display_sorted_products(self):
        """Test if products are sorted correctly"""
        self.product_list.add_product("ABCD-250")
        self.product_list.add_product("XYZ-300")
        self.product_list.add_product("LMNO-400")

        sorted_products = self.product_list.display_sorted_products()
        self.assertEqual(sorted_products, ["ABCD-250", "LMNO-400", "XYZ-300"])


if __name__ == "__main__":
    unittest.main()

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
