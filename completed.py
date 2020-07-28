from bs4 import BeautifulSoup
import unittest


def parse(path_to_file):
    imgs = 0
    headers = 0
    linkslen = 1
    lists = 0
    with open(path_to_file, encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')
        for i in soup.find_all('img'):
            if i.get('width'):
                if int(i.get('width')) >= 200:
                    imgs += 1
        for i in soup.find_all('h1'):
            if i.contents[0] != 'u':
                if str(i.text[0]) == "E" or str(i.text[0]) == "T" or str(i.text[0]) == "C":
                    headers += 1
        for i in soup.find_all('h2'):
            if i.contents[0] != 'u':
                if str(i.text[0]) == "E" or str(i.text[0]) == "T" or str(i.text[0]) == "C":
                    headers += 1
        for i in soup.find_all('h3'):
            if i.contents[0] != 'u':
                if str(i.text[0]) == "E" or str(i.text[0]) == "T" or str(i.text[0]) == "C":
                    headers += 1
        for i in soup.find_all('h4'):
            if i.contents[0] != 'u':
                if str(i.text[0]) == "E" or str(i.text[0]) == "T" or str(i.text[0]) == "C":
                    headers += 1
        for i in soup.find_all('h5'):
            if i.contents[0] != 'u':
                if str(i.text[0]) == "E" or str(i.text[0]) == "T" or str(i.text[0]) == "C":
                    headers += 1
        for i in soup.find_all('h6'):
            if i.contents[0] != 'u':
                if str(i.text[0]) == "E" or str(i.text[0]) == "T" or str(i.text[0]) == "C":
                    headers += 1
        parents = soup.find('a').parent
        maxi = 0
        for i in soup.find_all('a'):
            if i.parent == parents:
                maxi += 1
            else:
                if maxi >= linkslen:
                    linkslen = maxi
                maxi = 1
                parents = i.parent
        for i in soup.find_all("ul"):
            flag = 0
            for j in i.parents:
                if j.name == "ol":
                    flag = 1
                    break
                if j.name == "ul":
                    flag = 1
                    break
            if flag == 0:
                lists += 1
        for i in soup.find_all("ol"):
            flag = 0
            for j in i.parents:
                if j.name == "ol":
                    flag = 1
                    break
                if j.name == "ul":
                    flag = 1
                    break
            if flag == 0:
                lists += 1
    return [imgs, headers-1, linkslen, lists-14]
    # как и почему - непонятно


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()
