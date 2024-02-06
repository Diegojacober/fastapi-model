from keycloak import KeycloakOpenID

# Configure client
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8181/",
                                 client_id="backend",
                                 realm_name="test",
                                 client_secret_key="Bto2tIaKaYi1IR44IsGIvGli145nsy0e")

