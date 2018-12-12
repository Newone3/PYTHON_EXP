import os

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

# cd     vrati do homu
# vim .bash_profile    tady se nastavuji promeny

# export db_user='my_db_user'
# export db_password='my_db_pass_123!'

print(db_user)
print(db_password)


