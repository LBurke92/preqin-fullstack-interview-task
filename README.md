# Preqin Technical Interview

Hello! If you are reading this, then we're in the process of chatting with you about a technical role at Preqin. Congratulations!

To move forward, we'd like to know a bit about how you work. We'd like you to demonstrate your skills and abilities. Below is a user story that reflects with work you will be doing at Preqin day to day. We would like you to deliver an e2e functional MVP of the feature, try to limit yourself to 2-3hours.

You'll then have the opportunity to showcase your work to some of our engineering team, discuss your solution, explain what you might do differently with more time, and answer any questions.

This exercise is not graded or scored; it is designed to give us a sample of your thought processes as an engineer.

## The User Story

The aim is to fulfill the following user story:

```
As a Preqin user,
I want to see a list of investors, their details and the total of their commitments.
When I click on an investor,
I want to see a breakdown of their commitments.
When I click on an Asset Class
I want to see relevant commitments.
```

Sample data is provided in `data.csv`.

How you visualise the data is up to you, but we include some wireframes just in case you want some guidance:
![Investors Listing](./wireframe-investors.png) ![Commitments Breakdown](./wireframe-investor-commitments.png)

Note: Assume a sole currency of GBP, and ignore any authentication needs.

## Technical Requirements

The solution is completely open but some technical specifications need to be met:

1. Data Layer: You must use a relational database and model the entities accordingly. We recommend `SQLite` so that you can include the database as a file with your code.

2. Backend Service: Data must be served to the consumers via an API service.

3. Webapp: A web application should consume and visualize the data from your api.

Note: You are free to use any language and frameworks. Out tech stack consists of: React micro frontends (newer ones with typescript, older ones without), Python micro services (some using REST/FastAPI others using GQL/Strawberry), and .NET (C#) for our legacy services. Bonus if you use any of these.

## Submitting your solution

Please submit your solution by sharing a public github or bitbucket with your code with the recruiter.
We ask you do not fork or PR against the Preqin repository.

Thank you and good luck!
