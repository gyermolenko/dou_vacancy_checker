# dou_vacancy_checker
Use this script to check http://jobs.dou.ua/vacancies for updates.
Get list of vacancies for "search-word" specified as argument (or for 'python' by default)

 It uses **selenium** to get full list (clicks "more-btn" as long as it is on a page).
 And since it uses pyvirtualdisplay for invisible Chrome - you will need to put [chromedriver] (https://sites.google.com/a/chromium.org/chromedriver/downloads) in the same folder.

## Examples:

`python dou_vacancy_checker.py`

`python dou_vacancy_checker.py '-s','--search' ['-c','--city']`

