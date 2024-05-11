# Brute Force

## low

see `hydra.sh`

user|password
-|-
admin|password
gordonb|abc123
1337|charley
pablo|letmein
smithy|password

## medium

set hydra's wait time to 1 second (`-w 1`)

## high

brute force with csrf token

- in burpsuite: `Settings->Sessions->Session handling rules->Add->Rule actions->Add->Run a marco->Add`

- select the GET request

- in `Configure item`, add a new custom parameter called 'user_token' between `value='` and `'`

- applying to scope `http://localhost/vulnerabilities/brute/`

- select `Send to intruder`

- set maximum concurrent requests = 1 at `Resource pool->Create a new resource pool`
  (this step turns off multithread because new request renders old csrf token useless)
