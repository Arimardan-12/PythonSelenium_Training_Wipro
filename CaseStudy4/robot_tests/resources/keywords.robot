*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Registration Page
    Open Browser    http://127.0.0.1:5000    chrome
    Maximize Browser Window

Fill Patient Form
    Input Text    id=name       Robot User
    Input Text    id=age        30
    Click Element    xpath=//input[@name="gender" and @value="Male"]
    Input Text    id=contact    9999999999
    Input Text    id=disease    Fever
    Select From List By Value    id=doctor    Dr. Smith

Submit Form
    Click Button    xpath=//input[@type="submit"]

Close Application Browser
    Close Browser
