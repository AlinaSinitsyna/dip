import sender_stand_request
import data

def test_reserving_orders_trak():
    order_payload = data.orders_body.copy()
    order_response = sender_stand_request.post_new_orders(order_payload)
    assert order_response.status_code == 201
    track = order_response.json()['track']
    assert track is not None
    order_by_track = sender_stand_request.get_order_by_track(track)
    assert order_by_track.status_code == 200
    assert track == order_by_track.json()['order']['track']
