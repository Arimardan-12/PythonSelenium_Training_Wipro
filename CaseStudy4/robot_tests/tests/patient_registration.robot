*** Settings ***
Resource    ../resources/keywords.robot
Suite Setup    Open Registration Page
Suite Teardown    Close Application Browser

*** Test Cases ***
Register Patient
    Fill Patient Form
    Submit Form
    Page Should Contain    Registered Patients
