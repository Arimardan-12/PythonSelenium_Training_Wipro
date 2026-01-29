*** Settings ***
Library    Process
Library    SeleniumLibrary

*** Test Cases ***
Environment Setup Verification
    Log    ===== Starting Environment Verification =====

    Log    Checking Python installation...
    Run Keyword And Continue On Failure    Verify Python Installed

    Log    Checking Robot Framework installation...
    Run Keyword And Continue On Failure    Verify Robot Installed

    Log    SeleniumLibrary imported successfully.

    Log    ===== Environment Verification Completed =====


*** Keywords ***
Verify Python Installed
    ${result}=    Run Process    python    --version    stdout=PIPE    stderr=PIPE
    Run Keyword If    ${result.rc} != 0    Fail    Python is NOT installed or not added to PATH
    Log    Python Version: ${result.stdout}

Verify Robot Installed
    ${result}=    Run Process    python    -m    robot    --version    stdout=PIPE    stderr=PIPE
    Should Contain    ${result.stdout}    Robot Framework
    Log    Robot Framework Version: ${result.stdout}
