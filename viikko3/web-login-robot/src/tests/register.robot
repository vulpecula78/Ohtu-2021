*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Register With Valid Username And Password
    Click Link  Register new user
    Set Username  jokke
    Set Password  jyvatykk1
    Set Password confirmation  jyvatykk1
    Submit Credentials Register
    Register Should Succeed
    
Register With Too Short Username And Valid Password
    Click Link  Register new user
    Set Username  ma
    Set Password  jyvatykk1
    Set Password confirmation  jyvatykk1
    Submit Credentials Register
    Register Should Fail With Message  Username is too short
    
Register With Valid Username And Too Short Password
    Click Link  Register new user
    Set Username  jouko
    Set Password  jyva1
    Set Password Confirmation  jyva1
    Submit Credentials Register
    Register Should Fail With Message  Password is too short
    
Register With Nonmatching Password And Password Confirmation
    Click Link  Register new user
    Set Username  jouko
    Set Password  jyvatykk1
    Set Password confirmation  jyvatykk2
    Submit Credentials Register
    Register Should Fail With Message  Nonmatching password and Confirmation
    
Login After Successful Registration    
    Go To Login Page
    Set Username  jokke
    Set Password  jyvatykk1
    Submit Credentials
    Login Should Succeed
    
Login After Failed Registration
    Go To Login Page
    Set Username  jouko
    Set Password  jyva1
    Submit Credentials
    Login Should Fail With Message  Invalid username or password
    
*** Keywords ***
Submit Credentials Register
    Click Button  Register
    
Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!
    
Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
