# Just One More MS4

Just one more is a e-commerce site for lovers of gaming, music and tech.

# User Experience (UX)

## User Stories

### First Time User

1. I want to be able to see what is available quickly
2. I want to be able to navigate certain categories as well as sort within those categories
3. I would like to be able to add items to my bag and also dictate how much of said item I would like to add
4. If I select clothing I would like to able change the sizes and the size for me
5. Once my items are in the bag I would like to be able remove, update qty said items.
6. I would also like to able to see a total of the items within the bag.
7. Once in checkout and have filled out my details I would like to be able to save details for if I come back
8. Finally I would like to able to register an account

### Regular User/Super User 

1. I would like to be able to log in to my account using the credentials I used previously.
2. If for whatever I forget my password or username, i'd like the option to reset said credentials
3. Once I am signed into my account, I would like to able update my details if need be.
4. I would also like to be able to see my previous orders.
5. If I want to buy items, I would like the checkout form to be pre-filled with the details I have provided
6. **SUPERUSER ONLY** If I am the site owner or have been given super user access I would like to be able to add, edit and delete products should I see fit to do so. 
7. **SUPERUSER ONLY** If I am a super user I would the product management to only to myself and other super users.

## Scope

### Overview
This site is designed around my own interests in music and video games. I want the website to a one stop shop for all products related to gaming and music. I wanted it have
a simple and clean design so it is not too overwhelming for the user and not so in your face. It meant to be inviting and harkens back to my first project by adopting,
Minimal Viable Product, the advantage of this for new users of the site is, it is easy to understand and conveys a message effectively but simply. My Skill-set has raised
since my first project however and I have added a lot of back-end trickery that the front-end user shouldn't notice while still keeping the site as a whole clean.

# Database

During the development of the site I used SQLite3
Once deployed it was changed over to PostgresSQL which is provided by heroku

The database is from multiple apps and has models relevant to what is needed for things like, users, products and reviews.
These are my database tables and my Database ER Diagram

## Profile App

### UserProfile model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user | OneToOneField |  User, on_delete=models.CASCADE
 Phone number | default_phone_number | CharField | max_length=20, null=True, blank=True
 First Address Line | default_first_address_line | CharField | max_length=80, null=True, blank=True
 Second Address Line | default_second_address_line | CharField | max_length=80, null=True, blank=True
 Town or City | default_city | CharField | max_length=30, null=True, blank=True
 County | default_county | CharField | max_length=80, null=True, blank=True
 Postcode | default_postcode | CharField | max_length=15, null=True, blank=True
 Country | default_country | CountryField | blank_label='Country', null=True, blank=True

## Checkout App

### Order model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order number | order_number | CharField | max_length=32, null=False, editable=False
 User profile | user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 Full name | full_name | CharField | max_length=50, null=False, blank=False
 Email| email| EmailField | max_length=254, null=False, blank=False
 Mobile number | mob_number | Charfield | max_length=20, null=False, blank=False
 Country| country | CountryField | blank_label='Country *', null=False, blank=False
 Postcode | postcode | CharField | max_length=20, null=True, blank=True
 Town or City | city | CharField | max_length=40, null=False, blank=False
 First Address Line | first_address_line | CharField | max_length=80, null=False, blank=False
 Second Address Line | second_address_line | CharField | max_length=80, null=True, blank=True
 Date | date | DateTimeField | auto_now_add=True
 Delivery cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
 Order total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 Grand total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 Original bag | original_bag | TextField | null=False, blank=False, default=''
 Stipe pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

### OrderLineItem model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order  | order | ForeignKey | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
 Product | product | ForeignKey | Product, null=False, blank=False, on_delete=models.CASCADE
 Product Size | product_size | CharField | max_length=3, null=True, blank=True
 Quantity | quantity | IntegerField | null=False, blank=False, default=0
 Lineitem total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False

## Products App

### Category model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 name | name | CharField | max_length=256
 Friendly name | friendly_name | CharField | max_length=256, null=True, blank=True

### Product model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Category| category| ForeignKey | Category, null=True, blank=True, on_delete=models.SET_NULL
 Sku | sku | CharField | max_length=256, null=True, blank=True
 Name | name | CharField | max_length=256
 Age Rating | age_rating | CharField | max_length=10, null=True, blank=True
 Platform | platform | CharField | max_length=256, null=True, blank=True
 Genre | genre | CharField | max_length=256, null=True, blank=True
 Sizes | sizes | BooleanField | default=False, null=True, blank=True
 Description | description | TextField
 Price | price | DecimalField | max_digits=6, decimal_places=2
 Rating | rating | DecimalField | max_digits=6, decimal_places=2
 Image URL | image_url | URLField | max_length=1024, null=True, blank=True
 Image | image | ImageField | null=True, blank=True

