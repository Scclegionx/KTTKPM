from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user, backend):
    refresh = RefreshToken.for_user(user)
    refresh['backend'] = backend  # Thêm backend vào payload
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
