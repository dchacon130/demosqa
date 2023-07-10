Feature: Radio Button

    Scenario: Select Yes Radio Button
        Given I am on the Radio Button page "https://demoqa.com/radio-button"
        When I select the Yes radio button
        Then the Yes radio button is selected in the text

    Scenario: Select Impressive Radio Button
        Given I am on the Radio Button page "https://demoqa.com/radio-button"
        When I select the Impressive radio button
        Then the Impressive radio button is selected in the text