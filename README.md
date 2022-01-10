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
8. If I decide I do not want an account anymore I would like the option to delete my account and everything associated with it.

## Scope

### Overview
This site is designed around my own interests in music and video games. I want the website to a one stop shop for all products related to gaming and music. I wanted it have
a simple and clean design so it is not too overwhelming for the user and not so in your face. It meant to be inviting and harkens back to my first project by adopting,
Minimal Viable Product, the advantage of this for new users of the site is, it is easy to understand and conveys a message effectively but simply. My Skill-set has raised
since my first project however and I have added a lot of back-end trickery that the front-end user shouldn't notice while still keeping the site as a whole clean.

# Database

During the development of the site I used SQLite3
Once deployed it was changed over to PostgresSQL which is provided by heroku

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
