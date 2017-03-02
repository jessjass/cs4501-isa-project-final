# User Stories
1. As a user, I want to see all events on the events page.
  * Reasoning: Events are a core part of any transaction and a user should be able to see all options.
  * Acceptance Criteria (Tests):
    * Web Layer: Should be able to display events in the form of tiles with title, description, datetime and price showing.
    * Exp Layer: Should make requests to the Events entity and return a json response object to the web layer with all events.
    * Model Layer: Should query the db and return a json response object to the exp layer with all events.

2. As a user, I want to see all experiences on the experiences page.
  * Reasoning: Experiences are groups of events and can be part of a transaction.
  * Acceptance Criteria (Tests):
    * Web Layer: Should be able to display experiences in the form of tiles with title, description, and total price showing.
    * Exp Layer: Should make requests to the Experiences entity and return a json response object
    * Model Layer: Should query the db and return a json response object to the exp layer with all experiences.

3. As a user, I want to create an event.
  * Reasoning: As part of the marketplace, a user should be able to post an event with pricing.
  * Acceptance Criteria (Tests):
    * Web Layer: Should be able to fill out a form with the fields, upload an image, and be able to see their new post. 
    * Exp Layer: Should be able to make a successful post request to the models layer. 
    * Model Layer: Should be able to create a new Event instance in the db.

4. As a user, I want to see all events associated with an experience.
  * Reasoning: Experiences are groups of events so a user should see what events are involved.
  * Acceptance Criteria (Tests):
    * Web Layer: Should list all events when a user enters a experience details page.
    * Exp Layer: Should be able to make a successful request to get events by experience.
    * Model Layer: Should query the db and return the list of events in an experience.

5. As a user, I want to see which events I am attending.
  * Reasoning: As part of the user experience, a user should be able to see the events they've signed up for.
  * Acceptance Criteria (Tests):
    * Web Layer: Should be able to visit their user home page and see their events.
    * Exp Layer: Should make a request to the Users entity to get a User's event list. Given that event list, may have to make requests to the Events entity to get more details.
    * Model Layer: Should query the db successfully for the info requested by the experience layer.

6. As a user, I want to see which experiences I am associated with.
  * Reasoning: As part of the user experience, a user should be able to see the experiences they've signed up for.
  * Acceptance Criteria (Tests):
    * Web Layer: Should be able to visit their user home page and see their experiences.
    * Exp Layer: Should make a request to the Users entity to get a User's experience list. Given that experience list, may have to make requests to the Experience entity to get more details.
    * Model Layer: Should query the db successfully for the info requested by the experience layer.

7. As a user, I want to see the details of a specific event.
  * Reasoning: Before purchasing, a user may want more details to decide if an event is right for them.
  * Acceptance Criteria (Tests):
    * Web Layer: Should be able to click an event and get more details.
    * Exp Layer: Should make a request to the Event entity to get more details.
    * Model Layer: Should successfully query the db for an event by primary key.

8. As a user, I want to see the details of a specific experience.
  * Reasoning: Before purchasing, a user may want more details to decide if an experience is right for them.
  * Acceptance Criteria (Tests):
    * Web Layer: Should be able to click an experience and get more details.
    * Exp Layer: Should make a request to the Experience entity to get more details.
    * Model Layer: Should successfully query the db for an experience by primary key.

9. As a user, I want to see my user profile.
  * Reasoning: A user may want a central location to view their events or experiences.
  * Acceptance Criteria (Tests):
    * Web Layer: Should display a user logo on the navbar and go to a user home page when clicked.
    * Exp Layer: Should make a request to the User entity to get more details.
    * Model Layer: Should successfully query the db for a user profile by primary key.

10. As a user, I want to edit my user profile.
  * Reasoning: A user may want to change or update info to be more relevant.
  * Acceptance Criteria (Tests):
    * Web Layer: Should display a 'update profile' button that transforms profile to form that can be submitted by clicking 'save changes'.
    * Exp Layer: Should make a request to the User entity to update details.
    * Model Layer: Should successfully query and update the db for the specified user profile.

11. As a user, I want to see my list of friends.
  * Reasoning: A user may want to see who they are friends with to view their event/experience interests.
  * Acceptance Criteria (Tests):
    * Web Layer: Should display a friends list on the user profile.
    * Exp Layer: Should query the Users entity to get the friends of a user.
    * Model Layer: Should successfully query the db to return a list of users.

12. As a user, I want to see events my friends are going to.
  * Reasoning: A user would be more inclined to join events their friends are going to. 
  * Acceptance Criteria (Tests):
    * Web Layer: Should display a 'events your friends are going to' section.
    * Exp Layer: Should have some logic that queries friends and handpicks the closest events they're attending and returns them to the web layer.
    * Model Layer: Should return the list of friends and list of events each friends is going to from the db.

13. As a user, I want to see experiences my friends are associated with.
  * Reasoning: A user would be more inclined to join experiences their friends are going to. 
  * Acceptance Criteria (Tests):
    * Web Layer: Should display a 'experiences your friends are going to' section.
    * Exp Layer: Should have some logic that queries friends and handpicks the closest experiences they're attending and returns them to the web layer.
    * Model Layer: Should return the list of friends and list of experiences each friends is going to from the db.
