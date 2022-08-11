# CPS Tester

<img src="cpsTesterLogo.jpeg" width="200" height="200">

> Thanks [DALL-e](https://openai.com/dall-e-2/) for the logo.

CPS tester is a fun tool that tracks your CPS, clicks per second.

<img src="cps_tester_home_image.png" width="275" height="300">

CPS tester has a history to see your past 10 runs.

<img src="cps_tester_history_image.png" width="225" height="250">

## How to install

1. Download latest release from <https://github.com/sickpancake/cps-tester/releases> to a path

2. Run `tar zxvf cps_tester-<version>.tar.gz`

3. Run `./cps_tester`

## Prerequisites

- Tkinter
- sqlite3
- pyinstaller

## Build

```bash
$ pyinstaller -F cps_tester.py 
# the dist/ directory should have `cps_tester` binary now.
```

## How to use

1. Run `python3 cps_tester.py`
2. Start testing your CPS by clicking the big clickbutton in the middle of the score screen.

3. The timer will start so start clicking the big button!
4. Once the timer runs out the button will deactivate and a score screen with pop up with your click count (score), your cps and your ranking depending on your cps. If you broke your record it will say that too.
5. You cannot exit the off the score screen. The only way is to click the ok button.

6. To open the history, click the history button on the top left.

7. Each run in history has the cps and the score. It also has the time and date it was recorded.

8. To exit out of the history or main window, click the exit button on the top left.

9. Good luck and have fun!

## Upcoming Updates

- settings window
- allow more runs to be viewed in history
- better graphics like rounded corners and own fonts, can be changed in settings window
- add a world wide highscore and a total clicks around the world both stored in a website
