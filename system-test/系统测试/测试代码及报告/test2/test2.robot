*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser To Login Page
Suite Teardown    Close Browser

*** Variables ***
${URL}            http://localhost:8080
${BROWSER}        edge

*** Test Cases ***
Registration And Login Test
    [Documentation]    Test the registration and login functionality
    Click Element    id=signUp
    Input Text       css=input[placeholder="Username"]    testuser
    Input Text       css=input[placeholder="Id"]          testid
    Input Text       css=input[placeholder="Password"]    testpassword
    Scroll Element Into View    css=button.btn
    Click Button     css=button.btn
    Wait Until Element Is Visible    id=signIn

    Click Element    id=signIn
    Input Text       id=111    testid
    Input Text       id=222    testpassword
    Scroll Element Into View    id=333
    Sleep            2s
    Click Button     id=333
    Sleep            2s


    Click Element    id=svm
    Sleep            2s

    Click Button     id=start
    Sleep            5s


*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    id=signUp
