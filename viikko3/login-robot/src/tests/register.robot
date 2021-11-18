*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jokke  jyvatykk1
    Output Should Contain  New user registered
    
Register With Already Taken Username And Valid Password
    Input Credentials  jakke  123jakke
    Output Should Contain  User with username jakke already exists
    
Register With Too Short Username And Valid Password
    Input Credentials  se  passwd12
    Output Should Contain  Username is too short
    
Register With Valid Username And Too Short Password
    Input Credentials  jokke  1yhytpw
    Output Should Contain  Password is too short
    
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jokke  jyvatykki
    Output Should Contain  Not a valid password
    
*** Keywords ***
Input New Command And Create User
    Create User  jakke  salasana123
    Input New Command
