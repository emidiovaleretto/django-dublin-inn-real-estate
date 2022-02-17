 # Dublin Inn Real Estate

> ****Disclaimer***: The following Context is completely fictional, the company, the context, the CEO, the business questions exist only in my imagination.

> **For educational purposes only.

## Briefing

**Dublin Inn Real Estate** is a specialist rental company across Ireland. Based in Dublin, the company has a simple website that receives around 2,000 simultaneous hits per day.

In just over 1 year of the website, the marketing team of **Dublin Inn Real Estate** noticed that the volume of access to the website was falling, contributing with a significant portion of the company's revenue.

Based on this information, the team of analysts decided to investigate the reason for the decrease in access and found that the site had become obsolete and the system no longer supported the number of daily accesses, which required a redesign of the entire web application. Therefore, the marketing team launched a proposal to innovate the company's visual identity.

## Challenge

Concerned about this metric falling, the CEO of **Dublin Inn Real Estate** hired me to develop a new web application for the company.

At the end of the work, it is expected that a new application will be delivered, with a new identity, new functionalities, reliable and scalable, which supports more simultaneous accesses than the old website.

The company's business team gave me a report on the features that the CEO wants:

> 1. A website whose purpose of the company is immediately understood by the user.
> 2. Have a clear information on what the site is about and what it provides
> 3. Have an easy navigation that is consistent throughout the website
> 4. Consistent layout without any confusing elements
> 5. Accessibility considerations are taken throughout the site
> 6. A form where the user can filter the search by properties, passing information such as location, property type and price range (*This functionality does not exist in the current application*).
> 7. A functionality where the user can schedule a visit to one or more properties and a dashboard where he can view, edit and/or delete a visit (*This functionality does not exist in the current application*).

## Business Rules

The application's administrative functions are intended to manage what each user can do within the system. Permissions such as adding, editing or removing a property, for example, should under no circumstances be given to the user of the application. Such functionalities must be assigned exclusively to the administrator.

In the system, there will be the following user functionalities:

   - Admin: has permission in all areas of the system.
   - Users: can edit your own profile like change profile picture or change password. The user can search for properties by **location**, **type** of property (apartment, house, studio, etc.), **price range**, in addition to being able to schedule visits, edit date and time of visit (according to availability) and you can also cancel a certain scheduled visit.

## Screens

- Admin:
    - will be able to manage users.
    - Add/Edit/Remove properties.
    - View all screens users can view as well.
- Users:
    - can log in and out of the application.
    - manage his/her own profile.
    - form to search for properties.

# User Interface UI

## Skeleton

 The wireframes were created in [Figma](https://www.figma.com/).

### Desktop Homepage

<img src="./readme-files/wireframes/desktop_homepage.jpg" width="560" height="2412">