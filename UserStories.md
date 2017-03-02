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
    * Exp Layer: Should be able to make a sucessful post request to the models layer. 
    * Model Layer: Should be able to create a new Event instance in the db.

4. As a user, I want to see all events associated with an experience.
  * Reasoning: 
  * Acceptance Criteria (Tests):
    * Web Layer:
    * Exp Layer:
    * Model Layer:

5. As a user, I want to see which events I am attending.
  * Reasoning: As part of the user experience, a user should be able to see the events they've signed up for.
  * Acceptance Criteria (Tests):
    * Web Layer: Should be able to visit their user home page and see their events.
    * Exp Layer: Should make a request to the Users entity to get a User's event list. Given that event list, may have to make requests to the Events entity to get more details.
    * Model Layer: Should query the db successfully for the info requested by the experience layer.

6. As a user, I want to see which experiences I am associated with.
  * Reasoning:
  * Acceptance Criteria (Tests):
    * Web Layer:
    * Exp Layer:
    * Model Layer:

7. As a user, I want to see the details of a specific event.
  * Reasoning:
  * Acceptance Criteria (Tests):
    * Web Layer:
    * Exp Layer:
    * Model Layer:

8. As a user, I want to see the details of a specific experience.
  * Reasoning:
  * Acceptance Criteria (Tests):
    * Web Layer:
    * Exp Layer:
    * Model Layer:

9. As a user, I want to see my user profile.
  * Reasoning:
  * Acceptance Criteria (Tests):
    * Web Layer:
    * Exp Layer:
    * Model Layer:

10. As a user, I want to edit my user profile.
  * Reasoning:
  * Acceptance Criteria (Tests):
    * Web Layer:
    * Exp Layer:
    * Model Layer:

11. As a user, I want to see my list of friends.
  * Reasoning:
  * Acceptance Criteria (Tests):
    * Web Layer:
    * Exp Layer:
    * Model Layer:

12. As a user, I want to add a friend. 
  * Reasoning:
  * Acceptance Criteria (Tests):
    * Web Layer:
    * Exp Layer:
    * Model Layer:

13. As a user, I want to see events my friends are going to.
  * Reasoning:
  * Acceptance Criteria (Tests):
    * Web Layer:
    * Exp Layer:
    * Model Layer:

14. As a user, I want to see experiences my friends are associated with.
  * Reasoning:
  * Acceptance Criteria (Tests):
    * Web Layer:
    * Exp Layer:
    * Model Layer:
