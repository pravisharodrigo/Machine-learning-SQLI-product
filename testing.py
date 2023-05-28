import injectsqli

input = "1' or '1'='1"
api_key = "91b9eff33ab17f1b691dc8d5bc6332cc"

print(injectsqli.predict(input,api_key))