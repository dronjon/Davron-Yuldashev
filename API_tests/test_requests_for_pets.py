from import_library import *

payload_for_pets['id'] = pet_post_test_id
payload_for_pets['tags'][0]['id'] = tag_id


class TestPetRequests():
    def create_new_entry(self):
        return requests.post(base_url + '/pet', data=json.dumps(payload_for_pets), headers=headers)

    def get_data_by_id(self):
        return requests.get(base_url + '/pet/' + str(pet_post_test_id), headers=headers)

    def get_data_by_tag_id(self):
        return requests.get(base_url + '/pet/findByTags?tags=' + str(tag_id), headers=headers)

    def get_data_by_status(self):
        payload_for_pets['status'] = status
        return requests.get(base_url + '/pet/findByStatus?status=' + str(status), headers=headers)

    def update_name(self):
        payload_for_pets['id'] = pet_post_test_id
        payload_for_pets['name'] = pet_put_test_data
        return requests.put(base_url + '/pet', data=json.dumps(payload_for_pets), headers=headers)

    def update_existing_data_using_post(self):
        payload_for_pets['id'] = pet_post_test_id
        payload_for_pets['name'] = pet_update_post_test_data
        return requests.post(base_url + '/pet/' + str(pet_post_test_id) + '?name=' + pet_update_post_test_data + '&status=' + status)

    def upload_image(self):
        files = {'upload_file': open(os.getcwd() + '/test_data/dog.jpg', 'rb')}
        return requests.post(base_url + '/pet/' + str(pet_post_test_id) + '/uploadImage', files=files, headers={"Content-Type": "application/octet-stream"})

    def delete_entry(self):
        return requests.delete(base_url + '/pet/' + str(pet_post_test_id), headers=headers)

    def response_for_non_existing_animal(self):
        return requests.get(base_url + '/pet/' + str(pet_post_test_id), headers=headers)

    def test_user_can_create_new_entry_of_pets(self):
        request_output = self.create_new_entry()
        assert request_output.status_code == 200
        assert request_output.json()['id'] == pet_post_test_id

    def test_user_can_view_newly_created_animal(self):
        request_output = self.get_data_by_id()
        assert request_output.status_code == 200
        assert request_output.json()['id'] == pet_post_test_id

    def test_find_pet_by_status(self):
        request_output = self.get_data_by_status()
        assert request_output.status_code == 200
        assert request_output.json()[0]['status'] == status

    # TODO the option of finding tag by id does not work and returns empty list and returns 200 status code regardless of data existence
    @pytest.mark.skip(reason='api does not work')
    def test_pet_can_be_verified_by_tag_id(self):
        request_output = self.get_data_by_tag_id()
        assert request_output.status_code == 200
        assert request_output.json()['tags'][0]['id'] == tag_id

    def test_user_can_change_dog_name(self):
        request_output = self.update_name()
        assert request_output.status_code == 200
        assert request_output.json()['name'] == pet_put_test_data

    def test_user_can_change_pet_name_with_post(self):
        request_output = self.update_existing_data_using_post()
        assert request_output.status_code == 200
        assert request_output.json()['name'] == pet_update_post_test_data

    def test_uploaded_image(self):
        requests_outputs = self.upload_image()
        assert requests_outputs.status_code == 200
        assert len(requests_outputs.json()['photoUrls']) > 1

    def test_delete_entry(self):
        request_output = self.delete_entry()
        assert request_output.status_code == 200

    def test_response_for_non_existing_entry(self):
        request_output = self.response_for_non_existing_animal()
        assert request_output.status_code == 404