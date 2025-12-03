### hh_sru

the selenium bot responding to vacancies on hh.ru

### choose which browser to use

despite the fact that i am a firefox user and a big fan of firefox, `hh_sru` uses chromium by default, because hh.ru is known to have shit performance in firefox

especially when when using dark reader, and when using developer tools (ctrl+shift+i)

if you want the bot to use firefox, edit the `engine_to_use` parameter in `hh_sru/config.py`

### running

- i will use toolbox because i don't want to pollute my host system by installing chromium
- `toolbox enter`
- now we should install chromium or firefox, pick whichever you like more
- `sudo dnf install chromium` - for chromium
- `sudo dnf install firefox` - for firefox
- after the browser is installed, run the bot
- `python -m ensurepip`
- `pip install -U uv`
- `uv run -m hh_sru`