### Review Model
 
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
User | user | ForeignKey | User, on_delete=models.CASCADE
Product | product | ForeignKey | Product, related_name='reviews', on_delete=models.CASCADE
Date | date | DateTimeField | auto_now_add=True
User Review | user_review | TextField | max_length=500, blank=True
Rating | rate | PositiveSmallIntegerField | choices=ONE_TO_FIVE

# Features

## Implemented Features

1. Register an account.
2. Login to said account.
3. Log out of the account
4. Reset Password if needed
5. Reset Email if needed
6. **SUPER USER ONLY** Add a new product
7. **SUPER USER ONLY** Edit a product
8. **SUPER USER ONLY** Delete a product
9. Search for an item
10. Filter products by name, price, a-z etc..
11. Review a product and see said review.
12. Toasts so the user knows when they perform certain tasks like adding to basket
13. Live updating basket with order total
14. The ability to save information from the payment page.
15. Secure checkout and order confirmation generation
16. Sending real emails to customer

## To be implemented

1. To be able to remove your user reviews unless your the superuser where you can delete any of them
2. Carousel to implemented on the front page to show more products, easy to do just wanted to get the site functional first

# Wireframes

![Home_Page](/README_IMAGES/just_one_more_home.jpeg)

![Product_page](/README_IMAGES/just_one_more_product.jpeg)

![Product_detail](/README_IMAGES/just_one_more_productdetails.jpeg)

# Testing

## Navigation Bar

### Just One More

- When I click the name of the page, Just one More, it takes you to the home page regardless of which page I am. This work on all devices

### Navigation Buttons 

- There are a few navigation links that consist of the types of products that are avalible on the page. These links all have dropdowns which will allow the user to sort
the products into price, rating, platform etc.. For the Super User I have also added the ability to see all products at once. The reason I have done this is because
the vast majority of e-commerce sites don't have this option due to the vast quantity of products. Though my site is small I didn't want to treat as though it was a small site but rather an expanding one which I can hundreds or thousands of products too.

### Search

- The search is present all the time during desktop versions of the site and is hidden away in the offcanvas nav bar. The search bar allows to search for products. When you type a word in to the search bar, as long as it is the description of the product or title of the product. It will return those products to the screen for the user to see. If you type something in that doesn't appear in the parameters mentions then it will return a message to say "No Product Found" and redirect you to the products page.

## Products

### Products Page

- The overall product pages don't do much apart from display the products avalible to the customer. This does need to be linked to the database attached with django or postgres which worked flawlessly.

### Product Detail Page

- The Product detail is much the same as the product page apart from displaying all of the products it will only show the one you clicked on.

### Add to basket

- Any users of the website can add items to the bag. In addition to this you can also specify quantity of the items and size of the product, if this option have been avalible to said product

### Add Product

- The Super user has the ability to add products by clicking the product management button. This is linked to the add_product function in the views. This works perfectly and once the product has been added it will redirect to the product which the super user has made. There are few requirements for the add product but because the page is meant to be used for many different types of products.

### Edit Product

- Once again the edit_product function is only accessible to the super user. This form can be accessed through a specific products page, so for example if i want to edit God of War:Ragnarok then I have to click into said page. Once in the super user will be presented with the edit product button which will redirect him to a form very similar to the add_product form. The fields will be pre-filled and you can just edit the applicable fields. Once complete you will be returned to said products page

### Remove Product

- Again only accessible to the super user. The delete button is also avalible through the specific product page. You will be able to see the delete product button which will instantly delete the product you are in and return you to the products page. I would like to at some point add a modal so that the user can be prompted to this action before committing.

### Reviews

- Any signed in user has the ability to add a review for the product they are in. This will displayed the bottom of the specific page they are on and only requires to fields, User Review and Rating. Once the review has been written it will display on the product items page with the review, rating and created_by tags. I would like to add the delete review function at some point but for now I just wanted to get it working.

## Bag

### Basket 

- The basket button is live and any product that is added to the bag will then display the product price in basket icon in the bottom right of the screen. The user will also be prompted with a message confirming the product added to the basket.

### Bag

- The bag is accessible only once you have an item in your bag. The only exception to this is when you remove items from the bag it will display a message saying the bag is empty and will prompt the user to go back to the products page. If you do have products in the bag you will be able to see which products you have added, in addition to this depending on the type of product you have added it will display specific details which are applicable to that product, like sizes, quantity and platform.

