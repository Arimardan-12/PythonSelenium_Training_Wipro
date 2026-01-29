*** Settings ***
Library    BuiltIn

*** Variables ***
${NAME}        Robot Framework
${VERSION}     6.0
@{COLORS}      Red    Green    Blue

*** Test Cases ***
First Test Case - Logging Demo
    Log    This is a log message stored in the log file
    Log To Console    Hello from Robot Framework!
    Log    Name is ${NAME}
    Log    Version is ${VERSION}

Second Test Case - Variables Demo
    Log To Console    Demonstrating list variables
    Log    First color is ${COLORS}[0]
    Log    Second color is ${COLORS}[1]
    Log    All colors are ${COLORS}
