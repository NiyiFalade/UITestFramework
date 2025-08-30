from playwright.sync_api import expect


class ProductPrice:
    def __init__(self,page):
        self.page = page
        self.allPrice="//*[@data-test= \"inventory-item-price\"]"
        self.cartLink = "//*[@data-test=\"shopping-cart-link\"]"

    def is_displayed(self):
        return "inventory.html" in self.page.url.lower()   

    def get_highestPrice(self):
      locator = self.page.locator(self.allPrice)
      locator.first.wait_for(state="visible")
      prices_text = locator.all_inner_texts()
      prices = [float(price.replace("$", "")) for price in prices_text if price.strip()]
    
      if not prices:
        raise ValueError("No prices found on the page.")
    
       # Return the highest price
      return max(prices)


    def addPricetoCart(self):
        highestPriceXpath = f"//*[@class='inventory_item_price' and contains(string(.), '${self.get_highestPrice()}')]//following-sibling::button"
        button = self.page.locator(highestPriceXpath)
        button.click()
        self.page.screenshot(path="reports/screenshots/addtoCart.png")


    def verifyItemInCart(self): 
        button = self.page.locator(self.cartLink)
        button.click()
        locator = self.page.locator(
           f"//*[@data-test='inventory-item-price' and contains(string(.),'${self.get_highestPrice()}')]"
        )
        expect(locator).to_be_visible()
        self.page.screenshot(path="reports/screenshots/viewCart.png")


        

                  