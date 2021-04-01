MODEL/DB FIELDS

# Listing
- id : INT(auto increment)
- realtor : INT (FOREIGN KEY [realtor]), (one to many: 1 realtor can list many listing)
- title : STR
- address : STR
- city : STR
- state : STR
- zipcode : STR
- description : TEXT (longer text)
- price : INT
- bedrooms : INT
- bathrooms : INT
- garage : INT (defalt = 0)
- list_date : DATE
- sqft : INT
- lot_size : FLOAT (decimal)
- is_published : BOOL [true]
- photo_main : STR
- photo_1 : STR
- photo_2 : STR
- photo_3 : STR
- photo_4 : STR
- photo_5 : STR
- photo_6 : STR


# Realtor

- id : INT
- name : STR
- photo : STR
- description : TEXT
- email : STR
- phone : STR
- is_mvp : BOOL (seller of the month) (defalt = 0)
- hire_date : DATE


# contact

- id : INT
- user_id : INT
- listing : INT
- listing_id : INT
- name : STR
- email : STR
- phone : STR
- message : TEXT
- contact_date : DATE