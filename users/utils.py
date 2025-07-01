import requests

from config.settings.base import KAKAO_AUTH_URL, KAKAO_REST_API_KEY, KAKAO_REDIRECT_PATH

def get_kakao_token(code):
    url = f'{KAKAO_AUTH_URL}/oauth/token'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    data = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_REST_API_KEY,
        "redirect_uri": KAKAO_REDIRECT_PATH,
        "code": code
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.json())
    if response.status_code == 200:
        return response.json()
    else: 
        response.raise_for_status()

def get_kakao_user_info(access_token):
    url = "https://kapi.kakao.com/v2/user/me"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        # handle errors
        response.raise_for_status()
        
def social_login_process(code):
    token_response = get_kakao_token(code)
    access_token = token_response['access_token']
    user_response = get_kakao_user_info(access_token)
    
    return user_response