# Created by KARTIK at 18-01-2022
Feature: This feature describes the journey of wish list and lowest price products
  # Enter feature description here

  Scenario: View wish listed products
    Given website is open
    When 4 products are added to wish list
    And wish list page is opened
    Then 4 items are displayed
    # Enter steps here