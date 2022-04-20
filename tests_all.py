from django.urls import reverse
import pytest


@pytest.mark.parametrize('url, apps', [
    ['index', ('profiles:index', 'lettings:index')]
])
def test_render_home(client, url, apps):
    url = reverse(url)
    resp = client.get(url)
    urls_apps = [reverse(app) for app in apps]

    assert resp.status_code == 200

    assert b"<title>Holiday Homes</title>" in resp.content
    print(resp.content)

    for url in urls_apps:
        assert f"""<a href="{url}">""".encode('utf-8') in resp.content
