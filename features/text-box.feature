Feature: TextBox

    Scenario: Successfully fill out a text form
        Given I am on the "https://demoqa.com/text-box" page
        When I enter "John Smith" in the "Full Name" field
        And I enter "johnSmith@example.com" in the "Email" field
        And I enter "Calle 71 bis No. 91-67" in the "Current Address" field
        And I enter "Carrera 120a 77b 82" in the "Permanent Address" field
        When I click the "Submit" button
        Then I see the information at the bottom of the form

    Scenario: Validate email format
        Given I am on the "https://demoqa.com/text-box" page
        When I enter "John Smith" in the "Full Name" field
        And I enter an invalid email format (e.g., "john@example") in the "Email" field
        And I enter "Calle 71 bis No. 91-67" in the "Current Address" field
        And I enter "Carrera 120a 77b 82" in the "Permanent Address" field
        When I click the "Submit" button
        Then I see a red color in the "Email" field
