import requests

access_token = 'instagram_access_token_here'

def get_user_id(access_token):
    url = f'https://graph.instagram.com/me?fields=id,username&access_token={access_token}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

user_data = get_user_id(access_token)
if user_data:
    user_id = user_data.get('id')
    username = user_data.get('username')
    print(f'Your Instagram user ID is: {user_id}')
    print(f'Your Instagram username is: {username}')
else:
    print('Failed to fetch user ID.')
