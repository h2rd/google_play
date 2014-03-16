import unittest

from google_play import (leaderboard, search, developer,
                         app, FREE, PAID)

class Developer(unittest.TestCase):
    def test_not_exists_developer(self):
        apps = developer('twitter')
        self.assertIsNone(apps)

    def test_twitter_with_numbers(self):
        apps = developer('Twitter, Inc.')
        self.assertIsInstance(apps, list)
        self.assertEqual(len(apps), 2)


class Search(unittest.TestCase):
    def test_twitter(self):
        apps = search('twitter')
        self.assertIsInstance(apps, list)
        self.assertEqual(len(apps), 24)

    def test_twitter_with_numbers(self):
        apps = search('twitter', num=5)
        self.assertIsInstance(apps, list)
        self.assertEqual(len(apps), 5)

    def test_twitter_next_5_apps(self):
        apps1 = search('twitter', num=5)
        apps2 = search('twitter', num=5, start=5)

        self.assertIsInstance(apps2, list)
        self.assertEqual(len(apps2), 5)
        self.assertNotEqual(apps1, apps2)


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

    def test_numDownloads_problem(self):
        a = app('com.wHow2Makeapanelmould')
        self.assertIsInstance(a, dict)

    def test_images_test(self):
        a = app('kaus.mmautotrader.com')
        self.assertIsInstance(a['images'], list)
        self.assertNotEqual(len(a['images']), 0)

    def test_developer_email(self):
        a = app('com.pressmatrix.cimmagazine')
        self.assertEqual(a['developer_website'], '')

    def test_app_info(self):
        a = app('com.twitter.android')

        self.assertIsInstance(a, dict)
        self.assertEqual(a['title'], 'Twitter')
        self.assertEqual(a['package_name'], 'com.twitter.android')
        self.assertEqual(a['developer_name'], 'Twitter, Inc.')
        self.assertEqual(a['category'], 'Social')
        self.assertEqual(a['price'], '0')
        self.assertEqual(a['developer_website'], 'https://support.twitter.com/articles/20169915')
        self.assertEqual(a['developer_email'], 'android-support@twitter.com')
        self.assertEqual(a['url'], 'https://play.google.com/store/apps/details?id=com.twitter.android&hl=en')
        self.assertNotEqual(len(a['images']), 0)
        self.assertNotEqual(len(a['similar']), 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
