# Validation

## HTML

Each page has been validated with [W3 Validator](https://validator.w3.org/):

- Base.html:
Two errors are found, **those erros are presented in every page**
![Error index 1](readme_pics/indexhtml.png)
This error is actually not present in the base.html code, all li elements are children of ul elements. 
![Error index 2](readme_pics/indexhtml2.png)
This is due to the use of 'user-options' as an id and as an aria-labelledby tag.

- Products.html:
No errors found, only some div tags to close which have been fixed. 

- Edit Product:
Errors were found related to crispy form.
![Edit Product](readme_pics/editproducttest.png)

- About.html:
No errors found

- Events.html:
No errors found

- Blog.html:
No errors found

- Blog_detail.html:
No errors found

- Post edit:
Errors found related to summernote set up.

- Post delete:
No errors found

- Contact.html:
No errors found

- Product Managment:
Two errors were found due to the set up of crispy forms:

![Product Managment](readme_pics/productmanag.png)

- Profile page:
Two errors were found and corrected: one unclosed div and a repetition of a class tag. 

- Write blog page:
Several errors were found due to the set up of summernote. 

- My event page:
No errors found

- Shopping bag page:
No errors found

- Checkout Page:
Errors were found related to the use of Javascript.

![Checkout page](readme_pics/shoppingbagtest.png)

- Chekout success page:
No errors found

- Privacy Policy Page:
No errors found

- FAQ page:
No errors found

- Create New FAQ page:
No errors found

- Edit FAQ:
No errors found

- Delete FAQ:
No errors found

- Log out Page:
No errors found

- Sign in Page:
No errors found

- Sign up Page:
An error has been found related to allauth set up.

![Sign up error](readme_pics/signuptest.png)

# CSS

The custom css page has been validated with [W3C Validator](https://jigsaw.w3.org/css-validator/) and no errors were found:

![CSS validate](readme_pics/basecsstest.png)

# JS

The JS files have been validated with [JShint](https://jshint.com/), no errors were find apart from some "missing semicolon", which in Javascript are not always mandatory due to a feature called Automatic Semicolon Insertion.

Scroll:
![Scroll](readme_pics/scroll-js.png)

Bag JS:
![Bag](readme_pics/bag-js.png)

Add Product JS:
![Add Product](readme_pics/addproduct-js.png)

Product page JS:
![Product](readme_pics/products-jss.png)

Country field JS:
![Country field](readme_pics/countryfield-js.png)

Stripe JS:
![Stripe Js](readme_pics/stripe-js.png)

# Python

The project follows the PEP8 style guidelines and passes the [CI Phyton Linter](https://pep8ci.herokuapp.com) with no errors. 
The files settings.py and env.py have not undergone validation against the PP8 standards to prevent any potential disruptions to the application's functionality. These files are critical to the app's operation, and I opted to not modify them to ensure stability.
Some long lines have been left unmodified to preserve the integrity of the code without incurring in mistakes.

**Amigurumi Andes App:**
- Urls.py:
![Urls py AA](readme_pics/amigurumiandes-urls.png)
- Views.py:
![Views py AA](readme_pics/amigurumiandes-views.png)

**Home App:**
- Urls.py:
![Urls py Home](readme_pics/home-urls.png)
- Views.py:
![Views py Home](readme_pics/home-views.png)

**Bag App:**
- Context.py
![Context py bag](readme_pics/bag-context.png)
- Urls.py:
![Urls py bag](readme_pics/bag-urls.png)
- Views.py:
![views py bag](readme_pics/bag-views.png)

**Blog App:**
- Admin.py:
![Admin py blog](readme_pics/blog-admin.png)
- Forms.py:
![Forms py blog](readme_pics/blog-forms.png)
- models.py:
![Models py blog](readme_pics/blog-models.png)
- urls.py:
![urls py blog](readme_pics/blog-urls.png)
- views.py:
![views py blog](readme_pics/blog-views.png)

**Checkout App:**
- Admin.py:
![admin py checkout](readme_pics/checkout-admin.png)
- Forms.py:
![forms py checkout](readme_pics/checkout-forms.png)
- Models.py:
![models py checkout](readme_pics/checkout-models.png)
- urls.py:
![urls py checkout](readme_pics/checkout-urls.png)
- Views.py:
![views py checkout](readme_pics/checkout-views-E.png)
- Webhook handler.py:
![webhook handler py checkout](readme_pics/checkout-webh-handler-E.png)
- webhook.py:
![webhook py checkout](readme_pics/checkout-webh-E.png)

**Events App:**
- admin.py:
![admin py events](readme_pics/events-admin.png)
- forms.py:
![forms py events](readme_pics/events-form.png)
- models.py:
![models py events](readme_pics/events-model.png)
- urls.py:
![urls py events](readme_pics/events-urls.png)
- views.py:
![views py events](readme_pics/events-views.png)

**FAQs App:**
- forms.py:
![forms py faqs](readme_pics/faqs-forms.png)
- models.py:
![models py faqs](readme_pics/faqs-model.png)
- urls.py:
![urls py faqs](readme_pics/faqs-urls.png)
- views.py:
![views py faqs](readme_pics/faqs-views.png)

**Products App:**
- admin.py:
![admin py products](readme_pics/products-admin.png)
- forms.py:
![forms py products](readme_pics/products-form.png)
- models.py:
![models py products](readme_pics/products-model.png)
- urls.py:
![urls py products](readme_pics/products-urls.png)
- views.py:
![views py products](readme_pics/product-views-E.png)

**Profile App:**
- forms.py:
![forms py profile](readme_pics/profile-form.png)
- models.py:
![models py profile](readme_pics/profile-model.png)
- urls.py:
![urls py profile](readme_pics/profile-urls.png)
- views.py:
![views py profile](readme_pics/profile-views.png)


# Lighthouse report

# Responsiveness

The website is fully responsive across various browsers and screen sizes including desktops, tablets, and phones.

# Colour contrast

The website was tested for colour contrasts with [WAVE](https://wave.webaim.org) to improve accessibility, no concerning low contrast areas were found.
