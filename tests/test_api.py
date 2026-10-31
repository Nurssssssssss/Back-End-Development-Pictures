"""11 checks grouped in the same sequence as the IBM lab's checkpoints."""

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200 and res.json['status']=='OK'

def test_count(client):
    res = client.get('/count')
    assert res.status_code == 200 and res.json['length']==10

def test_data_contains_10_pictures(client):
    assert len(client.get('/picture').json)==10

def test_get_picture(client):
    res=client.get('/picture')
    assert res.status_code==200 and len(res.json)==10

def test_get_pictures_check_content_type_equals_json(client):
    assert client.get('/picture').content_type=='application/json'

def test_get_picture_by_id(client):
    assert client.get('/picture/2').json['id']==2
    assert client.get('/picture/404').status_code==404

def test_pictures_json_is_not_empty(client):
    assert client.get('/picture').json

def test_post_picture(client,picture):
    res=client.post('/picture',json=picture)
    assert res.status_code==201 and res.json['id']==200
    assert client.get('/count').json['length']==11

def test_post_picture_duplicate(client,picture):
    assert client.post('/picture',json=picture).status_code==201
    res=client.post('/picture',json=picture)
    assert res.status_code==302
    assert res.json['Message']=='picture with id 200 already present'

def test_update_picture_by_id(client):
    before=client.get('/picture/2').json
    res=client.put('/picture/2',json={'event_state':'*'+before['event_state']})
    assert res.status_code==200
    assert client.get('/picture/2').json['event_state'].startswith('*')

def test_delete_picture_by_id(client):
    assert client.delete('/picture/1').status_code==204
    assert client.get('/count').json['length']==9
    assert client.delete('/picture/100').status_code==404
