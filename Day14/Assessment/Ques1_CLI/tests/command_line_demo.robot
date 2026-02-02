*** Settings ***
Suite Setup       Suite Initialization
Suite Teardown    Suite Cleanup
Test Setup        Test Initialization
Test Teardown     Test Cleanup

*** Test Cases ***
Sample Tagged Test
    [Tags]    smoke
    Log    This is a tagged test case

Another Test Case
    Log    This is a normal test case

*** Keywords ***
Suite Initialization
    Log    Suite Setup: Executed before all test cases

Suite Cleanup
    Log    Suite Teardown: Executed after all test cases

Test Initialization
    Log    Test Setup: Executed before each test case

Test Cleanup
    Log    Test Teardown: Executed after each test case
