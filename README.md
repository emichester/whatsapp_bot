# whatsapp_bot
Automation whatsapp DON'T use it for spam

## Setup

```bash
$ git clone https://github.com/emichester/whatsapp_bot.git
$ cd whatsapp_bot
$ mkdir config && touch config/data.py
$ mkdir -p config/session && touch config/session/session.ini
$ touch messages.py
$ echo "
[SESSION]
session_id = ''
executor_url = ''
" > config/session/session.ini
$ 
$ chmod +x bot_whatsapp_firefox_init.py
$ chmod +x bot_whatsapp_firefox_instance.py
```

Go to your favorite web browser and find the user data folder, [here](https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data) you have the firefox default directory. Once you have it:

```bash
$ echo "USER_DATA_PATH = 'path/to/your/user/data/folder'" > config/data.py
```

### If you use Firefox

Download _"geckodriver"_ from [here](https://github.com/mozilla/geckodriver/releases). Then:

```bash
$ tar -xvzf geckodriver*
$ chmod +x geckodriver
$ sudo mv geckodriver /usr/bin/
```

[//]: # "https://github.com/mozilla/geckodriver/releases"
[//]: # "https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu"
[//]: # "https://tarunlalwani.com/post/reusing-existing-browser-session-selenium/"

## Usage

Define the messages you want to be sent by oppening `messages.py`, look at the following example.
```python
messages = {
    'contact 1' : """
The message for the contact 1.
The last line will be sent alone as it has a \\n at the end of the line.
""",
    'contact 2' : """This message will be sent all together because it doesn't have a endline character. This one also.""",
}
```

Open a bash (_main bash_) in the folder, install the _requirements.txt_ and do the following.

```bash
$ ./bot_whatsapp_firefox_init.py
```

Scan the QR code (I couldn't automate this step), and in another bash.

```bash
$ ./bot_whatsapp_firefox_instance.py
```

Modify the instance for the purpose you want to use it.

**IMPORTANT:** to close the webdriver just press enter in the _main bash_, this will automatically close the webdriver. Or you can call the _close_father_webdriver(drive)_ method to it.

## Extra

See more about selenium [here](https://www.selenium.dev/selenium/docs/api/py/). And for the options: [Firefox](https://www.selenium.dev/selenium/docs/api/javascript/module/selenium-webdriver/firefox_exports_Options.html), [Chrome](https://www.selenium.dev/selenium/docs/api/javascript/module/selenium-webdriver/chrome_exports_Options.html), ...

[//]: # " https://stackoverflow.com/questions/4823468/comments-in-markdown"
[//]: # " https://stackoverflow.com/questions/31248804/is-it-possible-to-locate-element-by-partial-id-match-in-selenium"
[//]: # " https://stackoverflow.com/questions/25807473/webobject-getattributetitle-does-not-work-in-python-any-idea-about-it"
[//]: # " https://selenium-python.readthedocs.io/index.html"
[//]: # " https://stackoverflow.com/questions/58759768/selenium-find-element-by-class-name-two-parameters"
[//]: # " "
[//]: # " "