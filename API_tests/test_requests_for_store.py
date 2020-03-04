from import_library import *

payload_for_users['username'] = user_post_name_test_data

class TestStoreRequests():
    def get_inventory(self):
        return requests.get(base_url + '/store/inventory/', headers=headers)

    def place_an_order(self):
        payload_for_orders['id'] = order_id
        payload_for_orders['petId'] = pet_id
        return requests.post(base_url + '/store/order/', data=json.dumps(payload_for_orders), headers=headers)

    def find_purchase_order_by_id(self):
        return requests.get(base_url + '/store/order/' + str(order_id), headers=headers)

    def delete_order(self):
        return requests.delete(base_url + '/store/order/' + str(order_id), headers=headers)

    def test_get_inventory(self):
        request_outputs = self.get_inventory()
        assert request_outputs.status_code == 200
        assert request_outputs.json()['placed'] == 100
        assert request_outputs.json()['delivered'] == 50

    def test_placing_an_order(self):
        request_outputs = self.place_an_order()
        assert request_outputs.status_code == 200
        assert request_outputs.json()['id'] == order_id
        assert request_outputs.json()['petId'] == pet_id

    def test_find_purchase_by_id(self):
        request_outputs = self.find_purchase_order_by_id()
        assert request_outputs.status_code == 200
        assert request_outputs.json()['id'] == order_id

    def test_deleted_order(self):
        request_outputs = self.delete_order()
        assert request_outputs.status_code == 200
        response = requests.get(base_url + '/store/order/' + str(order_id), headers=headers)
        assert response.status_code == 404