# DjangoRealEstate
Django Real Estate

**Summary**

Integration of a real estate web application in django. As with most sites, the main idea applies here, when the user assigns a house or anything depending on the options given to him and undertaken by the broker, after contacting the user. Also, the user at his assignment can choose the brokers he wants to undertake or the broker can reject the request from the user. Users are divided into two categories, ordinary users and brokers.


You can see the template [here](https://themeforest.net/item/manland-bootstrap-light-real-estate-html-template/26864388)

**Installation**

1. You can download or you can use `git clone https://github.com/alexdotis/DjangoRealEstate.git`
2. Go to directory `RealEstate` and `pip3 install -r requirements.txt`
3. `python3 manage.py makemigrations`
4. `python3 manage.py migrate`
5. You can use `python3 manage seed` to prepopulate the database with fake propeties, agents, users, blogs
   - By default it will create 10 agents that each will have 20 properties, 30 blogs and 10 users.
   - All agents and users have the same password `qwerty`
   - You can use the options `--properties (int)` `--agents (int)` `--blogs (int)` `--users (int)` if you want to change the numbers
6. `python3 manage.py createsuperuser`
7. **Note** : Before you run the server, please go to `RealEstate/urls.py` and uncomment the comments.
8. `python3 manage.py runserver`

You are good to go.

On `RealEstate` directory there is a `houses` folder that contains images in case you want to change or add a property.

Enjoy!

**Screenshots**

![Alt Text](https://github.com/alexdotis/DjangoRealEstate/blob/main/screenshots/screenshot1.jpg)

![Alt Text](https://github.com/alexdotis/DjangoRealEstate/blob/main/screenshots/screenshot2.jpg)
