import requests
from social_core.backends.oauth import BaseOAuth2

import requests
from django.http import HttpRequest

def getRole(request: HttpRequest):
    user = request.user

    # Verifica si tiene autenticación con Auth0
    auth0_users = user.social_auth.filter(provider="auth0")
    if not auth0_users.exists():
        return None  # o lanzar una excepción, según tu lógica

    auth0user = auth0_users.first()
    access_token = auth0user.extra_data.get('access_token')

    if not access_token:
        return None  # o lanzar una excepción

    url = "https://dev-7gjasd3m5ecgyzk7.us.auth0.com/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        userinfo = resp.json()
        role = userinfo.get('https://dev-7gjasd3m5ecgyzk7.us.auth0.com/role')
        
        return role
    except requests.RequestException as e:
        # Loguear el error si es necesario
        print(f"Error fetching user info: {e}")
        return None




class Auth0(BaseOAuth2):
    """Auth0 OAuth authentication backend"""
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [('picture', 'picture')]
    
    def authorization_url(self):
        
        """Return the authorization endpoint."""
        return "https://" + self.setting('DOMAIN') + "/authorize"
        
    def access_token_url(self):
        
        """Return the token endpoint."""
        
        return "https://" + self.setting('DOMAIN') + "/oauth/token"
    
    def get_user_id(self, details, response):
        
        """Return current user id."""
        
        return details['user_id']
        
    def get_user_details(self, response):
        
        url = 'https://' + self.setting('DOMAIN') + '/userinfo'
        
        headers = {'authorization': 'Bearer ' + response['access_token']}
        
        resp = requests.get(url, headers=headers)
        
        userinfo = resp.json()
        
        return {'username': userinfo['nickname'],
               'first_name': userinfo['name'],
               'picture': userinfo['picture'],
               'user_id': userinfo['sub']}
