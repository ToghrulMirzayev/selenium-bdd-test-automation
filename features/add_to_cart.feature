Feature: Add to cart functionality

Scenario: User adds product to cart
    Given the user is on the website
    And the user is logged in
    And the user is on the inventory page
    When the user adds a product to the cart
    Then the user should see the product in the cart