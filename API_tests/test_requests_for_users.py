from import_library import *

payload_for_users['username'] = user_post_name_test_data

class TestUserRequests():
    def create_new_entry_of_users(self):
        return requests.post(base_url + '/user/', data=json.dumps(payload_for_users), headers=headers)

    def create_users_with_list(self):
        payload_users_list[0]['id'] = multiple_user1
        payload_users_list[1]['id'] = multiple_user2
        return requests.post(base_url + '/user/createWithList', data=json.dumps(payload_users_list), headers=headers)

    def login_user(self):
        return requests.get(base_url + '/user/login?username=' + username_for_login + '&password=' + password_for_login)

    def get_user_by_username(self):
        return requests.get(base_url + '/user/' + user_post_name_test_data, headers=headers)

    def update_user_with_put(self):
        payload_for_users['username'] = username_for_update
        return requests.put(base_url + '/user/' + user_post_name_test_data, data=json.dumps(payload_for_users), headers=headers)

    def delete_user(self):
        return requests.delete(base_url + '/user/' + username_for_update, headers=headers)

    def test_user_can_create_new_entry_for_users(self):
        request_output = self.create_new_entry_of_users()
        assert request_output.status_code == 200
        assert request_output.json()['username'] == user_post_name_test_data

    def test_create_users_with_list(self):
        requests_output = self.create_users_with_list()
        assert requests_output.status_code == 200
        assert requests_output.json()[0]['id'] == multiple_user1
        assert requests_output.json()[1]['id'] == multiple_user2

    def test_user_can_login(self):
        request_output = self.login_user()
        assert request_output.status_code == 200

    def test_get_user_by_username(self):
        request_output = self.get_user_by_username()
        assert request_output.status_code == 200
        assert request_output.json()['username'] == user_post_name_test_data

    def test_username_is_updated(self):
        request_output = self.update_user_with_put()
        assert request_output.status_code == 200
        assert request_output.json()['username'] == username_for_update

    def test_user_is_deleted(self):
        request_output = self.delete_user()
        assert request_output.status_code == 200
        response = requests.get(base_url + '/user/' + username_for_update, headers=headers)
        assert response.status_code == 404
