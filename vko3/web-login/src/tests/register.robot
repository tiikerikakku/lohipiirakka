*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
  set username  viola
  set password  kukkan3n
  submit credentials
  register should succeed

Register With Too Short Username And Valid Password
  set username  x
  set password  valid000
  submit credentials
  register should fail with message  Invalid username

Register With Valid Username And Too Short Password
  set username  bukett
  set password  x
  submit credentials
  register should fail with message  Password too short

Register With Valid Username And Invalid Password
  set username  hbl
  set password  longbutinvalid
  submit credentials
  register should fail with message  Password too simple

Register With Nonmatching Password And Password Confirmation
  set username  raaste
  input password  password  s0methin
  input password  password_confirmation  s0mething
  submit credentials
  register should fail with message  Passwords do not match

Register With Username That Is Already In Use
  set username  xyz
  set password  abab0123
  submit credentials
  register should fail with message  User with username xyz already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
  reset application
  create user  xyz  abcdef12
  go to register page

Register Should Succeed
  Welcome Page Should Be Open

Register Should Fail With Message
  [Arguments]  ${message}
  Register Page Should Be Open
  Page Should Contain  ${message}

Submit Credentials
  Click Button  Register

Set Username
  [Arguments]  ${username}
  Input Text  username  ${username}

Set Password
  [Arguments]  ${password}
  Input Password  password  ${password}
  input password  password_confirmation  ${password}
