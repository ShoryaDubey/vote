import app

def test_vote_success():
    with app.app.test_client() as client:
        res = client.post("/vote", json={"option": "Option A"})
        assert res.status_code == 200

def test_vote_invalid():
    with app.app.test_client() as client:
        res = client.post("/vote", json={"option": "Invalid"})
        assert res.status_code == 400
