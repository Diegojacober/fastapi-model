import jwt
import base64
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicNumbers
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import json
from urllib.request import urlopen

def token_is_valid(tenant_id, client_id, token):
    jwks_url = f"https://login.microsoftonline.com/{tenant_id}/discovery/v2.0/keys"
    issuer_url = f"https://login.microsoftonline.com/0ae51e19-07c8-4e4b-bb6d-648ee58410f4/v2.0"

    jwks = json.loads(urlopen(jwks_url).read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = find_rsa_key(jwks, unverified_header)
    public_key = rsa_pem_from_jwk(rsa_key)

    return jwt.decode(
      token,
      public_key,
      verify=True,
      algorithms=["RS256"],
      issuer=issuer_url,
      options={"verify_aud": False,}
    )
    
    # -_F8Q~FssOIFAtAWLo9wHyMKiLzppKmC6culgafX

def find_rsa_key(jwks, unverified_header):
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            return {
              "kty": key["kty"],
              "kid": key["kid"],
              "use": key["use"],
              "n": key["n"],
              "e": key["e"]
            }

def ensure_bytes(key):
    if isinstance(key, str):
        key = key.encode('utf-8')
    return key


def decode_value(val):
    decoded = base64.urlsafe_b64decode(ensure_bytes(val) + b'==')
    return int.from_bytes(decoded, 'big')


def rsa_pem_from_jwk(jwk):
    return RSAPublicNumbers(
        n=decode_value(jwk['n']),
        e=decode_value(jwk['e'])
    ).public_key(default_backend()).public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSJ9.eyJhdWQiOiJhMjg1MmUyMC03ZDYxLTRlOWMtOTljZC0zNTUxMzY4MjliMmQiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vMGFlNTFlMTktMDdjOC00ZTRiLWJiNmQtNjQ4ZWU1ODQxMGY0L3YyLjAiLCJpYXQiOjE3MDkxNDE0ODAsIm5iZiI6MTcwOTE0MTQ4MCwiZXhwIjoxNzA5MTQ1MzgwLCJuYW1lIjoiRVRTLUVuZ2luZWVyaW5nVGVjaG5pY2FsU2Nob29sIEJPVC1SZXNlYXJjaERldmVsb3BtZW50IChDYVAvRVRTKSIsIm5vbmNlIjoiMDE4ZGYwYzktZGE1Yi03YzQzLTk4OTMtMTgxZTI5MjZmMmMzIiwib2lkIjoiYWUxZTdmMDMtY2EyNy00NTRkLTkyMjgtYjcyMzgxYjVjMzFjIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiY3Q2N2NhQGJvc2NoLmNvbSIsInJoIjoiMC5BU0VBR1I3bENzZ0hTMDY3YldTTzVZUVE5Q0F1aGFKaGZaeE9tYzAxVVRhQ215MGhBQmMuIiwicm9sZXMiOlsiYWRtaW4iXSwic3ViIjoiS0tkUG52ZjlkVTI0cjBUYjdUaVlBY194UF8xYXlMOUNJd3pPYmFFckFORSIsInRpZCI6IjBhZTUxZTE5LTA3YzgtNGU0Yi1iYjZkLTY0OGVlNTg0MTBmNCIsInV0aSI6Im5aQkd6SmZFY0VLT3ZPeThYVWtlQUEiLCJ2ZXIiOiIyLjAifQ.EdXrf16VtQOuq83wUupzMS0-D5nZYD1rtEMDQ9W_jr9PRUc1sKqXUMn9p49IwKzemGrzKMftHmYcaCd5YJc-LZLq07ids00570a9RKD1DW8xKlW6tXSSib3ZQrTFf-YZxgJh4pBvPp65kWpjqsi0oXb9dRSIwfwWtzl-7GDq_1z2WSAPsObvoQtn6dL2Xv-a1hHODLl-TR9M_KDl8jxz9LCLbOKASOQTpBYQ3_9u22uMuClUu_68DXVSiTwThakT9sVoyxAy6GPILDp4wueRrM8IuNHUesYT2euhCXEpmTchR0asDeHrZG42V-0wNjA0u8Nevfo5CH_LG28zzEN56Q"
tenant = "0ae51e19-07c8-4e4b-bb6d-648ee58410f4"
app = "a2852e20-7d61-4e9c-99cd-355136829b2d"
print(token_is_valid(tenant, app, token))