# whatsapp_bot
Automation whatsapp DON'T use it for spam

## Steps to use

```bash
git clone https://github.com/emichester/whatsapp_bot.git
cd whatsapp_bot
mkdir config && touch config/data.py
mkdir -p config/cache && touch config/cache/session.ini
```

Go to your favorite web browser and find the user data folder, [here](https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data) you have the firefox default directory. Once you have it:

```bash
echo "USER_DATA_PATH = 'path/to/your/user/data/folder'" > config/data.py
echo "
[SESSION]
session_id = ''
executor_url = ''
" > config/cache/session.ini
```

### If you use Firefox

Download _"geckodriver"_ from [here](https://github.com/mozilla/geckodriver/releases). Then:

```bash
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/bin/
```

[//]: # "https://github.com/mozilla/geckodriver/releases"
[//]: # "https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu"

## Extra

See more about selenium [here](https://www.selenium.dev/selenium/docs/api/py/). And for the options: [Firefox](https://www.selenium.dev/selenium/docs/api/javascript/module/selenium-webdriver/firefox_exports_Options.html), [Chrome](https://www.selenium.dev/selenium/docs/api/javascript/module/selenium-webdriver/chrome_exports_Options.html), ...