import unittest

from google_play import (leaderboard, search, developer,
                         app, FREE, PAID)

class Developer(unittest.TestCase):
    def test_not_exists_developer(self):
        apps = developer('twitter', start=20)
        self.assertEqual(len(apps), 0)

    def test_twitter_with_numbers(self):
        apps = developer('Twitter, Inc.')
        self.assertIsInstance(apps, list)
        self.assertEqual(len(apps), 2)

    def test_zynga_first_five(self):
        apps = developer('Zynga', num=5)
        self.assertIsInstance(apps, list)
        self.assertEqual(len(apps), 5)

    def test_zynga_first_ten(self):
        apps = developer('Zynga', num=10)
        self.assertIsInstance(apps, list)
        self.assertEqual(len(apps), 10)


class Search(unittest.TestCase):
    def test_twitter(self):
        apps = search('twitter')
        self.assertIsInstance(apps, list)
        self.assertEqual(len(apps), 20)


class Leaderboard(unittest.TestCase):
    def test_FREE_leaderboard(self):
        apps = leaderboard(FREE)
        self.assertIsInstance(apps, list)
        self.assertEqual(len(apps), 24)

    def test_PAID_leaderboard(self):
        apps = leaderboard(PAID)
        self.assertIsInstance(apps, list)
        self.assertEqual(len(apps), 24)

    def test_PAID_with_category(self):
        apps = leaderboard(PAID, 'health_and_fitness', num=5)
        self.assertIsInstance(apps, list)
        self.assertEqual(len(apps), 5)

    def test_search_next_5_apps(self):
        apps1 = leaderboard(PAID, 'health_and_fitness', num=5)
        apps2 = leaderboard(PAID, 'health_and_fitness', num=5, start=5)

        self.assertIsInstance(apps2, list)
        self.assertEqual(len(apps2), 5)
        self.assertNotEqual(apps1, apps2)


class Apps(unittest.TestCase):
    def test_not_found_app(self):
        a = app('google.super.app')
        self.assertIsNone(a)

    def test_images_test(self):
        a = app('com.instagram.android')
        self.assertIsInstance(a['images'], list)
        self.assertNotEqual(len(a['images']), 0)

    def test_pressmatrix(self):
        a = app('com.pressmatrix.cimmagazine')
        self.assertEqual(a['title'], 'CIM Kiosk')
        self.assertEqual(a['category'], 'News & Magazines')
        self.assertEqual(a['developer_name'], 'DVV Media Group GmbH')
        self.assertIsInstance(a['images'], list)
        self.assertNotEqual(len(a['images']), 14)
        self.assertEqual(a['developer_email'], 'info@cimunity.com')
        self.assertIsInstance(a['similar'], list)
        self.assertEqual(a['developer_website'], 'http://www.cimunity.com/home/')

    def test_setupgroup_app(self):
        a = app('com.setupgroup.xo.free')
        self.assertEqual(a['title'], 'XO Demo')
        self.assertEqual(a['category'], 'Puzzle')
        self.assertEqual(a['developer_name'], 'Setup Group')
        self.assertEqual(a['developer_email'], 'mokun@setupgroup.com')
        self.assertEqual(a['developer_website'], 'http://wwww.setupgroup.com')

    def test_app_info(self):
        a = app('com.twitter.android')
        self.assertIsInstance(a, dict)
        self.assertEqual(a['title'], 'Twitter')
        self.assertEqual(a['package_name'], 'com.twitter.android')
        self.assertEqual(a['developer_name'], 'Twitter, Inc.')
        self.assertEqual(a['category'], 'Social')
        self.assertEqual(a['price'], '0')
        self.assertEqual(a['developer_website'], 'https://support.twitter.com/articles/20169915')
        self.assertEqual(a['developer_email'], 'google-play-emails@twitter.com')
        self.assertEqual(a['url'], 'https://play.google.com/store/apps/details?id=com.twitter.android&hl=en&c=apps')
        self.assertNotEqual(len(a['images']), 0)
        self.assertNotEqual(len(a['similar']), 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
