def test_get_results(monkeypatch):
    import app
    def mock_get_votes():
        class MockResponse:
            def json(self):
                return {"Option A": 3, "Option B": 2}
        return MockResponse()

    monkeypatch.setattr(app.requests, "get", lambda *a, **kw: mock_get_votes())
    with app.app.test_client() as client:
        res = client.get("/results")
        assert res.status_code == 200