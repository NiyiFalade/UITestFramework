Feature: Add highest priced item to cart

  As a standard user
  I want to log in and navigate to the products page
  So that I can add the most expensive item to my cart

  Background:
    Given I am logged in as a standard user

  Scenario: Add highest priced item to cart
    Given I am on the products page
    When I search for the highest priced item
    And I add it to the cart
    Then the item should be in my cart