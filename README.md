# `A Simple RESTful API`

Implemented using Flask-RESTFul, Flask-JWT and Flask-SQLAlchemy.

Hosted on Heroku https://api-david.herokuapp.com/

Has the following resources and endpoints respectively:
1. UserRegister `POST /signup {"username": string, "password": string}`
2. UsersList  `GET /users `
3. User `GET /user/<string:name>`
4. ItemList `GET /items`
5. Item `GET or DELETE /item/<string:name>`
6. Item `POST or PUT /item/<string:name> {"price": float, "store_id": int}`
7. StoresList `GET /stores`
8. Store `GET or POST or DELETE /item/<string:name>`

###### Not an API in production though, but only for learning purpose