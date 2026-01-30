*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    OrangeHRM Login With Excel
Suite Setup    Open OrangeHRM
Suite Teardown    Close OrangeHRM

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   chrome

*** Keywords ***
Open OrangeHRM
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

OrangeHRM Login With Excel
    [Arguments]    ${username}    ${password}

    Wait Until Element Is Visible    name=username    15s
    Input Text    name=username    ${username}
    Input Text    name=password    ${password}
    Click Button    xpath=//button[@type='submit']

    ${login_success}=    Run Keyword And Return Status
    ...    Wait Until Element Is Visible    xpath=//span[@class='oxd-userdropdown-tab']    10s

    IF    ${login_success}
        Logout From OrangeHRM
    ELSE
        Log    Login failed for user ${username}    WARN
        Capture Page Screenshot
    END

Logout From OrangeHRM
    Click Element    xpath=//span[@class='oxd-userdropdown-tab']
    Wait Until Element Is Visible    xpath=//a[text()='Logout']    10s
    Click Element    xpath=//a[text()='Logout']
    Wait Until Element Is Visible    name=username    15s

Close OrangeHRM
    Close Browser

*** Test Cases ***
Login using Excel Data
    Log    Test executed using DataDriver
