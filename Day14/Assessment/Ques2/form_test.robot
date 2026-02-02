"""
Write a Robot Framework test case that:
1. Opens a browser using SeleniumLibrary
2. Interacts with:
Text box
Radio button
Check box
Drop-down
3. Uses Built-in keywords:
Run Keyword If Should Be Equal
Sleep
4. Validates form submission
5. Closes the browser and generates execution reports
"""

*** Settings ***
Library           SeleniumLibrary
Suite Setup       Open Browser To Form
Suite Teardown    Close Browser

*** Variables ***
${URL}            https://demoqa.com/automation-practice-form
${BROWSER}        chrome

*** Test Cases ***
Fill And Submit Form
    [Documentation]    Fill form elements, validate submission, and close browser

    # Text boxes
    Input Text    id=firstName    John
    Input Text    id=lastName     Doe
    Input Text    id=userEmail   john.doe@test.com
    Input Text    id=userNumber  9876543210

    # Scroll to Gender
    Execute Javascript    document.getElementById('gender-radio-1').scrollIntoView(true)

    # Radio button (JS click)
    Execute Javascript    document.querySelector("label[for='gender-radio-1']").click()

    # Checkbox
    Execute Javascript    document.querySelector("label[for='hobbies-checkbox-1']").click()

    # Drop-down (State)
    Execute Javascript    document.getElementById('state').scrollIntoView(true)
    Click Element        id=state
    Click Element        xpath=//div[text()='NCR']

    Sleep    1s

    # Built-in keyword
    Run Keyword If    '${BROWSER}' == 'chrome'    Log    Chrome browser selected

    # Submit form (JS click)
    Execute Javascript    document.getElementById('submit').click()

    Sleep    2s

    # Validation (SUCCESS MODAL)
    Wait Until Page Contains Element    id=example-modal-sizes-title-lg
    ${text}=    Get Text    id=example-modal-sizes-title-lg
    Should Be Equal    ${text}    Thanks for submitting the form


*** Keywords ***
Open Browser To Form
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    id=firstName