## Checkout 

### Checkout form

- The form is generated through `forms.py` and displayed to the user via `crispy_forms`. The fields that are displayed are as follows.

1. Full Name
2. Email
3. Mobile Number
4. First Address Line
5. Second Address Line
6. Town or City
7. County
8. Postcode
9. Country
10. Stripe Payment Form

### Stripe Payments

- The payment system is handled through Stripe. Stripe enables me to test the function of the checkout form by using "4242 4242 4242 4242" Card number. This send a test to the stripe server side and generate a "successful" payment. You can also use other forms of testing like "4000 0027 6000 3184" which make authorize the payment manually before it submits

### Email Confirmation

- Once a successful payment has been processed you will recieve an email which will have details of the order, like order number, product name etc.... 

## Profile

### Registration

- If you are not signed in you will have the option to register an account. Once you click register account you will be redirected to the registration screen where you will be prompted to fill out the form. This form does have built in security features built in which is from `django-all_auth`. Such features are, min and max length of username and password and password similarity. Once you have been filled the form out the user will be sent an email with a confirmation link. Once that link has been clicked you will asked to confirm which finishes the registration process

### Sign in

- If you have registered you will be given the option to sign in. The credentials from your previous registration are all saved, so all you have to do is hit sign in and login with the details given. You can also request for the form to remember you, this should only be used on a private machine however.

### Profile 

- Once you have an account you will have access to more features, like saving delivery details and being able to leave a user review. You can also update your details through the account page. If you have placed any order you will also see your previous orders, these can be clicked into allowing you to review your orders without searching through emails.

## Summary

Every single feature has been tested and works as expected. 


# Testing User Stories

## As a New User

1. I want to be able to see what is available quickly
- You will be greeted with a splash image of a pre-order and also the navigation links are always at the top (on desktop) and easy to navigate

2. I want to be able to navigate certain categories as well as sort within those categories
- Through the dropdown menus of the navigation links you are able to sort specific categories by things like price, rating, platform etc.. If you then click into any of these links you are then able to sort further through a sort by dropdown

3. I would like to be able to add items to my bag and also dictate how much of said item I would like to add
- Once you click in a product, you'll be shown a big add to basket button. Once you hit that not only will the total of the basket update in the bottom left but you will be given a prompt confirming item has been added successfully

4. If I select clothing I would like to able change the sizes and the size for me
- On applicable items sizes are available ranging from XS to XL

5. Once my items are in the bag I would like to be able remove, update qty said items.
- If you have added an item by mistake or would like to modify the amount of said item. By navigating to the basket you will be able to remove the item and/or update

6. I would also like to able to see a total of the items within the bag.
- The bag will give a order total and a delivery cost, which will be combined into a grand total.

7. Once in checkout and have filled out my details I would like to be able to save details for if I come back
- The checkout allows users to save delivery details, but not payment details as I need to find a secure of securing this very sensitive details

8. Finally I would like to able to register an account
- Registering an account is easy. Just by clicking register, follow the steps and your account will be set up and unlock new features

### Regular User/Super User 

1. I would like to be able to log in to my account using the credentials I used previously.
- If you have created an account you will be able to log in to your account by clicking login, filling out the form with the credentials you have supplied previously.

2. If for whatever I forget my password or username, i'd like the option to reset said credentials
- You will be able to get a password reset by clicking sign in and clicking forgot password.

3. Once I am signed into my account, I would like to able update my details if need be.
- You can update your delivery details by navigating to my account, you will immediately greeted with the Delivery Details form where you can update your details

4. I would also like to be able to see my previous orders.
- Previous orders are also avalible to you via the account page. You can also access said orders by clicking the order number where it will give a more detailed view.

5. If I want to buy items, I would like the checkout form to be pre-filled with the details I have provided
- Once you have saved your delivery details the payment form will pre-filled with your details. This not apply to payment details however.

6. **SUPERUSER ONLY** If I am the site owner or have been given super user access I would like to be able to add, edit and delete products should I see fit to do so.
- You can very easily Create, Edit and Delete products. To create a product you will need to click product management where you can fill out the details of the product you would like to add to the products page. Once you have added the product you will redirected to the product page of the item you have just added. In this product page you will be to see the edit product and delete product buttons. Be careful with the delete button as at the moment it deletes the item immediately as appose to giving the user a warning. This will be implemented later.

7. **SUPERUSER ONLY** If I am a super user I would the product management to only to myself and other super users.
- Only super users will have access to these features.


