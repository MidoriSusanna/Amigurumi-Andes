# Amigurumi Andes

Amigurumi Andes is an e-commerce platform that specializes in the sale of handcrafted goods directly to consumers. The business portfolio includes diverse products such as amigurumi, scarves, snoods, and hats, each meticulously crafted by skilled artisans. Rooted deeply in Chilean cultural heritage, Amigurumi Andes promotes sustainable and eco-friendly practices in its operations.

The platform serves a niche market of craft enthusiasts, collectors of handmade items, advocates of fair trade, and individuals with an appreciation for Chilean culture. By integrating the principles of fair trade and environmental consciousness, Amigurumi Andes aims to offer products that are both culturally significant and responsibly made, fostering a community of conscious consumers who value artisan craftsmanship and ethical production methods.

![Mock up](readme_pics/mockup.png)

[Link to the Deployed website](https://amigurumi-andes-8d4d6b3c47a6.herokuapp.com/)

# Project Goals and Stories
## Project Goals
- As a user I want to:
  - easily and intuitively navigate the website.
  - browse the website to be able to find the products and information I am looking for.
  - be able to buy products easily and quickly through different devices.
  - be able to interact with the interface and receive feedback when making a purchase, adding a blog post or joining an event.
  - create an account on the website to purchase a product and join the community.
  - search for blog posts and information I need.
  - join events organised by the community.
  - get in touch with the admin of the page.
  - be able to understand the privacy policy of the website and feel like I can make a safe payment. 
  - Understand the marketing presence of the business through the website, social media and newsletter.

  ## Epics and User Stories
  [Full list of EPICS available here](https://github.com/MidoriSusanna/Amigurumi-Andes/milestones)

  [Full list of open user stories available here](https://github.com/MidoriSusanna/Amigurumi-Andes/issues)

  [Full list of closed user stories available here](https://github.com/MidoriSusanna/Amigurumi-Andes/issues?q=is%3Aissue+is%3Aclosed)

# Agile Development
I utilized GitHub Issues and Projects for writing and managing user stories and epics. The Kanban board was employed to categorize stories into Todo, In Progress, and Done columns. Additionally, I applied the MoSCoW method to label stories as Must-Have, Could-Have and Should-Have.

[Kanban Board](https://github.com/users/MidoriSusanna/projects/2/views/1 )

# Design

**Fonts:**
- Crimson text for main titles.
- Open sans for paragraphs.

**Colour Palette:**
A very simple colour palette was chosen.

![Colour palette](readme_pics/palette.png)

## Wireframes

Wirefranes were created by me using Adobe Illustrator:

![Wireframes dekstop](readme_pics/wireframes-dekstop.png)
![Wireframes phone](readme_pics/wireframes-phone.png)

# Features 
## Header, nav bar and footer

The header is composed by the logo, a search bar, My Account section and the shopping bag. The My Account dropdown changes if the user is logged in. The cart shows in real time how much money the user is spending on items. Below this first part of the header, there is a menu section with different dropdowns: all products, amigurumi, accessories and about us. Below this section, there is a free delivery banner. 
This header features all pages.

![Header dekstop ](readme_pics/header.png)

On mobile version and smaller screens, the menu becomes an hamburger menu, where it is also possible to go back to homepage. 

![Header phone](readme_pics/header-phone.png)

The footer features all pages. It contains the company name, a brief description of the company, social media icons. In a second column links to contact us page, privacy policy and FAQs. In a third column the form to subscribed to the newsletter. If the user subscribe to the newsletter, a thank you message is provided. 

![Footer](readme_pics/footer.png)

## Homepage
The homepage is composed by a hero image with a shop now button that brings the user to the product page. It is also composed by a section with 3 cards, each one of them bringing to a different part of the website and providing a preview of the website content.

![Homepage](readme_pics/homepage.png)

## Product Page
The product page shows the total number of products available, each product with a picture, name of the product, cost and rate. This page has also a sorting function, where it is possible to sort the products by name, price, rating and category. It is possible only for the superadmin to edit and delete products direclty from the frontend and not just in the admin page.

![Product page](readme_pics/products.png)

## Product Detail
The product details page shows a picture of the product, the name of the product, price, rating, description, size (if available), chosen quantity and the options of adding the product to bag or keep shopping on the product page. The quantity can be increased with the "+" button or decreased with the "-" button, but it cannot go below 1. To make any purchase, the user needs to be logged in.


![Product details](readme_pics/product-details.png)

## Shopping Bag
The shopping bag gives the logged-in user the possibility to check their purchases before heading to checkout. This page contains again the product details and provides the user with subtotal and total, also adding the delivery charges if applicable. From this page, it is possible to go to secure chekout or go back to the products page.

![shopping bag](readme_pics/shoppingbag.png)

## My profile
The profile section is available only to logged in users. It is possible for the user to save delivery information and update them to guarantee a quicker buying experience. The profile shows also a order story. 

![My profile](readme_pics/myprofile.png)

## Checkout
The checkout page might be pre-filled if we tick "Save this delivery information to my profile", otherwise the user needs to fill it our to complete the purchase. The payment is processed via Stripe and can be controlled by the admin with webhooks. On this page is possible to see a sum of the purchases, the total and complete the order or adjust the bag. 

![Checkout1](readme_pics/checkout1.png)
![Checkout2](readme_pics/checkout2.png)

## Authentication
Only authenticated users have access to many of the website features. An autenticated user has access to: buying products, having a profile, join or leave events, add blog posts. The authentication system was made with allauth templates. The sign up for an account, the user needs to provide email address, username and a password. Upon registration, a confirmation email is sent to the user for the final set up. It is also possible to change the password and restore the profile via an email confirmation. To do this, it is possible to go to the sign in page and click "Forgot your password?". It is possible to save the password to the browser.

![Sign up](readme_pics/signup.png)
![Sign in](readme_pics/signin.png)
![Sign out](readme_pics/singout.png)

## About
The about page is a simple page with a picture and description of the philosophy of the business.

![About](readme_pics/about.png)

## Blog and blog detail
The blog page consists of 6 posts per page about relevant topics to the community. The preview of the post contains title, excert, date and author. It is possible for authenticated users to add a blog post. The admin needs to approve the blog post, and can perfomr CRUD functionality from the frontend and from the admin page. Logged in users can also edit and delete their posts.

![Blog](readme_pics/blog.png)
![Blog detail](readme_pics/blogdetail.png)

## Events and My events
The event page showcase the available events to the logged in users. To join an event, the user needs to be logged in. Once the user has joined the event, the "join event" button disabled and the event appears in the page "my events". In the My Events page, the user can decide to leave the event, this way the admin will see that the participation has been cancelled in the admin panel. When the user joins an event, they receive a confirmation email. 

![Events](readme_pics/events.png)

![My events](readme_pics/myevents.png)

## Product Management
The Product Management page is useful for the superuser to add products directly from the webpage, without using the admin panel.

![Product Management1](readme_pics/productman1.png)
![Product Management2](readme_pics/productman2.png)

## Privacy Policy
The privacy policy is useful for every user to understand the policies of the company and make purchases in a safa way.

![Privacy Policy](readme_pics/privacy-policy.png)

## FAQs
FAQs are useful for the users to find information before getting in touch with the admins. The superuser can perform CRUD funcionalities both from the admin panel and from the website/frontend. 

![FAQs](readme_pics/faqs.png)

## Messages and Emails
A system of messages has been implemented to provide feedback for every user's action. Messages are given in different circumstances, as: log-in, log-out, sign-in, sign-up, emails have been sent to confirm, update item to bag, remove item from bag, posted blog successfully, await for approval for the blog, successfully delete/edit a blog post...

![Example message 1](readme_pics/example-mess-1.png)
![Example message 2](readme_pics/example-mess-2.png)

Email confirmations are sent in different occasions: mainly to manage the account registration and also to confirm joining an event. 
![Example email](readme_pics/example-email.png)

# Database Chart

![Database 1](readme_pics/database1.png)
![Database 2](readme_pics/database2.png)
![Database 3](readme_pics/database3.png)

**Relationships**
- **Post-User:** Post is linked to User via a ForeignKey on the author field. This relationship indicates that each post is authored by a single user, establishing a many-to-one relationship from Post to User.
- **Order-UserProfile:** Order is linked to UserProfile via a ForeignKey on the user_profile field. This allows each order to be associated with a user profile. It's a many-to-one relationship where one user profile can have multiple orders.
- **OrderLineItem, Order, and Product:** 
OrderLineItem serves as the connection between Order and Product through two ForeignKeys:
1. order: Links to an Order, signifying that each line item is part of a specific order.
2. product: Connects to a Product, indicating which product is included in the order line.
- **Event-User(EventJoin):** 
EventJoin model uses two ForeignKeys to connect Event and User:
1. user: Indicates the user who is participating in an event.
2. event: Points to the event in which the user is participating.
This setup implements a many-to-many relationship, allowing many users to participate in many events.
- **Product-Category:**
Product is related to Category through a ManyToManyField.
- **User Profile-User:**
UserProfile has a OneToOneField with User. This direct link ensures that each user has a unique profile.

