*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    String
Suite Setup    Setup Test Data
Suite Teardown    Delete All Sessions

*** Variables ***
${BASE_URL}    http://localhost:5000

*** Test Cases ***

# ---------------- Restaurant Module ----------------
Update Restaurant
    ${body}=    Create Dictionary    name=Food Hub Updated
    ${response}=    PUT On Session    foodie    /api/v1/restaurants/${restaurant_id}    json=${body}
    Status Should Be    200    ${response}

Disable Restaurant
    ${response}=    PUT On Session    foodie    /api/v1/restaurants/${restaurant_id}/dis
    Status Should Be    200    ${response}

Get Restaurant
    ${response}=    GET On Session    foodie    /api/v1/restaurants/${restaurant_id}
    Status Should Be    200    ${response}

# ---------------- Dish Module ----------------
Update Dish
    ${body}=    Create Dictionary    price=150
    ${response}=    PUT On Session    foodie    /api/v1/dishes/${dish_id}    json=${body}
    Status Should Be    200    ${response}

Toggle Dish
    ${body}=    Create Dictionary    enabled=True
    ${response}=    PUT On Session    foodie    /api/v1/dishes/${dish_id}/status    json=${body}
    Status Should Be    200    ${response}

Delete Dish
    ${response}=    DELETE On Session    foodie    /api/v1/dishes/${dish_id}
    Status Should Be    200    ${response}

# ---------------- User Module ----------------
Search Restaurant
    ${params}=    Create Dictionary    name=Food Hub    location=City Center
    ${response}=    GET On Session    foodie    /api/v1/restaurants/search    params=${params}
    Status Should Be    200    ${response}

# ---------------- Order Module ----------------
Give Rating
    ${body}=    Create Dictionary    order_id=${order_id}    rating=5    comment=Excellent
    ${response}=    POST On Session    foodie    /api/v1/orders/ratings    json=${body}
    Status Should Be    201    ${response}

View Orders User
    ${response}=    GET On Session    foodie    /api/v1/orders/${user_id}
    Status Should Be    200    ${response}

View Orders Restaurant
    ${response}=    GET On Session    foodie    /api/v1/orders/restaurant/${restaurant_id}
    Status Should Be    200    ${response}

# ---------------- Admin Module ----------------
Approve Restaurant
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/${restaurant_id}/approve
    Status Should Be    200    ${response}

Disable Restaurant Admin
    ${response}=    PUT On Session    foodie    /api/v1/admin/restaurants/${restaurant_id}/disable
    Status Should Be    200    ${response}

View Feedback
    ${response}=    GET On Session    foodie    /api/v1/admin/feedback
    Status Should Be    200    ${response}

View Orders Admin
    ${response}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${response}

*** Keywords ***
Setup Test Data
    [Arguments]    ${restaurant_id}=
    Create Session    foodie    ${BASE_URL}

    # Create Restaurant
    ${body}=    Create Dictionary    name=Food Hub    category=Fast Food    location=City Center    images=[]    contact=1234567890
    ${resp}=    POST On Session    foodie    /api/v1/restaurants/    json=${body}
    Should Be Equal As Integers    ${resp.status_code}    201
    ${json}=    Set Variable    ${resp.json()}
    ${id}=      Get From Dictionary    ${json}    id
    Set Suite Variable    ${restaurant_id}    ${id}

    # Create Dish
    ${body}=    Create Dictionary    name=Pizza    type=Main    price=120    available_time=10:00-22:00    image=""
    ${resp}=    POST On Session    foodie    /api/v1/dishes/    json=${body}
    Should Be Equal As Integers    ${resp.status_code}    201
    ${json}=    Set Variable    ${resp.json()}
    ${id}=      Get From Dictionary    ${json}    id
    Set Suite Variable    ${dish_id}    ${id}

    # Create User
    ${rand}=    Generate Random String    6
    ${email}=   Set Variable    user${rand}@test.com
    ${body}=    Create Dictionary    name=Alice    email=${email}    password=123
    ${resp}=    POST On Session    foodie    /api/v1/users/register    json=${body}
    Should Be Equal As Integers    ${resp.status_code}    201
    ${json}=    Set Variable    ${resp.json()}
    ${id}=      Get From Dictionary    ${json}    id
    Set Suite Variable    ${user_id}    ${id}

    # Place Order
    ${body}=    Create Dictionary    user_id=${user_id}    restaurant_id=${restaurant_id}    dishes=[]
    ${resp}=    POST On Session    foodie    /api/v1/orders/    json=${body}
    Should Be Equal As Integers    ${resp.status_code}    201
    ${json}=    Set Variable    ${resp.json()}
    ${id}=      Get From Dictionary    ${json}    id
    Set Suite Variable    ${order_id}    ${id}
