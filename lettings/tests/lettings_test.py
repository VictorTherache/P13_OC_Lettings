from django.urls import reverse
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize('url, apps', [
    ['lettings:index', ('oc_lettings_site:index', 'profiles:index')]
])
def test_render_lettings(client, url, apps, create_test_address, create_test_letting):
    url = reverse(url)
    resp = client.get(url)
    urls_redirection_apps = [reverse(app) for app in apps]

    assert resp.status_code == 200

    assert b"<title>Lettings</title>" in resp.content

    assert f"""<a href="{url}{create_test_letting.id}/">""".encode('utf-8') in resp.content

    for url in urls_redirection_apps:
        assert f"""<a href="{url}">""".encode('utf-8') in resp.content


@pytest.mark.django_db
@pytest.mark.parametrize('url, apps', [
    ['lettings:letting', ('oc_lettings_site:index', 'lettings:index', 'profiles:index')]
])
def test_render_letting_address_informations(client, url, apps, create_test_address,
                                             create_test_letting):

    url = reverse(url, kwargs={'letting_id': create_test_letting.id})
    resp = client.get(url)
    urls_redirection_apps = [reverse(app) for app in apps]
    informations_letting = [create_test_address.__str__(),
                            f"{create_test_address.city}, {create_test_address.state} "
                            f"{create_test_address.zip_code}",
                            f"{create_test_address.country_iso_code}"]

    assert resp.status_code == 200

    assert f"""<title>{create_test_letting.title}</title>""".encode('utf-8') in resp.content

    for url in urls_redirection_apps:
        assert f"""<a href="{url}">""".encode('utf-8') in resp.content

    for information in informations_letting:
        assert f"""<p>{information}</p>""".encode('utf-8') in resp.content
