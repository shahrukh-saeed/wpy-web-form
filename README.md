# wpy-web-form

A user registration form made for WhoPlusYou.

I have hosted the webpage on Render and you can test it at https://wpy-web-form.onrender.com/

## Features

- Responsive design to accomodate varying screen sizes
- Comprehensive front-end validation using HTML5 and JavaScript
- Data stored in MySQL database hosted on PlanetScale

    **SQL command used to insert data into MySQL database (found in database.py)**

    ```
    INSERT INTO users (firstName, lastName, email, password, phone, address, city, province, country)
    VALUES ('{data['firstName']}', '{data['lastName']}', '{data['email']}', '{data['password']}', '{data['phone']}', '{data['address']}', '{data['city']}', '{data['province']}', '{data['country']}')
    ```

## Screenshots

**Desktop**
![Desktop](https://i.imgur.com/pYN6625.png)

![Desktop](https://i.imgur.com/xOY5RIb.png)

**Mobile Top**
![Mobile Top](https://i.imgur.com/0yzbRhb.png)

**Mobile Bottom**
![Mobile Bottom](https://i.imgur.com/j6dCCnk.png)

![Mobile Success](https://i.imgur.com/ODLeVWH.png)




