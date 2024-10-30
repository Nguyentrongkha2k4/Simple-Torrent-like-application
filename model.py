from database import connect_mongodb


def get_all_users():
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    data = collection.find()
    user_list = []
    for row in data:
        user_list.append(row.get('username'))
    client.close()
    return user_list

def get_user_password(username):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    data = collection.find_one({'username': username})
    client.close()
    return data.get('password')

def get_user_file(username):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    user = collection.find_one({'username': username})
    file_list = []
    for file in user.get('filename'):
        file_list.append(file.get('filename'))
    client.close()
    return file_list

def add_new_user(username, password):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    # if get_user_password(username) != "":
    #     client.close()
    #     return False
    try:
        data={
            'username': username,
            'password': password,
            'filename': [],
            'status': 'inactive',
            'ipaddress': "",
            'port': ""
        }
        sid = collection.insert_one(data)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        client.close() 

def add_onl_user(username):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    collection.update_one({'username': username}, {'$set': {'status': 'active'}})
    client.close()
    return True

def remove_onl_user(username):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    collection.update_one({'username': username}, {'$set': {'status': 'inactive'}})
    client.close()
    return True

def get_onl_users():
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    data = collection.find({'status': 'active'})
    user_onl_list = []
    for user in data:
        user_onl_list.append(user.get('username'))
    client.close()
    return user_onl_list

def delete_all_onl_users():
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    collection.update_many({'status':'active'}, {"$set": { "status": "inactive" }})
    client.close()
    return True

def delete_user(username):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    collection.delete_one({'username': username})
    client.close()
    return True

def add_new_file(username, filename, filepath, status = []):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    userdata = collection.find_one({'username': username})
    userdata.get('filename').append({'filename': filename, 'filepath': filepath, 'status': status})
    collection.update_one({'_id': userdata.get('_id')}, {'$set': userdata})
    client.close()
    return True

def delete_file(username, filename):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    userdata = collection.find_one({'username': username})
    userdata.get('filename').remove({'filename': filename})
    collection.update_one({'_id': userdata.get('_id')}, {'$set': userdata})
    client.close()
    return True

def search_file_name(filename):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    data = collection.find({'filename.filename':filename})
    user_list = []
    for user in data:
        user_list.append(user.get('username'))
    client.close()
    return user_list
def update_user_password(username, password):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    collection.update_one({'username': username}, {"$set": {'password': password}})
    client.close()
    return
def update_user_address_port(username, address, port):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    collection.update_one({'username': username}, {"$set": {"address": address, "port": port}})
    client.close()
    return

def delete_all_users():
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    collection.delete_many({})
    client.close()
    return True
def get_path_by_filename(username, filename):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    path = collection.find_one({'username': username}).get('filename')
    for file in path:
        if file.get('filename') == filename:
            return file.get('filepath')
    client.close()
    return ""
def get_status_file(username, filename):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    path = collection.find_one({'username': username}).get('filename')
    for file in path:
        if file.get('filename') == filename:
            return file.get('status')
    client.close()
    return []
def update_status_file(username, filename, status = []):
    client = connect_mongodb()
    database = client['networkapp']
    collection = database['users']
    path = collection.find_one({'username': username}).get('filename')
    for file in path:
        if file.get('filename') == filename:
            file.update({'status': status})
    collection.update_one({'_id': collection.find_one({'username': username}).get('_id')}, {'$set': {'filename': path}})
    client.close()
    return