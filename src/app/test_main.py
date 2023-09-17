from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "歡迎使用 Exchange Rate Server API 服務，詳情請看 /docs"}

def test_current_exchanger_rate():
    test_data = []
    test_append = test_data.append
    for source in ['TWD', 'JPY', 'USD']:
        for target in ['TWD', 'JPY', 'USD']:
            for amount in ['$1,525']:
                response = client.get(f"/api/v1/current-exchanger-rate/change?source={source}&target={target}&amount={amount}")
                test_append(response)
    
    test_ans_data = [
        {'amount': '$1,525.00', 'msg': 'success'},
        {'amount': '$5,595.23', 'msg': 'success'},
        {'amount': '$50.04', 'msg': 'success'},
        {'amount': '$411.08', 'msg': 'success'},
        {'amount': '$1,525.00', 'msg': 'success'},
        {'amount': '$13.50', 'msg': 'success'},
        {'amount': '$46,427.10', 'msg': 'success'},
        {'amount': '$170,496.53', 'msg': 'success'},
        {'amount': '$1,525.00', 'msg': 'success'}
    ]
    for i in range(0, len(test_data)):
        assert test_data[i].status_code == 200
        assert test_data[i].json() == test_ans_data[i]


def test_current_exchanger_rate_bad_query():
    response = client.get("/api/v1/current-exchanger-rate/change?source=UST&target=JPY&amount=$1,525")
    assert response.status_code == 404
    response = client.get("/api/v1/current-exchanger-rate/change?source=USD&target=JP&amount=$1,525")
    assert response.status_code == 404
    response = client.get("/api/v1/current-exchanger-rate/change?source=USD&target=JPY&amount=1,525")
    assert response.status_code == 404
    response = client.get("/api/v1/current-exchanger-rate/change?source=USD&target=JPY&amount=$1000000000000000")
    assert response.status_code == 404
    response = client.get("/api/v1/current-exchanger-rate/change?source=USD&target=JPY&amount=$-1")
    assert response.status_code == 404