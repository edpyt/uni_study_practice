from user_interact.models import NewUserInfo


def save_provided_username(username: str) -> str:
    user_info = NewUserInfo(name=username)
    user_info.save()
    return str(user_info.name)
