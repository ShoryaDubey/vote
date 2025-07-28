def test_index():
    import app
    with app.app.test_client() as client:
        res = client.get("/")
        assert res.status_code == 200
