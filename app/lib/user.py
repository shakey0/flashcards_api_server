class User:
    
    def __init__(self, id, username, email, oauth_provider, oauth_id, magic_link_token,
                magic_link_expiry, refresh_token, is_active, last_login, created_at, updated_at):
        self.id = id
        self.username = username
        self.email = email
        self.oauth_provider = oauth_provider
        self.oauth_id = oauth_id
        self.magic_link_token = magic_link_token
        self.magic_link_expiry = magic_link_expiry
        self.refresh_token = refresh_token
        self.is_active = is_active
        self.last_login = last_login
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"<User {self.id} {self.username} {self.email} {self.oauth_provider} {self.oauth_id} {self.magic_link_token} 
            {self.magic_link_expiry} {self.refresh_token} {self.is_active} {self.last_login} {self.created_at} {self.updated_at}>"
