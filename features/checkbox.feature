Feature: CheckBoxes

    Scenario: Selecting and deselecting checkboxes
        Given the user opens the webpage "https://demoqa.com/checkbox"
        When the user selects all checkboxes
        Then all checkboxes should be selected