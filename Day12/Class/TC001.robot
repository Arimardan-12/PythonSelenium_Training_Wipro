*** Settings ***
Library     SeleniumLibrary


*** Keywords ***
open application
    Open Browser     https://www.google.com/       chrome
    Maximize Browser Window

*** Test Cases ***
Launch App Test
    Open Application
    Close Browser
