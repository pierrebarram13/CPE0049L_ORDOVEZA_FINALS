from src.services.jwt_service import generate_token, verify_token

token = generate_token("Pierre")

print("Generated Token:")
print(token)

print()

print("Decoded Token:")
print(verify_token(token))