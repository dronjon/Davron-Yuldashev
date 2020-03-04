import random

pet_post_test_id = random.randint(1, 1000)
pet_put_test_data = 'Beam'
pet_update_post_test_data = 'Chapa'
tag_id = random.randint(1, 1000)
status = 'available'

user_post_name_test_data = 'davron'
username_for_login = 'user1'
password_for_login = 'password1'
username_for_update = 'davron1'

multiple_user1 = random.randint(1, 1000)
multiple_user2 = random.randint(1, 1000)


order_id = random.randint(1, 100)
pet_id = random.randint(1, 1000)



payload_for_pets = {"id": 10, "name": "doggie", "category": {"id": 1, "name": "Dogs"}, "photoUrls": ["string"],
               "tags": [{"id": 0, "name": "string"}], "status": "available"}

payload_for_users = { "id": 10,"username": "theUser1","firstName": "John","lastName": "James","email": "john@email.com",
                      "password": "12345","phone": "12345","userStatus": 1
}

payload_users_list = [{"id":100, "username": "theUser100", "firstName": "John", "lastName": "James", "email": "john@email.com",
               "password":"12345","phone":"12345","userStatus":1}, {"id":101,"username":"theUser101","firstName":"John","lastName":"James",
                                                                   "email":"john@email.com","password":"12345","phone":"12345","userStatus":1}]


payload_for_orders = {"id":10,"petId":198772,"quantity":7,"shipDate":"2020-03-01T21:18:41.004Z","status":"approved","complete":True}