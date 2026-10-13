from backend.api import create_app

def test_health():
    app = create_app()
    client = app.test_client()
    res = client.get('/api/health')
    assert res.status_code == 200
    assert res.json['status'] == 'ok'

def test_action_requires_interview_and_type():
    app = create_app()
    client = app.test_client()
    res = client.post('/api/actions', json={'interview_id': 'INT0001'})
    assert res.status_code == 400
