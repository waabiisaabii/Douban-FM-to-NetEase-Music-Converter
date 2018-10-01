import requests

from douban_util import urls

def get_douban_dbcl2(username, password):

    print 'Logging in: ' + username

    http_login_data = "source=fm" \
                 "&referer=https://douban.fm/user-guide" \
                 "&ck=" \
                 "&name=" + username + \
                 "&password=" + password + \
                 "&captcha_solution=" \
                 "&captcha_id="
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    req = requests.post(url=urls.url_login,
                        data=http_login_data,
                        headers=headers)

    print 'HTTP status: ', req.status_code
    if (req.status_code is not 200):
        raise Exception("Unexpected response code")

    return get_douban_dbcl2_from_cookie(req)

def get_douban_dbcl2_from_cookie(req):
    return req.cookies._cookies['.douban.com']['/']['dbcl2'].value