import allure
from pytest_bdd import scenarios, given, when, then


scenarios("../features/addHighestPricedItem.feature")


@given("I am logged in as a standard user")
def login_as_standarduser(login_page, user_cred):
    with allure.step("Logon as standard user"):
     login_page.load()
     login_page.loginAsUser(user_cred["username"], user_cred["password"])


@given("I am on the products page")
def inventoryIsDisplayed(product_price_page):
     with allure.step("launch the product page "):
      assert product_price_page.is_displayed(); "Product page failed to load"


@when("I search for the highest priced item")
def search_for_higest_priced_item(product_price_page):
     with allure.step("Search for the highest priced item"):
      product_price_page.get_highestPrice()
  
@when("I add it to the cart")
def add_to_cart(product_price_page):
       with allure.step("Add the item to cart"):
        product_price_page.addPricetoCart()

@then("the item should be in my cart")
def item_in_cart(product_price_page):
      with allure.step("cart contains highest priced item"):
       product_price_page.verifyItemInCart()






